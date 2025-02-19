import asyncio
from pulsefire.clients import RiotAPIClient
from pulsefire.schemas import RiotAPISchema
from pulsefire.taskgroups import TaskGroup
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
        match_ids = await client.get_lol_match_v5_match_ids_by_puuid(region="americas", puuid=summoner["puuid"])
        #assert summoner["summonerLevel"] > 200

        async with TaskGroup() as tg:
            for match_id in match_ids[:20]:
                await tg.create_task(client.get_lol_match_v5_match(region="americas", id=match_id))

        matches: list[RiotApiSchema.LolMatchV5Match] = tg.results()

        for match in matches:
            assert match["metadata"]["matchId"] in match_ids


        print(match_ids)


asyncio.run(main())
