# (c) Copyright Ascensio System SIA 2009-2025
# 
# This program is a free software product.
# You can redistribute it and/or modify it under the terms
# of the GNU Affero General Public License (AGPL) version 3 as published by the Free Software
# Foundation. In accordance with Section 7(a) of the GNU AGPL its Section 15 shall be amended
# to the effect that Ascensio System SIA expressly excludes the warranty of non-infringement of
# any third-party rights.
# 
# This program is distributed WITHOUT ANY WARRANTY, without even the implied warranty
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR  PURPOSE. For details, see
# the GNU AGPL at: http://www.gnu.org/licenses/agpl-3.0.html
# 
# You can contact Ascensio System SIA at Lubanas st. 125a-25, Riga, Latvia, EU, LV-1021.
# 
# The  interactive user interfaces in modified source and object code versions of the Program must
# display Appropriate Legal Notices, as required under Section 5 of the GNU AGPL version 3.
# 
# Pursuant to Section 7(b) of the License you must retain the original Product logo when
# distributing the program. Pursuant to Section 7(e) we decline to grant you any rights under
# trademark law for use of our trademarks.
# 
# All the Product's GUI elements, including illustrations and icon sets, as well as technical writing
# content are licensed under the terms of the Creative Commons Attribution-ShareAlike 4.0
# International. See the License terms at http://creativecommons.org/licenses/by-sa/4.0/legalcode



from docspace import Configuration, ApiClient, AuthenticationApi, FilesFoldersApi, BackupApi
from docspace.models.auth_requests_dto import AuthRequestsDto
from docspace.models.create_folder import CreateFolder
from docspace.models.delete_folder import DeleteFolder
from docspace.models.backup_dto import BackupDto
from docspace.models.backup_storage_type import BackupStorageType
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