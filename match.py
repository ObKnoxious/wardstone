import sys
import json
import pprint
import pandas as pd
import asyncio
from datetime import datetime
from pulsefire.clients import RiotAPIClient
from pulsefire.schemas import RiotAPISchema
from pulsefire.taskgroups import TaskGroup
from config import api_key

def teamStats(team):
    totals = {"damage" : 0, "kills" : 0, "deaths" : 0, "vision" : 0, "wards" : 0}
    totals["damage"] = team["p4"]["totalDamageDealtToChampions"] + team["p3"]["totalDamageDealtToChampions"] + team["p2"]["totalDamageDealtToChampions"] + team["p1"]["totalDamageDealtToChampions"] + team["p0"]["totalDamageDealtToChampions"]
    totals["kills"] = team["p4"]["kills"] + team["p3"]["kills"] + team["p2"]["kills"] + team["p1"]["kills"] + team["p0"]["kills"]
    totals["deaths"] = team["p4"]["deaths"] + team["p3"]["deaths"] + team["p2"]["deaths"] + team["p1"]["deaths"] + team["p0"]["deaths"]
    totals["vision"] = team["p4"]["visionScore"] + team["p3"]["visionScore"] + team["p2"]["visionScore"] + team["p1"]["visionScore"] + team["p0"]["visionScore"]
    totals["wards"] = team["p4"]["detectorWardsPlaced"] + team["p3"]["detectorWardsPlaced"] + team["p2"]["detectorWardsPlaced"] + team["p1"]["detectorWardsPlaced"] + team["p0"]["detectorWardsPlaced"]
    return totals;


def playerStats(player, timestamp, totals):
    input_match = sys.argv[1]
    matchStart = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
    minutes= player["timePlayed"]/60
    t = "\t"
    c = ","
    print(input_match,c,timestamp,c,player["riotIdGameName"],c,player["individualPosition"],c,player["championName"],c,player["timePlayed"],c,player["teamId"],c,player["gameEndedInEarlySurrender"],c,player["gameEndedInSurrender"],c,player["teamEarlySurrendered"],c,player["win"],c,player["kills"],c,player["deaths"],c,player["assists"],c,player["longestTimeSpentLiving"],c,player["totalTimeSpentDead"],c,player["damageSelfMitigated"],c,player["magicDamageDealt"],c,player["magicDamageDealtToChampions"],c,player["magicDamageTaken"],c,player["totalDamageDealt"],c,player["totalDamageDealtToChampions"],c,player["totalDamageShieldedOnTeammates"],c,player["totalDamageTaken"],c,player["totalUnitsHealed"],c,player["trueDamageDealt"],c,player["trueDamageDealtToChampions"],c,player["trueDamageTaken"],c,player["totalHeal"],c,player["totalHealsOnTeammates"],c,player["physicalDamageDealt"],c,player["physicalDamageDealtToChampions"],c,player["physicalDamageTaken"],c,player["baronKills"],c,player["dragonKills"],c,player["objectivesStolen"],c,player["objectivesStolenAssists"],c,player["neutralMinionsKilled"],c,player["damageDealtToObjectives"],c,player["nexusKills"],c,player["nexusLost"],c,player["nexusTakedowns"],c,player["damageDealtToBuildings"],c,player["inhibitorKills"],c,player["inhibitorTakedowns"],c,player["inhibitorsLost"],c,player["turretKills"],c,player["turretTakedowns"],c,player["turretsLost"],c,player["damageDealtToTurrets"],c,player["visionScore"],c,player["visionWardsBoughtInGame"],c,player["wardsKilled"],c,player["wardsPlaced"],c,player["win"],c,player["detectorWardsPlaced"],c,player["sightWardsBoughtInGame"],c,player["goldEarned"],c,player["goldSpent"],c,player["totalMinionsKilled"],c,player["totalAllyJungleMinionsKilled"],c,player["totalEnemyJungleMinionsKilled"],c,player["bountyLevel"],c,player["champExperience"],c,player["champLevel"],c,player["championTransform"],c,player["firstBloodAssist"],c,player["firstBloodKill"],c,player["firstTowerAssist"],c,player["firstTowerKill"],c,player["timeCCingOthers"],c,player["totalTimeCCDealt"],c,player["allInPings"],c,player["assistMePings"],c,player["basicPings"],c,player["commandPings"],c,player["dangerPings"],c,player["enemyMissingPings"],c,player["enemyVisionPings"],c,player["getBackPings"],c,player["holdPings"],c,player["needVisionPings"],c,player["onMyWayPings"],c,player["pushPings"],c,player["retreatPings"],c,player["visionClearedPings"],c,player["largestCriticalStrike"],c,player["pentaKills"],c,player["spell1Casts"],c,player["spell2Casts"],c,player["spell3Casts"],c,player["spell4Casts"],c,matchStart,c,minutes,c,totals["damage"],c,totals["kills"],c,totals["deaths"],c,totals["vision"],c,totals["wards"])


async def main():
    async with RiotAPIClient(default_headers={"X-Riot-Token": api_key}) as client:
        input_match = sys.argv[1]
        #  match_data = await client.get_lol_match_v5_match(region = "americas", id = "NA1_5239217022")
        match_data = await client.get_lol_match_v5_match(region = "americas", id = input_match)

        match_metadata = match_data["metadata"]
        #currently unused metadata
        match_info = match_data["info"]
        #main match data storage
        timestamp = (match_info["gameCreation"])
        timestamp = timestamp//1000
        #timestamp needs to be in seconds not ms, floor division so stays int

        match_parts = match_info["participants"]
        #participants is a list 0f 10 dictionaries with 145 starts per player

        blue = {"p0": match_parts[0], "p1": match_parts[1], "p2": match_parts[2],
                "p3": match_parts[3], "p4": match_parts[4]}
        #  blueL = [match_parts[0], match_parts[1], match_parts[2], match_parts[3], match_parts[4]]
        #in testing blue team is always the first 5 values, assign to dictionary

        red = {"p0": match_parts[5], "p1": match_parts[6], "p2": match_parts[7],
                "p3": match_parts[8], "p4": match_parts[9]}
        team = "red"
        for player in red.values():
            squad = ["FluffyWhale", "ObKnoxious", "pyro", "D1stract1n", "Star Grompian", "HugeTortoise151"]
            if(player["riotIdGameName"] in squad):
                pass
            else:
                team="blue"

        if(team=="blue"):
            for player in blue.values():
                squad = ["FluffyWhale", "ObKnoxious", "pyro", "D1stract1n", "Star Grompian", "HugeTortoise151"]
                if player["riotIdGameName"] in squad:
                    pass
                else:
                    team="none"

        if(team=="red"):
            totals = teamStats(red)
            for player in red.values():
                playerStats(player, timestamp, totals)
        elif(team=="blue"):
            totals = teamStats(blue)
            for player in blue.values():
                playerStats(player, timestamp, totals)
        else:
            print("Team is not a complete 5 from squad")

asyncio.run(main())

