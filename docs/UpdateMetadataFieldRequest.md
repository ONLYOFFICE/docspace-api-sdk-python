# UpdateMetadataFieldRequest
The parameters of a metadata field update. Every property is optional: a property that is omitted keeps its current value.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The new field name. | [optional] 
**type** | [**MetadataFieldType**](MetadataFieldType.md) | The new field type. The type can be changed only while the field has no values. | [optional] 
**options** | [**List[MetadataFieldOptionRequest]**](MetadataFieldOptionRequest.md) | The new choice options of the field. The options in use cannot be removed. | [optional] 
**order** | **int** | The new display position of the field inside the template: the fields are shown by it ascending. | [optional] 

## Example

```python
from docspace_api_sdk.models.update_metadata_field_request import UpdateMetadataFieldRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateMetadataFieldRequest from a JSON string
update_metadata_field_request_instance = UpdateMetadataFieldRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateMetadataFieldRequest.to_json())

# convert the object into a dict
update_metadata_field_request_dict = update_metadata_field_request_instance.to_dict()
# create an instance of UpdateMetadataFieldRequest from a dict
update_metadata_field_request_from_dict = UpdateMetadataFieldRequest.from_dict(update_metadata_field_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


