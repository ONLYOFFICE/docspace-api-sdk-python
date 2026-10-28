# MetadataFieldRequest
The parameters of a metadata field.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The field name. | [optional] 
**type** | [**MetadataFieldType**](MetadataFieldType.md) | The field type. | [optional] 
**options** | [**List[MetadataFieldOptionRequest]**](MetadataFieldOptionRequest.md) | The choice options of the field. | [optional] 
**order** | **int** | The display position of the field inside the template: the fields are shown by it ascending, and equal positions  keep the order of creation. | [optional] 

## Example

```python
from docspace_api_sdk.models.metadata_field_request import MetadataFieldRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MetadataFieldRequest from a JSON string
metadata_field_request_instance = MetadataFieldRequest.from_json(json)
# print the JSON string representation of the object
print(MetadataFieldRequest.to_json())

# convert the object into a dict
metadata_field_request_dict = metadata_field_request_instance.to_dict()
# create an instance of MetadataFieldRequest from a dict
metadata_field_request_from_dict = MetadataFieldRequest.from_dict(metadata_field_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


