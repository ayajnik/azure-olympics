import logging
import sys
import azure.functions as func
import datetime
from datetime import datetime

sys.path.append('..')

#from HttpTrigger1_tokyoOlympics.operations import io
from HttpTrigger1_tokyoOlympics.operations import io
#from app import final_frame
import pandas as pd
from functools import reduce

today = datetime.today()
today_str = today.strftime('%Y-%m-%d')

df_athletes,df_medal, df_coaches, df_teams,df_ent_gender = io.getFile()

df_medal.rename(columns={'Team_Country': 'Country'}, inplace=True)

# List of dataframes to join
dfs = [df_athletes, df_medal, df_coaches, df_teams]

result = reduce(lambda left,right: pd.merge(left,right,on='Country',how='inner'), dfs)
final_frame = result.drop_duplicates()
