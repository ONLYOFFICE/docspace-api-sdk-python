# DuplicateRequestDto
The files and folders to duplicate.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**return_single_operation** | **bool** | Which operations the answer carries: `true` returns the operation this call started and nothing else, `false`  returns every operation of the same kind that the caller has running or unread. When nothing was queued, which  happens for an empty selection, `true` falls back to the full list. | [optional] 
**folder_ids** | [**List[DuplicateRequestDtoAllOfFolderIds]**](DuplicateRequestDtoAllOfFolderIds.md) | The folders to duplicate, by id; the copy of each one is created in the folder that already holds it. A number  addresses a folder stored in the portal itself, a string addresses a folder on a connected third-party  account, and both kinds may be sent in one list. | [optional] 
**file_ids** | [**List[DuplicateRequestDtoAllOfFileIds]**](DuplicateRequestDtoAllOfFileIds.md) | The files to duplicate, by id; the copy of each one is created in the folder that already holds it. A number  addresses a file stored in the portal itself, a string addresses a file on a connected third-party account,  and both kinds may be sent in one list. | [optional] 

## Example

```python
from docspace_api_sdk.models.duplicate_request_dto import DuplicateRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of DuplicateRequestDto from a JSON string
duplicate_request_dto_instance = DuplicateRequestDto.from_json(json)
# print the JSON string representation of the object
print(DuplicateRequestDto.to_json())

# convert the object into a dict
duplicate_request_dto_dict = duplicate_request_dto_instance.to_dict()
# create an instance of DuplicateRequestDto from a dict
duplicate_request_dto_from_dict = DuplicateRequestDto.from_dict(duplicate_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


