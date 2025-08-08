# BaseBatchRequestDto
The base batch request parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**return_single_operation** | **bool** | Specifies whether to return only the current operation | [optional] 
**folder_ids** | [**List[BaseBatchRequestDtoAllOfFolderIds]**](BaseBatchRequestDtoAllOfFolderIds.md) | The list of folder IDs of the base batch request. | [optional] 
**file_ids** | [**List[BaseBatchRequestDtoAllOfFileIds]**](BaseBatchRequestDtoAllOfFileIds.md) | The list of file IDs of the base batch request. | [optional] 

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


