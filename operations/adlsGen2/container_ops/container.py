import os
import datetime
from datetime import datetime
import pandas as pd
from datetime import datetime, timedelta
from azure.storage.blob import BlobServiceClient, generate_blob_sas, BlobSasPermissions
import pandas as pd




class readFile:
    def __init__(self,account_name,account_key,container_name):
        self.account_name = account_name
        self.account_key = account_key
        self.container_name = container_name
        

    def _connection_string(self):
        #create a client to interact with blob storage
        connect_str = 'DefaultEndpointsProtocol=https;AccountName=' + self.account_name + ';AccountKey=' + self.account_key + ';EndpointSuffix=core.windows.net'
        return connect_str

    def blobClient(self):
        connecti_strng = self._connection_string()
        blob_service_client = BlobServiceClient.from_connection_string(connecti_strng)
        return blob_service_client

    def blobConnection(self):
        # #use the client to connect to the container
        blobbyClient = self.blobClient()
        container_client = blobbyClient.get_container_client(self.container_name)
        return container_client

    def getFile(self):
        containy_client = self.blobConnection()
        blob_list = []
        for blob_i in containy_client.list_blobs():
            blob_list.append(blob_i.name)
        print(blob_list)
            
        df_list = []
        #generate a shared access signiture for files and load them into Python
        for blob_i in blob_list:
            #generate a shared access signature for each blob file
            sas_i = generate_blob_sas(account_name = self.account_name,
                                        container_name = self.container_name,
                                        blob_name = blob_i,
                                        account_key=self.account_key,
                                        permission=BlobSasPermissions(read=True),
                                        expiry=datetime.utcnow() + timedelta(hours=1))
            
            
            sas_url = 'https://' + self.account_name+'.blob.core.windows.net/' + self.container_name + '/' + blob_i + '?' + sas_i
        
            if sas_url.__contains__('Athletes.csv'):
                print("*****")
                print(sas_url)
                df = pd.read_csv(sas_url,delimiter=',',encoding='latin-1')
                return df
            else:
                return "No files found"


    def dumpFile(self,filename):


        '''
        Export the dataframe as a csv and then dump it in processedData directory.


        '''

        connection__string = 'DefaultEndpointsProtocol=https;AccountName=' + self.account_name + ';AccountKey=' + self.account_key + ';EndpointSuffix=core.windows.net'
        blob_service_client = BlobServiceClient.from_connection_string(connection__string)
        blob_container = blob_service_client.get_container_client(self.container_name)  ## this is the name of the container

        with open(file=os.path.join(os.getcwd()+'/my_dataframe.csv'), mode="rb") as data:
            blob_client = blob_container.upload_blob(name="processedData/"+filename, data=data, overwrite=True)

        
        try:
            os.remove(os.path.join(os.getcwd()+filename))
            print(f"'{os.getcwd()+filename}' removed successfully.")
        except OSError as e:
            print(f"Error deleting '{os.getcwd()+filename}': {e}")