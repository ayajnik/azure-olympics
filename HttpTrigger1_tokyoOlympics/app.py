import sys
import os

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
    final_frame.to_csv(os.getcwd()+'/processedOlympicsData_'+today_str+'.csv')
    final_extract = io.dumpFile('processedOlympicsData_'+today_str+'.csv')
    return final_extract

if __name__ == "__main__":
    print("\n")
    print("**************************************************************")
    print("\n")
    print("Welcome to NeuralWave operations for Azure excellance")
    print("\n")
    print("**************************************************************")
    

    rows = 9    
    # Here, we are declaring an outer for loop to handle number of rows   
    for i in range(0, rows):    
        # Here, we are declaring an inner for loop to print the stars   
        for j in range(0, i + 1):    
            print("*", end=' ')    
        # Here, we are changing the line after each iteration    
        print(" ")    
    # Here, we are creating the code for the second pattern    
    for i in range(rows + 1, 0, -1):    
        for j in range(0, i - 1):     
            print("*", end=' ')    
        print(" ")   
    main_execution = main()
    main_execution

