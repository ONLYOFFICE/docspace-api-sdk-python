# ExternalSharingSettingsRequestDto
The Access Control external sharing settings request parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_share** | **bool** | Specifies whether external (public) link creation is allowed. | [optional] 
**default_share_link_internal** | **bool** | Specifies the default sharing link type: true = DocSpace users only, false = Anyone with the link.  Relevant only when ExternalShare is true. | [optional] 
**external_share_apply_to_documents** | **bool** | When external sharing is restricted, specifies whether to apply the restriction to the My Documents section.  Relevant only when ExternalShare is false. | [optional] 
**external_share_apply_to_rooms** | **bool** | When external sharing is restricted, specifies whether to apply the restriction to the Rooms section.  Relevant only when ExternalShare is false. | [optional] 
**block_existing_links_on_restrict** | **bool** | When external sharing is restricted, specifies whether to block existing public links immediately.  Relevant only when ExternalShare is false. | [optional] 

## Example

```python
from docspace_api_sdk.models.external_sharing_settings_request_dto import ExternalSharingSettingsRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalSharingSettingsRequestDto from a JSON string
external_sharing_settings_request_dto_instance = ExternalSharingSettingsRequestDto.from_json(json)
# print the JSON string representation of the object
print(ExternalSharingSettingsRequestDto.to_json())

# convert the object into a dict
external_sharing_settings_request_dto_dict = external_sharing_settings_request_dto_instance.to_dict()
# create an instance of ExternalSharingSettingsRequestDto from a dict
external_sharing_settings_request_dto_from_dict = ExternalSharingSettingsRequestDto.from_dict(external_sharing_settings_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


