import json
import asyncio
from pulsefire.clients import RiotAPIClient
from pulsefire.schemas import RiotAPISchema
from pulsefire.taskgroups import TaskGroup
from config import api_key

async def main():
    async with RiotAPIClient(default_headers={"X-Riot-Token": api_key}) as client:
        match_data = await client.get_lol_match_v5_match_timeline(region = "americas", id = "NA1_5234777914")

        json_object = json.dumps(match_data, indent = 4)
        print(json_object)

asyncio.run(main())
