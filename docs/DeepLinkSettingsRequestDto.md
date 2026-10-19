# DeepLinkSettingsRequestDto
The deep link handling the portal applies on mobile devices.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**handling_mode** | [**DeepLinkHandlingMode**](DeepLinkHandlingMode.md) | Whether a link always opens in the browser, always in the native application, or asks the user each time. | [optional] 
**last_modified** | **datetime** | Accepted for compatibility with earlier clients and not read: the server keeps its own value. | [optional] 

## Example

```python
from docspace_api_sdk.models.deep_link_settings_request_dto import DeepLinkSettingsRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of DeepLinkSettingsRequestDto from a JSON string
deep_link_settings_request_dto_instance = DeepLinkSettingsRequestDto.from_json(json)
# print the JSON string representation of the object
print(DeepLinkSettingsRequestDto.to_json())

# convert the object into a dict
deep_link_settings_request_dto_dict = deep_link_settings_request_dto_instance.to_dict()
# create an instance of DeepLinkSettingsRequestDto from a dict
deep_link_settings_request_dto_from_dict = DeepLinkSettingsRequestDto.from_dict(deep_link_settings_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


