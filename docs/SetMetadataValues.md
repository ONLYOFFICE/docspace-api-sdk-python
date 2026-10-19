# SetMetadataValues
The parameters for setting metadata values.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[MetadataValueRequest]**](MetadataValueRequest.md) | The metadata field values. An empty value clears the field. | 

## Example

```python
from docspace_api_sdk.models.set_metadata_values import SetMetadataValues

# TODO update the JSON string below
json = "{}"
# create an instance of SetMetadataValues from a JSON string
set_metadata_values_instance = SetMetadataValues.from_json(json)
# print the JSON string representation of the object
print(SetMetadataValues.to_json())

# convert the object into a dict
set_metadata_values_dict = set_metadata_values_instance.to_dict()
# create an instance of SetMetadataValues from a dict
set_metadata_values_from_dict = SetMetadataValues.from_dict(set_metadata_values_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


