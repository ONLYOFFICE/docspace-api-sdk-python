#
# (c) Copyright Ascensio System SIA 2025
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#



from docspace-api-sdk import Configuration, ApiClient, AuthenticationApi, FilesFoldersApi, BackupApi
from docspace-api-sdk.models.auth_requests_dto import AuthRequestsDto
from docspace-api-sdk.models.create_folder import CreateFolder
from docspace-api-sdk.models.delete_folder import DeleteFolder
from docspace-api-sdk.models.backup_dto import BackupDto
from docspace-api-sdk.models.backup_storage_type import BackupStorageType
import time

def main():
    config = Configuration()
    with ApiClient(config) as api_client:
        auth_instance = AuthenticationApi(api_client)
        
        auth_request_data = AuthRequestsDto()
        auth_request_data.password = ""
        auth_request_data.user_name = ""
        
        try:
            auth_response = auth_instance.authenticate_me(auth_request_data)
            token = auth_response.response.token
            custom_headers = {"Authorization": f"Bearer {token}"}
            folder_instance = FilesFoldersApi(api_client)
            responseFolderMy = folder_instance.get_my_folder(_headers=custom_headers)
            print(responseFolderMy.response.current.id)

            folderMyId = responseFolderMy.response.current.id
            folderData = CreateFolder()
            folderData.title = "TestTitle"
            createFolder = folder_instance.create_folder(folder_id=folderMyId, create_folder=folderData, _headers=custom_headers)
            print(createFolder.response.id)

            newFolderId = createFolder.response.id
            getFolder = folder_instance.get_folder_by_folder_id(folder_id=newFolderId, _headers=custom_headers)
            print(getFolder.status_code)

            newFolderData = CreateFolder()
            newFolderData.title = "Updated title"
            updateFolder = folder_instance.rename_folder(folder_id=newFolderId, create_folder=newFolderData, _headers=custom_headers)
            print(updateFolder.status_code)

            deleteFolderData = DeleteFolder()
            deleteFolderData.delete_after = False
            deleteFolderData.immediately = True
            deleteFolder = folder_instance.delete_folder(folder_id=newFolderId, delete_folder=deleteFolderData, _headers=custom_headers)
            print(deleteFolder.status_code)

            backup_instanse = BackupApi(api_client)
            backup_data = BackupDto()
            backup_data.dump = False
            backup_data.storage_type = BackupStorageType.NUMBER_4
            createBackup = backup_instanse.start_backup(backup_dto=backup_data, _headers=custom_headers)
            if createBackup.status_code == 200:
                print("Backup started")
            
            backupProgress = backup_instanse.get_backup_progress(_headers=custom_headers)
            print(backupProgress.response.is_completed)
            while True:
                progress = backup_instanse.get_backup_progress(_headers=custom_headers)
                if progress.response.is_completed:
                    print("Backup completed")
                    break
                time.sleep(1.0)

        except Exception as e:
            print("Exception when calling API:", e)

if __name__ == "__main__":
    main()