import json
import pprint
import pandas as pd
import asyncio
from pulsefire.clients import RiotAPIClient
from pulsefire.schemas import RiotAPISchema
from pulsefire.taskgroups import TaskGroup
from config import api_key

async def main():
    async with RiotAPIClient(default_headers={"X-Riot-Token": api_key}) as client:
        match_data = await client.get_lol_match_v5_match(region = "americas", id = "NA1_5234777914")
        #  pprint.pp(match_data)
        match_metadata = match_data["metadata"]
        match_info = match_data["info"]
        match_parts = match_info["participants"]
        print(len(match_info))
        print(match_info.keys())
        print(type(match_parts))
        print(len(match_parts))
        print(type(match_parts[0]))
        print(len(match_parts[0]))
        print(match_parts[0].keys())
        #  df = pd.DataFrame.from_dict(match_data, orient="index")
        #  print(df.loc[0])
        #  df.to_csv("data_out.csv")
        #  json_object = json.dumps(match_data, indent = 4)
        #  print(json_object)

asyncio.run(main())
