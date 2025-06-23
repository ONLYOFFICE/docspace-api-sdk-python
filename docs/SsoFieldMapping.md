# SsoFieldMapping

The SSO field mapping.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** | The first name. | [optional] 
**last_name** | **str** | The last name. | [optional] 
**email** | **str** | The email address. | [optional] 
**title** | **str** | The title. | [optional] 
**location** | **str** | The location. | [optional] 
**phone** | **str** | The phone number. | [optional] 

## Example

```python
from docspace.models.sso_field_mapping import SsoFieldMapping

# TODO update the JSON string below
json = "{}"
# create an instance of SsoFieldMapping from a JSON string
sso_field_mapping_instance = SsoFieldMapping.from_json(json)
# print the JSON string representation of the object
print(SsoFieldMapping.to_json())

# convert the object into a dict
sso_field_mapping_dict = sso_field_mapping_instance.to_dict()
# create an instance of SsoFieldMapping from a dict
sso_field_mapping_from_dict = SsoFieldMapping.from_dict(sso_field_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


