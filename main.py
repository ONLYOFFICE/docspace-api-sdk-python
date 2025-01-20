import asyncio
from kiota_abstractions.authentication.anonymous_authentication_provider import (
    AnonymousAuthenticationProvider)
from kiota_http.httpx_request_adapter import HttpxRequestAdapter
from posts_client import PostsClient
from models.a_s_c.web.api.api_model.requests_dto.auth_requests_dto import AuthRequestsDto
from models.a_s_c.files.core.api_models.request_dto.create_folder import CreateFolder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from kiota_abstractions.headers_collection import HeadersCollection
from models.a_s_c.files.core.api_models.request_dto.delete_folder import DeleteFolder

async def main():
    auth_provider = AnonymousAuthenticationProvider()
    request_adapter = HttpxRequestAdapter(auth_provider)
    client = PostsClient(request_adapter)
    auth_request = AuthRequestsDto()
    auth_request.user_name = "test@onlyoffice.com"
    auth_request.password = "12345678"
    auth = await client.authentication.post(body=auth_request)
    if auth:
        print("success")
        print(f"Token: {auth.response.token}")
    else:
        print("fail")
    
    headers = HeadersCollection()
    auth_token = auth.response.token
    headers.add("Authorization", auth_token)
    request_configuration = RequestConfiguration(headers=headers)
    folderMy = await client.folderMy.get(request_configuration=request_configuration)
    if folderMy:
        print("success")
        print(f"FolderId: {folderMy.response.current.id}")
    else:
        print("fail")
    
    folderMyID = folderMy.response.current.id
    folderData = CreateFolder()
    folderData.title = "TestTitle"

    createFolder = await client.createFolerInFolderMy.by_folder_id(folderMyID).post(body=folderData, request_configuration=request_configuration)
    if createFolder:
        print("success")
        print(f"FolderId: {createFolder.response.id}")
    
    createdFolderId = createFolder.response.id

    getFolder = await client.createFolerInFolderMy.by_folder_id(createdFolderId).get(request_configuration=request_configuration)
    if getFolder:
        print("success")
    
    newFolderData = CreateFolder()
    newFolderData.title = "NewTitle"

    putFolder = await client.createFolerInFolderMy.by_folder_id(createdFolderId).put(body=newFolderData, request_configuration=request_configuration)
    if putFolder:
        print(f"{putFolder.response.title}")
    
    deleteFolderData = DeleteFolder()
    deleteFolderData.immediately = True
    deleteFolderData.delete_after = True

    deleteFolder = await client.createFolerInFolderMy.by_folder_id(createdFolderId).delete(body=deleteFolderData, request_configuration=request_configuration)
    if deleteFolder:
        print("success")

if __name__ == "__main__":
    asyncio.run(main())