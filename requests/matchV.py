import requests
import pandas as pd
import time
from warnings import simplefilter
simplefilter(action="ignore", category=pd.errors.PerformanceWarning)
import config.py
import ids.py

api_url = 'https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/' + knox + '/ids?queue=420&type=ranked&start=0&count=20' + '&api_key=' + api_key
