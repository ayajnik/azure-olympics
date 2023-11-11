import sys

sys.path.append('..')

from HttpTrigger1_tokyoOlympics.operations import io
#from .operations import io
import pandas as pd
from functools import reduce
import datetime
from datetime import datetime


def main():

    today = datetime.today()
    today_str = today.strftime('%Y-%m-%d')

    df_athletes,df_medal, df_coaches, df_teams,df_ent_gender = io.getFile()

    df_medal.rename(columns={'Team_Country': 'Country'}, inplace=True)

    # List of dataframes to join
    dfs = [df_athletes, df_medal, df_coaches, df_teams]

    result = reduce(lambda left,right: pd.merge(left,right,on='Country',how='inner'), dfs)
    final_frame = result.drop_duplicates()
    final_frame.to_csv('/tmp/processedOlympicsData_'+today_str+'.csv')
    final_extract = io.dumpFile('processedOlympicsData_'+today_str+'.csv')
    return final_extract