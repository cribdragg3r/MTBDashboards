from PyForks.trailforks_region import TrailforksRegion
from PyForks.trailforks_user import TrailforksUser
import pandas as pd
from tqdm import tqdm

USERNAME = "mnmtb"
PASSWORD = ""

region_to_id_map = {
    "battle-creek-5538": "5538", 
    "west-lake-marion-park": "20367", 
    "lebanon-hills": "3438",
    "murphyhanrehan-park": "7646",
    "theodore-wirth-park": "9224",
    "xcel-energy-mountain-bike-park-50624": "50624"
}

tf_region = TrailforksRegion(username=USERNAME, password=PASSWORD)
tf_region.login()

trails_files_dfs = []
trail_ridecounts_dfs = []
trail_ridelogs_dfs = []

pbar = tqdm(total=len(region_to_id_map))
for region, region_id in region_to_id_map.items():
    trails_files_dfs.append(tf_region.download_all_region_trails(region, region_id))
    trail_ridelogs_dfs.append(tf_region.download_all_region_ridelogs(region))
    trail_ridecounts_dfs.append(tf_region.download_region_ridecounts(region))
    pbar.update(1)
pbar.close()

pd.concat(trails_files_dfs).to_csv("data/region_trails.csv", index=False)
pd.concat(trail_ridecounts_dfs).to_csv("data/region_ridecounts.csv")
pd.concat(trail_ridelogs_dfs).to_csv("data/region_ridelogs.csv")
