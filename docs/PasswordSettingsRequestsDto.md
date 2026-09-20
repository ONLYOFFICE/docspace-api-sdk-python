# PasswordSettingsRequestsDto
The four values that make up the portal password policy, replaced together.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min_length** | **int** | The shortest password the portal will accept. It has to sit between the floor the installation is configured  with, 8 characters unless it was changed, and the ceiling of 30; a value outside that is refused with 400. | 
**upper_case** | **bool** | Whether a password must contain at least one uppercase letter. There is no partial update on this body, so  leaving the flag out stores it as `false` and drops the requirement. | [optional] 
**digits** | **bool** | Whether a password must contain at least one digit. Leaving the flag out stores it as `false` and drops the  requirement. | [optional] 
**spec_symbols** | **bool** | Whether a password must contain at least one special symbol. Leaving the flag out stores it as `false` and  drops the requirement. | [optional] 

## Example

```python
from docspace_api_sdk.models.password_settings_requests_dto import PasswordSettingsRequestsDto

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordSettingsRequestsDto from a JSON string
password_settings_requests_dto_instance = PasswordSettingsRequestsDto.from_json(json)
# print the JSON string representation of the object
print(PasswordSettingsRequestsDto.to_json())

# convert the object into a dict
password_settings_requests_dto_dict = password_settings_requests_dto_instance.to_dict()
# create an instance of PasswordSettingsRequestsDto from a dict
password_settings_requests_dto_from_dict = PasswordSettingsRequestsDto.from_dict(password_settings_requests_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


