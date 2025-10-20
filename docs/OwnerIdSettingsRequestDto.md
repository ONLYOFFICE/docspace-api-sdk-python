# OwnerIdSettingsRequestDto
The request parameters for managing the owner-specific settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owner_id** | **str** | The ID of the owner whose settings are being managed. | 

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


