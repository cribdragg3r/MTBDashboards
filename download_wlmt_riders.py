import pandas as pd
from tqdm import tqdm
from pprint import pprint
from concurrent.futures import as_completed, ThreadPoolExecutor
from PyForks.user import User
from PyForks.region import Region
import PyForks.exceptions


USERNAME = ""
PASSWORD = ""

tf_user = User(username=USERNAME, password=PASSWORD)
tf_user.login()

def run_job(users: list) -> list:
    results = []
    thread_list = []
    pbar = tqdm(total=len(users))
    with ThreadPoolExecutor() as executor:
        thread_list = [ executor.submit(tf_user.get_user_info, user) for user in users ]
        pbar.update(1)
        
    for thread in as_completed(thread_list):
        try:
            results.append(thread.result())
        except PyForks.exceptions.InvalidUser as e:
            pass
    pbar.close()
    return results


df = pd.read_csv("./data/region_ridelogs.csv")
df = df[df["region"] == "west-lake-marion-park"]

wlmt_riders = df.username.unique().tolist()

raw_data = run_job(wlmt_riders)
final_df = pd.DataFrame.from_dict(raw_data)
final_df.to_csv("data/wlmt_riders.csv", index=False)

