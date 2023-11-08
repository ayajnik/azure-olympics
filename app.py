import sys

sys.path.append('..')

from operations import io

df_athletes = io.getFile()

print(df_athletes.head())

io.dumpFile(df_athletes,'Athletes.csv')


####################################### Uploading a file to blob #############################################

import pandas as pd
from azure.storage.blob import BlobServiceClient, generate_blob_sas, BlobSasPermissions
import pandas as pd


# Create a pandas dataframe
df = pd.DataFrame({'name': ['John', 'Mary'], 'age': [25, 30]})

# Convert the pandas dataframe to a csv file
csv_file = df.to_csv('my_dataframe.csv', index=False,encoding='utf-8')
connection__string = ''
# Upload the csv file to the azure container
#blob_service = BlobServiceClient(account_url=string)
blob_service_client = BlobServiceClient.from_connection_string(connection__string)
print('establishing the connection in the next line')
blob_container = blob_service_client.get_container_client('containerrawdata')  ## this is the name of the container
print("Connection established")

import os

with open(file=os.path.join(os.getcwd()+'/my_dataframe.csv'), mode="rb") as data:
    blob_client = blob_container.upload_blob(name="processedData/test.csv", data=data, overwrite=True)


###################################################################################################################

