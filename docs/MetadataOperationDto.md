# MetadataOperationDto
The cascade metadata assignment operation status.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The operation ID. | [optional] 
**progress** | **float** | The operation progress percentage. | [optional] 
**is_completed** | **bool** | Specifies if the operation is completed. | [optional] 
**error** | **str** | The operation error message. | [optional] 
**template_ids** | **List[int]** | The IDs of the metadata templates the operation propagates to the subtree. Empty when there is no operation to  report, so the answer describes nothing in progress. | [optional] 

## Example

```python
from docspace_api_sdk.models.metadata_operation_dto import MetadataOperationDto

# TODO update the JSON string below
json = "{}"
# create an instance of MetadataOperationDto from a JSON string
metadata_operation_dto_instance = MetadataOperationDto.from_json(json)
# print the JSON string representation of the object
print(MetadataOperationDto.to_json())

# convert the object into a dict
metadata_operation_dto_dict = metadata_operation_dto_instance.to_dict()
# create an instance of MetadataOperationDto from a dict
metadata_operation_dto_from_dict = MetadataOperationDto.from_dict(metadata_operation_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


