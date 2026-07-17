# ChatSettings
The chat settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_id** | **int** | The provider ID. | [optional] 
**model_id** | **str** | The model ID. | [optional] 
**prompt** | **str** | The prompt. | [optional] 
**internal** | **bool** | Specifies whether the provider is internal or not. | [optional] [readonly] 

## Example

```python
from docspace_api_sdk.models.chat_settings import ChatSettings

# TODO update the JSON string below
json = "{}"
# create an instance of ChatSettings from a JSON string
chat_settings_instance = ChatSettings.from_json(json)
# print the JSON string representation of the object
print(ChatSettings.to_json())

# convert the object into a dict
chat_settings_dict = chat_settings_instance.to_dict()
# create an instance of ChatSettings from a dict
chat_settings_from_dict = ChatSettings.from_dict(chat_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


