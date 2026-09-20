# OwnerIdSettingsRequestDto
The portal member named as the new owner of the portal.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owner_id** | **UUID** | The member who is to become the portal owner, by user ID. They have to be an active member of this portal and  not a guest; a member who is not a DocSpace administrator yet is promoted to one as part of the transfer, so  the portal needs a paid seat for them. | 

## Example

```python
from docspace_api_sdk.models.owner_id_settings_request_dto import OwnerIdSettingsRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of OwnerIdSettingsRequestDto from a JSON string
owner_id_settings_request_dto_instance = OwnerIdSettingsRequestDto.from_json(json)
# print the JSON string representation of the object
print(OwnerIdSettingsRequestDto.to_json())

# convert the object into a dict
owner_id_settings_request_dto_dict = owner_id_settings_request_dto_instance.to_dict()
# create an instance of OwnerIdSettingsRequestDto from a dict
owner_id_settings_request_dto_from_dict = OwnerIdSettingsRequestDto.from_dict(owner_id_settings_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


