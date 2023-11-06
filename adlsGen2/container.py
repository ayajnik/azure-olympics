try:
    import os
    from azure.storage.filedatalake import (
        DataLakeServiceClient,
        DataLakeDirectoryClient,
        FileSystemClient
    )
    from azure.identity import DefaultAzureCredential
    print("Azure Gen2 libraries imported!")
except ImportError as e:
    print(e)


class containerSDK:
    def __init__(self,account_name):
        self.account_name = account_name

    def get_service_client_token_credential(self) -> DataLakeServiceClient:
        try:
            account_url = f"https://{self.account_name}.dfs.core.windows.net"
            token_credential = DefaultAzureCredential()

            service_client = DataLakeServiceClient(account_url, credential=token_credential)

            return service_client
        except InterruptedError as i:
            print(i)
            print('\n')
            print('FS not created')

# tokyocontainerolympics

    ## create a container
    def create_file_system(self, service_client: DataLakeServiceClient, file_system_name: str) -> FileSystemClient:
        try:
            fs = self.get_service_client_token_credential()
            file_system_client = fs.create_file_system(file_system=file_system_name)

            return file_system_client
        except:
            print("There is some error!")
            
    def create_directory(self, file_system_client: FileSystemClient, directory_name: str) -> DataLakeDirectoryClient:
        directory_client = file_system_client.create_directory(directory_name)

        return directory_client