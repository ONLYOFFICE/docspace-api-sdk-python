# GreetingSettingsRequestDto
The greeting caption the portal shows its users.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The caption to store, which is kept as the portal name. An empty value clears the greeting and returns the  portal to the built-in default caption. On a cloud portal with a free or trial plan the text is also matched  against the character rule configured for the installation and a text that breaks it is refused, while a paid  cloud plan and a self-hosted installation apply no such check. | 

## Example

```python
from docspace_api_sdk.models.greeting_settings_request_dto import GreetingSettingsRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of GreetingSettingsRequestDto from a JSON string
greeting_settings_request_dto_instance = GreetingSettingsRequestDto.from_json(json)
# print the JSON string representation of the object
print(GreetingSettingsRequestDto.to_json())

# convert the object into a dict
greeting_settings_request_dto_dict = greeting_settings_request_dto_instance.to_dict()
# create an instance of GreetingSettingsRequestDto from a dict
greeting_settings_request_dto_from_dict = GreetingSettingsRequestDto.from_dict(greeting_settings_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


