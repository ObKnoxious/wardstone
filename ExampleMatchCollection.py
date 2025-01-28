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








