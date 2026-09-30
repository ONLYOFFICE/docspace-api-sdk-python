# BaseBatchRequestDto
The files and folders a background operation is applied to.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**return_single_operation** | **bool** | Which operations the answer carries: `true` returns the operation this call started and nothing else, `false`  returns every operation of the same kind that the caller has running or unread. When nothing was queued, which  happens for an empty selection, `true` falls back to the full list. | [optional] 
**folder_ids** | [**List[BaseBatchRequestDtoAllOfFolderIds]**](BaseBatchRequestDtoAllOfFolderIds.md) | The folders to act on, by id, as reported by a folder listing such as `GET api/2.0/files/{folderId}`. A number  addresses a folder stored in the portal itself, a string addresses a folder on a connected third-party  account, and both kinds may be sent in one list. | [optional] 
**file_ids** | [**List[BaseBatchRequestDtoAllOfFileIds]**](BaseBatchRequestDtoAllOfFileIds.md) | The files to act on, by id, as reported by a folder listing such as `GET api/2.0/files/{folderId}`. A number  addresses a file stored in the portal itself, a string addresses a file on a connected third-party account,  and both kinds may be sent in one list. | [optional] 

## Example

```python
from docspace_api_sdk.models.base_batch_request_dto import BaseBatchRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of BaseBatchRequestDto from a JSON string
base_batch_request_dto_instance = BaseBatchRequestDto.from_json(json)
# print the JSON string representation of the object
print(BaseBatchRequestDto.to_json())

# convert the object into a dict
base_batch_request_dto_dict = base_batch_request_dto_instance.to_dict()
# create an instance of BaseBatchRequestDto from a dict
base_batch_request_dto_from_dict = BaseBatchRequestDto.from_dict(base_batch_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


