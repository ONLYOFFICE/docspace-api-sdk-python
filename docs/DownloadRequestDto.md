# DownloadRequestDto
The files and folders to pack into one archive, together with the formats they are converted to.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**return_single_operation** | **bool** | Which operations the answer carries: `true` returns the operation this call started and nothing else, `false`  returns every operation of the same kind that the caller has running or unread. When nothing was queued, which  happens for an empty selection, `true` falls back to the full list. | [optional] 
**folder_ids** | [**List[DownloadRequestDtoAllOfFolderIds]**](DownloadRequestDtoAllOfFolderIds.md) | The folders to pack, by id; everything inside them that the caller may read goes into the archive. A number  addresses a folder stored in the portal itself, a string addresses a folder on a connected third-party  account, and both kinds may be sent in one list. | [optional] 
**file_ids** | [**List[DownloadRequestDtoAllOfFileIds]**](DownloadRequestDtoAllOfFileIds.md) | The files to pack as they are, by id, without conversion. A number addresses a file stored in the portal  itself, a string addresses a file on a connected third-party account, and both kinds may be sent in one list. | [optional] 
**file_convert_ids** | [**List[DownloadRequestItemDto]**](DownloadRequestItemDto.md) | The files to convert before they are packed, each named together with the format it is converted to. A file  listed here does not have to be repeated in `fileIds`. | [optional] 

## Example

```python
from docspace_api_sdk.models.download_request_dto import DownloadRequestDto

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


