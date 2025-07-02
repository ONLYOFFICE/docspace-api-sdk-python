# PasswordSettingsRequestsDto
The request parameters for configuring the password complexity requirements.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min_length** | **int** | The minimum number of characters required for valid passwords. | [optional] 
**upper_case** | **bool** | Specifies whether the password should contain the uppercase letters or not. | [optional] 
**digits** | **bool** | Specifies whether the password should contain the digits or not. | [optional] 
**spec_symbols** | **bool** | Specifies whether the password should contain the special symbols or not. | [optional] 

## Example

```python
from docspace-api-python.models.password_settings_requests_dto import PasswordSettingsRequestsDto

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


