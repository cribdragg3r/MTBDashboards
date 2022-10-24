from PyForks.trailforks_region import TrailforksRegion
from PyForks.trailforks_user import TrailforksUser
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

pbar = tqdm(total=len(region_to_id_map))
for region, region_id in region_to_id_map.items():
    tf_region.download_all_region_trails(region, region_id, "./data")
    tf_region.download_all_region_ridelogs(region, "./data")
    tf_region.download_region_ridecounts(region, output_path="./data")
    pbar.update(1)
pbar.close()