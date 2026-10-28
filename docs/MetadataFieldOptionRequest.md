# MetadataFieldOptionRequest
The parameters of a metadata field choice option.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | The option ID. Omit it for a new option. | [optional] 
**value** | **str** | The option value. | [optional] 

## Example

```python
from docspace_api_sdk.models.metadata_field_option_request import MetadataFieldOptionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MetadataFieldOptionRequest from a JSON string
metadata_field_option_request_instance = MetadataFieldOptionRequest.from_json(json)
# print the JSON string representation of the object
print(MetadataFieldOptionRequest.to_json())

# convert the object into a dict
metadata_field_option_request_dict = metadata_field_option_request_instance.to_dict()
# create an instance of MetadataFieldOptionRequest from a dict
metadata_field_option_request_from_dict = MetadataFieldOptionRequest.from_dict(metadata_field_option_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


