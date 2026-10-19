# SetCustomFields
The parameters for setting custom fields.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fields** | [**List[CustomFieldRequest]**](CustomFieldRequest.md) | The custom fields to set on the entry. A listed field gets the value, a null or empty value removes the field  from the entry, the fields not listed are left alone. A name the portal has not seen yet creates the field. | 

## Example

```python
from docspace_api_sdk.models.set_custom_fields import SetCustomFields

# TODO update the JSON string below
json = "{}"
# create an instance of SetCustomFields from a JSON string
set_custom_fields_instance = SetCustomFields.from_json(json)
# print the JSON string representation of the object
print(SetCustomFields.to_json())

# convert the object into a dict
set_custom_fields_dict = set_custom_fields_instance.to_dict()
# create an instance of SetCustomFields from a dict
set_custom_fields_from_dict = SetCustomFields.from_dict(set_custom_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


