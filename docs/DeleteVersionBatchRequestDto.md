# DeleteVersionBatchRequestDto

Request parameters for deleting file's version

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delete_after** | **bool** | Specifies whether to delete a file after the editing session is finished or not | [optional] 
**file_id** | **int** |  | [optional] 
**versions** | **List[int]** |  | [optional] 

## Example

```python
from docspace.models.delete_version_batch_request_dto import DeleteVersionBatchRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteVersionBatchRequestDto from a JSON string
delete_version_batch_request_dto_instance = DeleteVersionBatchRequestDto.from_json(json)
# print the JSON string representation of the object
print(DeleteVersionBatchRequestDto.to_json())

# convert the object into a dict
delete_version_batch_request_dto_dict = delete_version_batch_request_dto_instance.to_dict()
# create an instance of DeleteVersionBatchRequestDto from a dict
delete_version_batch_request_dto_from_dict = DeleteVersionBatchRequestDto.from_dict(delete_version_batch_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


