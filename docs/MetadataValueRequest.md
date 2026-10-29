# MetadataValueRequest
The parameters of a metadata field value.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_id** | **int** | The field ID. | 
**string_value** | **str** | The string value. | [optional] 
**number_value** | **int** | The number value: a whole number of at most 2^53-1 (9007199254740991) in magnitude, the largest integer a JSON  client reads exactly. A larger one is refused rather than stored and returned rounded. | [optional] 
**date_value** | **datetime** | The date value. A value without a time zone offset is treated as UTC, the same way the metadata filters treat their date bounds. | [optional] 
**option_ids** | **List[UUID]** | The selected choice option IDs. | [optional] 

## Example

```python
from docspace_api_sdk.models.metadata_value_request import MetadataValueRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MetadataValueRequest from a JSON string
metadata_value_request_instance = MetadataValueRequest.from_json(json)
# print the JSON string representation of the object
print(MetadataValueRequest.to_json())

# convert the object into a dict
metadata_value_request_dict = metadata_value_request_instance.to_dict()
# create an instance of MetadataValueRequest from a dict
metadata_value_request_from_dict = MetadataValueRequest.from_dict(metadata_value_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


