# ExternalSharingSettingsRequestDto
The complete external sharing policy of the portal. Every field is written, so an omitted one is stored as  false.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_share** | **bool** | Whether links that open a file or a room without a portal account may be created at all. This is the master  switch of the policy: while it is false the portal keeps the default link type internal, turns sharing on  social networks off, and applies the three restriction fields below. | [optional] 
**default_share_link_internal** | **bool** | The kind of link offered first when a new one is created: true offers a link only accounts of this portal can  open, false one that anyone holding it can open. The portal keeps it at true while external sharing is  switched off. | [optional] 
**external_share_apply_to_documents** | **bool** | Whether the restriction reaches personal documents: with true, no external link can be created for an entry in  the caller's own documents while external sharing is off. It has no effect while external sharing is allowed. | [optional] 
**external_share_apply_to_rooms** | **bool** | Whether the restriction reaches rooms: with true, no external link can be created for a room or its content  while external sharing is off, and a new room cannot be made public. It has no effect while external sharing  is allowed. | [optional] 
**block_existing_links_on_restrict** | **bool** | What happens to the links that already exist once external sharing is switched off: with true they stop  opening for the sections named above, with false they keep working and only new ones are refused. This is the  field that changes access to data that is already shared. | [optional] 

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


