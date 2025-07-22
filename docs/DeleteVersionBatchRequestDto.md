# DeleteVersionBatchRequestDto
The request parameters for deleting file versions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**return_single_operation** | **bool** | Specifies whether to return only the current operation | [optional] 
**delete_after** | **bool** | Specifies whether to delete a file after the editing session is finished or not. | [optional] 
**file_id** | **int** | The file ID to delete. | 
**versions** | **List[int]** | The collection of file versions to be deleted. | 

## Example

```python
from docspace-api-sdk.models.delete_version_batch_request_dto import DeleteVersionBatchRequestDto

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


