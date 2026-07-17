# ExternalSharingSettingsDto
The Access Control external sharing settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_share** | **bool** | Specifies whether external (public) link creation is allowed. | [optional] 
**default_share_link_internal** | **bool** | Specifies the default sharing link type: true = DocSpace users only, false = Anyone with the link. | [optional] 
**external_share_apply_to_documents** | **bool** | When external sharing is restricted, specifies whether the restriction applies to the My Documents section. | [optional] 
**external_share_apply_to_rooms** | **bool** | When external sharing is restricted, specifies whether the restriction applies to the Rooms section. | [optional] 
**block_existing_links_on_restrict** | **bool** | When external sharing is restricted, specifies whether existing public links are blocked immediately. | [optional] 

## Example

```python
from docspace_api_sdk.models.external_sharing_settings_dto import ExternalSharingSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalSharingSettingsDto from a JSON string
external_sharing_settings_dto_instance = ExternalSharingSettingsDto.from_json(json)
# print the JSON string representation of the object
print(ExternalSharingSettingsDto.to_json())

# convert the object into a dict
external_sharing_settings_dto_dict = external_sharing_settings_dto_instance.to_dict()
# create an instance of ExternalSharingSettingsDto from a dict
external_sharing_settings_dto_from_dict = ExternalSharingSettingsDto.from_dict(external_sharing_settings_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


