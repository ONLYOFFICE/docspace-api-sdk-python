# PasswordSettingsDto
The password settings parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min_length** | **int** | The minimum number of characters required for valid passwords. | 
**upper_case** | **bool** | Specifies whether the password should contain the uppercase letters or not. | 
**digits** | **bool** | Specifies whether the password should contain the digits or not. | 
**spec_symbols** | **bool** | Specifies whether the password should contain the special symbols or not. | 
**allowed_characters_regex_str** | **str** | The allowed password characters in the regex string format. | 
**digits_regex_str** | **str** | The password digits in the regex string format. | 
**upper_case_regex_str** | **str** | The password uppercase letters in the regex string format. | 
**spec_symbols_regex_str** | **str** | The passaword special symbols in the regex string format. | 

## Example

```python
from docspace_api_sdk.models.password_settings_dto import PasswordSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordSettingsDto from a JSON string
password_settings_dto_instance = PasswordSettingsDto.from_json(json)
# print the JSON string representation of the object
print(PasswordSettingsDto.to_json())

# convert the object into a dict
password_settings_dto_dict = password_settings_dto_instance.to_dict()
# create an instance of PasswordSettingsDto from a dict
password_settings_dto_from_dict = PasswordSettingsDto.from_dict(password_settings_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


