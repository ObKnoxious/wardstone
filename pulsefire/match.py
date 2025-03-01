import json
import pprint
import pandas as pd
import asyncio
from pulsefire.clients import RiotAPIClient
from pulsefire.schemas import RiotAPISchema
from pulsefire.taskgroups import TaskGroup
from config import api_key

def playerStats(player):
    print(player["riotIdGameName"], player["teamId"], 
           player["individualPosition"], player["playerSubteamId"], player["profileIcon"], 
          player["championName"], player["timePlayed"], player["totalTimeSpentDead"] 
          )


async def main():
    async with RiotAPIClient(default_headers={"X-Riot-Token": api_key}) as client:
        match_data = await client.get_lol_match_v5_match(region = "americas", id = "NA1_5239217022")
        #currently unused metadata
        match_metadata = match_data["metadata"]
        #main match data storage
        match_info = match_data["info"]
        #participants is a list 0f 10 dictionaries with 145 starts per player
        match_parts = match_info["participants"]
        #in testing blue team is always the first 5 values, assign to dictionary 
        blue = {"b0": match_parts[0], "b1": match_parts[1], "b2": match_parts[2], 
                   "b3": match_parts[3], "b4": match_parts[4]}
        
        red = {"r0": match_parts[5], "r1": match_parts[6], "r2": match_parts[7], 
                   "r3": match_parts[8], "r4": match_parts[9]}
        for value in red.values():
            playerStats(value)
asyncio.run(main())
