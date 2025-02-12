import asyncio
from pulsefire.clients import RiotAPIClient
from config import api_key
#print("API Key: ")
#api_key = input()
#print(api_key)


async def main():
    print("main?")
    async with RiotAPIClient(default_headers={"X-Riot-Token": api_key}) as client:
        print("asyncing?")
        account = await client.get_account_v1_by_riot_id(region="americas", game_name="ObKnoxious", tag_line="3824")
        print(account)
        summoner = await client.get_lol_summoner_v4_by_puuid(region="na1", puuid=account["puuid"])
        assert summoner["summonerLevel"] > 200


asyncio.run(main())
