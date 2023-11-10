import sys

sys.path.append('..')

from operations import io
import pandas as pd
from functools import reduce
import datetime
from datetime import datetime

df_athletes,df_medal, df_coaches, df_teams,df_ent_gender = io.getFile()

df_medal.rename(columns={'Team_Country': 'Country'}, inplace=True)

# List of dataframes to join
dfs = [df_athletes, df_medal, df_coaches, df_teams]

result = reduce(lambda left,right: pd.merge(left,right,on='Country',how='inner'), dfs)
final_frame = result.drop_duplicates()
