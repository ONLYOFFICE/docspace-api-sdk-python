# EditorConfigurationDto
How the editors behave for this opening: the mode, the language, the interface, and who is editing.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callback_url** | **str** | Where the editors post the document back to when they save it. A client must not call it itself; it is the  address the document service uses. | [optional] 
**co_editing** | [**CoEditingConfig**](CoEditingConfig.md) | How co-editing starts out for this session and whether the user may switch it in the interface. | [optional] 
**create_url** | **str** | Where the editor sends the user when they ask for a new document of the same type. It is empty when creating  one is not offered here. | [optional] 
**customization** | [**CustomizationConfigDto**](CustomizationConfigDto.md) | How the editor interface is dressed for this portal, this document and this layout. | [optional] 
**embedded** | [**EmbeddedConfig**](EmbeddedConfig.md) | The addresses the framed viewer needs. It is filled in only for the embedded layout. | [optional] 
**encryption_keys** | [**List[EncryptionKeyDto]**](EncryptionKeyDto.md) | The caller's end-to-end encryption keys, added only when the document lies in a private room, so that the  editors can decrypt it in the browser. It is empty everywhere else. | [optional] 
**lang** | **str** | The culture the editor interface is shown in, taken from the profile of the caller. | 
**mode** | **str** | `edit` when this session may write the document, `view` when it may only read it. | 
**mode_write** | **bool** | Whether this session may write; it is what the mode above says in one word. | [optional] 
**plugins** | [**PluginsConfig**](PluginsConfig.md) | Which editor plugins are offered. The portal currently offers none, so the list inside comes back empty. | [optional] 
**recent** | [**List[RecentConfig]**](RecentConfig.md) | The documents offered in the editor's recent list. It is left out altogether when there is nothing to offer. | [optional] 
**templates** | [**List[TemplatesConfig]**](TemplatesConfig.md) | Always empty: the portal no longer passes creation templates through the editor configuration. | [optional] 
**user** | [**UserConfig**](UserConfig.md) | The account the editors attribute changes to. It is empty for an anonymous session opened through an external  link, and the editors then ask for a name themselves. | [optional] 

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


