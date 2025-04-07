# SsoFieldMapping


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** | First name | [optional] 
**last_name** | **str** | Last name | [optional] 
**email** | **str** | Email | [optional] 
**title** | **str** | Title | [optional] 
**location** | **str** | Location | [optional] 
**phone** | **str** | Phone | [optional] 

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


