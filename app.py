import os
# from azure.storage.filedatalake import (
#     DataLakeServiceClient,
#     DataLakeDirectoryClient,
#     FileSystemClient
# )
from azure.identity import DefaultAzureCredential
import azure.storage.blob.blockblobservice
import datetime
from datetime import datetime
import pandas as pd
from datetime import datetime, timedelta
#from azure.storage.blob import BlobServiceClient, generate_blob_sas, BlobSasPermissions
import pandas as pd
from azure.storage.blob import BlobServiceClient

# account_name = 'tokyoolympicsanalysis'
# account_key = 'Q/2Up2Id9usdnnic3RaiUQw/p98nR+DTqoDXKaa6JD950Ba4UNWGb30+iNVPczhsULhSa9kUTkx6+AStKmiPCw=='
# container_name = 'containerrawdata'

# #create a client to interact with blob storage
# connect_str = 'DefaultEndpointsProtocol=https;AccountName=' + account_name + ';AccountKey=' + account_key + ';EndpointSuffix=core.windows.net'
# blob_service_client = BlobServiceClient.from_connection_string(connect_str)

# #use the client to connect to the container
# container_client = blob_service_client.get_container_client(container_name)

# #get a list of all blob files in the container
# blob_list = []
# for blob_i in container_client.list_blobs():
#     blob_list.append(blob_i.name)
    


# df_list = []
# #generate a shared access signiture for files and load them into Python
# for blob_i in blob_list:
#     #generate a shared access signature for each blob file
#     sas_i = generate_blob_sas(account_name = account_name,
#                                 container_name = container_name,
#                                 blob_name = blob_i,
#                                 account_key=account_key,
#                                 permission=BlobSasPermissions(read=True),
#                                 expiry=datetime.utcnow() + timedelta(hours=1))
    
#     sas_url = 'https://' + account_name+'.blob.core.windows.net/' + container_name + '/' + blob_i + '?' + sas_i
    
# df = pd.read_csv(sas_url)
