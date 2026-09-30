# ThirdPartyConfigurationDto
Everything an editor client needs in order to open one document: the document itself, the editor setup for this  caller, and the signature that lets the editors trust both.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document** | [**DocumentConfigDto**](DocumentConfigDto.md) | The document as the editors address it: its revision key, title, type, download address and the permissions of  this caller on it. | 
**document_type** | **str** | The editor family the file opens in - `word`, `cell`, `slide`, `pdf` or `diagram`. It comes back empty for a  format no editor handles. | 
**editor_config** | [**EditorConfigurationDto**](EditorConfigurationDto.md) | How the editor is set up for this opening: the mode, the language, the interface customization, the callback  the editors save through, and the account they attribute changes to. | 
**editor_type** | [**EditorType**](EditorType.md) | The layout the configuration was actually built for. It echoes the requested one except where the room  overruled it, as the templates folder does by forcing the embedded viewer. | 
**editor_url** | **str** | The address of the editor api script the client has to load, with the shard key of this document already  appended. Load it as it is given rather than assembling it by hand. | 
**token** | **str** | Signs this whole configuration so that the editors can trust it; anything a client changes in the  configuration invalidates it. It stays empty on a portal that has no signature secret configured for the  document service. | [optional] 
**type** | **str** | The layout spelled as a lowercase word - `desktop`, `mobile` or `embedded` - the same value the editor type  carries as a number. | [optional] 
**file** | [**ThirdPartyFileDto**](ThirdPartyFileDto.md) | The file the configuration was built for, in the same shape the file listings report it. | 
**error_message** | **str** | Filled in when the document could not be prepared for opening; the rest of the configuration should then not  be handed to the editors. | [optional] 
**start_filling** | **bool** | Whether this caller may start a filling session on the form from inside the editor. It stays empty when the  file is not a form opened where starting is possible at all. | [optional] 
**filling_status** | **bool** | True once the caller holds a role in the running filling session of this form. It stays empty outside a  virtual data room, where roles are the only place it is set. | [optional] 
**start_filling_mode** | [**StartFillingMode**](StartFillingMode.md) | Which filling button the editor offers: none at all, sharing the form out for others to fill, starting a  filling session, or starting one inside the form-filling room. | [optional] 
**filling_session_id** | **str** | Identifies the filling session this opening belongs to, and is empty when the document is not opened as part  of one. Submissions made in the editor are collected under it. | [optional] 
**quota_exceeded_scope** | [**QuotaScope**](QuotaScope.md) | Names the quota that ran out - the user, the room or the portal - and is set only when the document had to be  opened read-only because of it. | [optional] 
**generation_tool_call_state** | [**EditorToolCallStateDto**](EditorToolCallStateDto.md) | The generation the editor should run as soon as the document opens. It is set only for a document an AI agent  produced and left waiting for its content, and is empty for every other file. | [optional] 

## Example

```python
from docspace_api_sdk.models.third_party_configuration_dto import ThirdPartyConfigurationDto

# TODO update the JSON string below
json = "{}"
# create an instance of ThirdPartyConfigurationDto from a JSON string
third_party_configuration_dto_instance = ThirdPartyConfigurationDto.from_json(json)
# print the JSON string representation of the object
print(ThirdPartyConfigurationDto.to_json())

# convert the object into a dict
third_party_configuration_dto_dict = third_party_configuration_dto_instance.to_dict()
# create an instance of ThirdPartyConfigurationDto from a dict
third_party_configuration_dto_from_dict = ThirdPartyConfigurationDto.from_dict(third_party_configuration_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


