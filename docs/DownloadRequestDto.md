# DownloadRequestDto

The request parameters for downloading files.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**folder_ids** | [**List[BaseBatchRequestDtoFolderIdsInner]**](BaseBatchRequestDtoFolderIdsInner.md) | The list of folder IDs to be downloaded. | [optional] 
**file_ids** | [**List[BaseBatchRequestDtoFolderIdsInner]**](BaseBatchRequestDtoFolderIdsInner.md) | The list of file IDs to be downloaded. | [optional] 
**file_convert_ids** | [**List[DownloadRequestItemDto]**](DownloadRequestItemDto.md) | The list of file IDs which will be converted. | [optional] 

## Example

```python
from docspace.models.download_request_dto import DownloadRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of DownloadRequestDto from a JSON string
download_request_dto_instance = DownloadRequestDto.from_json(json)
# print the JSON string representation of the object
print(DownloadRequestDto.to_json())

# convert the object into a dict
download_request_dto_dict = download_request_dto_instance.to_dict()
# create an instance of DownloadRequestDto from a dict
download_request_dto_from_dict = DownloadRequestDto.from_dict(download_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


