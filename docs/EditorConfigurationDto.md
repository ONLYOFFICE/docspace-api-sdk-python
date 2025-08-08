# EditorConfigurationDto
The editor configuration parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callback_url** | **str** | The callback URL of the editor. | [optional] 
**co_editing** | [**CoEditingConfig**](CoEditingConfig.md) |  | [optional] 
**create_url** | **str** | The creation URL of the editor. | [optional] 
**customization** | [**CustomizationConfigDto**](CustomizationConfigDto.md) |  | [optional] 
**embedded** | [**EmbeddedConfig**](EmbeddedConfig.md) |  | [optional] 
**encryption_keys** | [**EncryptionKeysConfig**](EncryptionKeysConfig.md) |  | [optional] 
**lang** | **str** | The language of the editor configuration. | [optional] 
**mode** | **str** | The mode of the editor configuration. | [optional] 
**mode_write** | **bool** | Specifies if the mode is write of the editor configuration. | [optional] 
**plugins** | [**PluginsConfig**](PluginsConfig.md) |  | [optional] 
**recent** | [**List[RecentConfig]**](RecentConfig.md) | The recent configuration of the editor. | [optional] 
**templates** | [**List[TemplatesConfig]**](TemplatesConfig.md) | The templates of the editor configuration. | [optional] 
**user** | [**UserConfig**](UserConfig.md) |  | [optional] 

## Example

```python
from docspace_api_sdk.models.editor_configuration_dto import EditorConfigurationDto

# TODO update the JSON string below
json = "{}"
# create an instance of EditorConfigurationDto from a JSON string
editor_configuration_dto_instance = EditorConfigurationDto.from_json(json)
# print the JSON string representation of the object
print(EditorConfigurationDto.to_json())

# convert the object into a dict
editor_configuration_dto_dict = editor_configuration_dto_instance.to_dict()
# create an instance of EditorConfigurationDto from a dict
editor_configuration_dto_from_dict = EditorConfigurationDto.from_dict(editor_configuration_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


