# CustomFieldRequest
The parameters of a custom text field.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The field name. The names are matched without regard to case. | 
**value** | **str** | The field value. Null or empty removes the field from the entry. | [optional] 

## Example

```python
from docspace_api_sdk.models.custom_field_request import CustomFieldRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CustomFieldRequest from a JSON string
custom_field_request_instance = CustomFieldRequest.from_json(json)
# print the JSON string representation of the object
print(CustomFieldRequest.to_json())

# convert the object into a dict
custom_field_request_dict = custom_field_request_instance.to_dict()
# create an instance of CustomFieldRequest from a dict
custom_field_request_from_dict = CustomFieldRequest.from_dict(custom_field_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


