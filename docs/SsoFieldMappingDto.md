# SsoFieldMappingDto
Which SAML attributes fill the profile fields of a user who signs in through SSO.

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
from docspace_api_sdk.models.sso_field_mapping_dto import SsoFieldMappingDto

# TODO update the JSON string below
json = "{}"
# create an instance of SsoFieldMappingDto from a JSON string
sso_field_mapping_dto_instance = SsoFieldMappingDto.from_json(json)
# print the JSON string representation of the object
print(SsoFieldMappingDto.to_json())

# convert the object into a dict
sso_field_mapping_dto_dict = sso_field_mapping_dto_instance.to_dict()
# create an instance of SsoFieldMappingDto from a dict
sso_field_mapping_dto_from_dict = SsoFieldMappingDto.from_dict(sso_field_mapping_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


