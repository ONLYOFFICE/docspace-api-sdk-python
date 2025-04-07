# PasswordSettingsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min_length** | **int** | Min length | [optional] 
**upper_case** | **bool** | Upper case | [optional] 
**digits** | **bool** | Digits | [optional] 
**spec_symbols** | **bool** | Spec symbols | [optional] 
**allowed_characters_regex_str** | **str** | Allowed characters regex str | [optional] 
**digits_regex_str** | **str** | Digits regex str | [optional] 
**upper_case_regex_str** | **str** | Upper case regex str | [optional] 
**spec_symbols_regex_str** | **str** | Spec symbols regex str | [optional] 

## Example

```python
from docspace.models.password_settings_dto import PasswordSettingsDto

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


