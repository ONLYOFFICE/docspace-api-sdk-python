# GreetingSettingsRequestsDto

The request parameters for managing the greeting settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The title of the tenant greeting settings. | 

## Example

```python
from docspace.models.greeting_settings_requests_dto import GreetingSettingsRequestsDto

# TODO update the JSON string below
json = "{}"
# create an instance of GreetingSettingsRequestsDto from a JSON string
greeting_settings_requests_dto_instance = GreetingSettingsRequestsDto.from_json(json)
# print the JSON string representation of the object
print(GreetingSettingsRequestsDto.to_json())

# convert the object into a dict
greeting_settings_requests_dto_dict = greeting_settings_requests_dto_instance.to_dict()
# create an instance of GreetingSettingsRequestsDto from a dict
greeting_settings_requests_dto_from_dict = GreetingSettingsRequestsDto.from_dict(greeting_settings_requests_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


