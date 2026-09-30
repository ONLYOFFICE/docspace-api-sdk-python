# ExternalSharingSettingsDto
The external sharing policy of the portal as it now stands.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_share** | **bool** | Whether links that open a file or a room without a portal account may be created. While it is false the portal  also reports sharing on social networks as off and the default link type as internal, whatever was asked for. | [optional] 
**default_share_link_internal** | **bool** | The kind of link the portal offers first: true means a link only accounts of this portal can open, false one  that anyone holding it can open. | [optional] 
**external_share_apply_to_documents** | **bool** | Whether the restriction covers personal documents. It only has an effect while external sharing is off, so a  true here with sharing allowed restricts nothing. | [optional] 
**external_share_apply_to_rooms** | **bool** | Whether the restriction covers rooms, including the creation of new public ones. It only has an effect while  external sharing is off. | [optional] 
**block_existing_links_on_restrict** | **bool** | Whether links created before the restriction stop opening as well. With false they keep working and only new  ones are refused. | [optional] 

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


