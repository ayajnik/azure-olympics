import logging
import sys
import azure.functions as func
import datetime
from datetime import datetime

sys.path.append('..')

#from HttpTrigger1_tokyoOlympics.operations import io
from .operations import io
import pandas as pd
from functools import reduce


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    today = datetime.today()
    today_str = today.strftime('%Y-%m-%d')

    df_athletes,df_medal, df_coaches, df_teams,df_ent_gender = io.getFile()

    df_medal.rename(columns={'Team_Country': 'Country'}, inplace=True)

    # List of dataframes to join
    dfs = [df_athletes, df_medal, df_coaches, df_teams]

    result = reduce(lambda left,right: pd.merge(left,right,on='Country',how='inner'), dfs)
    final_frame = result.drop_duplicates()

    
    final_frame.to_csv('/tmp/processedOlympicsData_'+today_str+'.csv')

    


    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             io.dumpFile('processedOlympicsData_'+today_str+'.csv'),
             status_code=200
        )
