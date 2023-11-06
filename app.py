import os
from azure.storage.filedatalake import (
    DataLakeServiceClient,
    DataLakeDirectoryClient,
    FileSystemClient
)
from azure.identity import DefaultAzureCredential
import datetime
from datetime import datetime
import pandas as pd

## resource group: tokyo-olympic-analysis

## storage account: tokyoolympicsayush

## Step 1:

# To work with the code examples, we need to create an authorized DataLakeServiceClient instance that represents the storage account. 
# We can authorize a DataLakeServiceClient object using Microsoft Entra ID, an account access key, or a shared access signature (SAS).
 
## access key: qBCN/PQ1cTuD/sgVyNVosaFt+RavmhnVY4kYw/MUNmXlWOluXwlBJJ8cEkLIcmNZ9YkADtMSXULJ+AStZuuJHw==
## account name: tokyoolympicsayush
account_url = "https://tokyoolympicsayush.dfs.core.windows.net"
service_client = DataLakeServiceClient(account_url, credential='qBCN/PQ1cTuD/sgVyNVosaFt+RavmhnVY4kYw/MUNmXlWOluXwlBJJ8cEkLIcmNZ9YkADtMSXULJ+AStZuuJHw==')

# Step 2: Create a container

# A container acts as a file system for your files. You can create a container by using the following method:

# make sure that the name of the container can only contain the following characters
# 1. lower case alphabets
# 2. numbers
# 3. hyphens

#file_system_client = service_client.create_file_system('tokyorawdata1')

# create a directory



# reading a csv file from pandas which is in a container

df = 






