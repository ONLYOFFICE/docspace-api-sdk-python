# SettingsRequestDto
The settings request parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**set** | **bool** | Specifies whether to set the specified settings or not. | [optional] 

## Example

```python
from docspace-api-python.models.settings_request_dto import SettingsRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of SettingsRequestDto from a JSON string
settings_request_dto_instance = SettingsRequestDto.from_json(json)
# print the JSON string representation of the object
print(SettingsRequestDto.to_json())

# convert the object into a dict
settings_request_dto_dict = settings_request_dto_instance.to_dict()
# create an instance of SettingsRequestDto from a dict
settings_request_dto_from_dict = SettingsRequestDto.from_dict(settings_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


