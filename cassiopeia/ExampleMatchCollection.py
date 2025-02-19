# most of this is taken from github cassiopeia example 
# https://github.com/meraki-analytics/cassiopeia/blob/master/examples/match_collection.py

import random
from sortedcontainers import SortedList
import arrow

from cassiopeia.core import Account, Summoner, MatchHistory, Match
from cassiopeia import Queue, Patch 

def filter_match_history(summoner: Summoner, patch: Patch):
    end_time = patch.end
    if end_time is None: 
        end_time is arrow.now()
    match_history = MatchHistory(
        puuid=summoner.puuid,
        continent=summoner.continent,
        queue=Queue.ranked_solo_fives,
        start_time=patch.start,
        end_time=end_time,
    )
    return match_history


def collect_matches():
    initial_summoner_name, initial_summoner_tagline = "ObKnoxious", "3824"
    region = "NA"

    account = Account(
            name=inital_summoner_name, tagline=initial_summoner_tagline, region=region
            )
    summoner = account.summoner
    patch = Patch.from_str("15.2.1", region=region)

    unpulled_summoner_ids = SortedList([summoner.id])
    pulled_summoner_ids = SortedList()

    unpulled_match_ids = SortedList()
    pulled_match_ids = SortedList()

    while unpulled_summoner_ids:
        new_summoner_id = random.choice(unpulled_summoner_ids)
        new_summoner = Summoner(id=new_summoner_id, region=region)
        matches = filter_match_history(new_summoner, patch)
        unpulled_match_ids.update([match.id for match in matches])
        unpulled_summoner_ids.remove(new_summoner_id)
        pulled_summoner_ids.add(new_summoner_id)

        while unpulled_match_ids:
            new_match_id = random.choice(unpulled_match_ids)
            new_match = Match(id=new_match_id, region=region)
            for participant in new_match.participants:
                if (
                    participant.summoner.id not in pulled_summoner_ids
                    and participant.summoner.id not in unpulled_summoner_ids
                ):
                    unpulled_summoner_ids.add(participant.summoner.id)
            unpulled_match_ids.remove(new_match_id)
            pulled_match_ids.add(new_match_id)


if __name__ == "__main__":
    collect_matches()







