import sys
import json
import pprint
import pandas as pd
import asyncio
from pulsefire.clients import RiotAPIClient
from pulsefire.schemas import RiotAPISchema
from pulsefire.taskgroups import TaskGroup
from config import api_key

def kda(player):
    t = "\t"
    c = ","
    print(player["riotIdGameName"],c,player["kills"],c,player["deaths"],c,player["assists"])

def playerStats(player):
    input_match = sys.argv[1]
    t = "\t"
    c = ","
    #  print(player["riotIdGameName"], 
           #  player["individualPosition"],c,player["playerSubteamId"],c, 
          #  player["championName"], player["timePlayed"], player["totalTimeSpentDead"] 
          #  )
    print(input_match,c,player["riotIdGameName"],c,player["individualPosition"],c,player["timePlayed"],c,player["teamId"],c,player["gameEndedInEarlySurrender"],c,player["gameEndedInSurrender"],c,player["teamEarlySurrendered"],c,player["win"],c,player["kills"],c,player["deaths"],c,player["assists"],c,player["longestTimeSpentLiving"],c,player["totalTimeSpentDead"],c,player["damageSelfMitigated"],c,player["magicDamageDealt"],c,player["magicDamageDealtToChampions"],c,player["magicDamageTaken"],c,player["totalDamageDealt"],c,player["totalDamageDealtToChampions"],c,player["totalDamageShieldedOnTeammates"],c,player["totalDamageTaken"],c,player["totalUnitsHealed"],c,player["trueDamageDealt"],c,player["trueDamageDealtToChampions"],c,player["trueDamageTaken"],c,player["totalHeal"],c,player["totalHealsOnTeammates"],c,player["physicalDamageDealt"],c,player["physicalDamageDealtToChampions"],c,player["physicalDamageTaken"],c,player["baronKills"],c,player["dragonKills"],c,player["objectivesStolen"],c,player["objectivesStolenAssists"],c,player["neutralMinionsKilled"],c,player["damageDealtToObjectives"],c,player["nexusKills"],c,player["nexusLost"],c,player["nexusTakedowns"],c,player["damageDealtToBuildings"],c,player["inhibitorKills"],c,player["inhibitorTakedowns"],c,player["inhibitorsLost"],c,player["turretKills"],c,player["turretTakedowns"],c,player["turretsLost"],c,player["damageDealtToTurrets"],c,player["visionScore"],c,player["visionWardsBoughtInGame"],c,player["wardsKilled"],c,player["wardsPlaced"],c,player["win"],c,player["detectorWardsPlaced"],c,player["sightWardsBoughtInGame"],c,player["goldEarned"],c,player["goldSpent"],c,player["totalMinionsKilled"],c,player["totalAllyJungleMinionsKilled"],c,player["totalEnemyJungleMinionsKilled"],c,player["bountyLevel"],c,player["champExperience"],c,player["champLevel"],c,player["championTransform"],c,player["firstBloodAssist"],c,player["firstBloodKill"],c,player["firstTowerAssist"],c,player["firstTowerKill"],c,player["timeCCingOthers"],c,player["totalTimeCCDealt"],c,player["allInPings"],c,player["assistMePings"],c,player["basicPings"],c,player["commandPings"],c,player["dangerPings"],c,player["enemyMissingPings"],c,player["enemyVisionPings"],c,player["getBackPings"],c,player["holdPings"],c,player["needVisionPings"],c,player["onMyWayPings"],c,player["pushPings"],c,player["retreatPings"],c,player["visionClearedPings"],c,player["largestCriticalStrike"],c,player["pentaKills"],c,player["spell1Casts"],c,player["spell2Casts"],c,player["spell3Casts"],c,player["spell4Casts"])


async def main():
    async with RiotAPIClient(default_headers={"X-Riot-Token": api_key}) as client:
        input_match = sys.argv[1]
        #  match_data = await client.get_lol_match_v5_match(region = "americas", id = "NA1_5239217022")
        match_data = await client.get_lol_match_v5_match(region = "americas", id = input_match)
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
        #  print("\tName\tK\tD\tA")
        for value in red.values():
            playerStats(value)
            #  kda(value)
asyncio.run(main())
