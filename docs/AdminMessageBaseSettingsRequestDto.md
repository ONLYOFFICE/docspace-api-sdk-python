# AdminMessageBaseSettingsRequestDto
Who is invited to join the portal, and in which language the invitation is written.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | The address the join link is sent to. It has to be a well-formed ASCII address rather than an  internationalized one, must not already belong to a member of the portal, and, where the portal trusts named  domains only, has to end with one of them; any of these faults is refused with 400. | 
**culture** | **str** | The language the letter is written in, as a culture name such as `en-US`. A culture the installation does not  have falls back to the portal language rather than failing the call. | [optional] 

## Example

```python
from docspace_api_sdk.models.admin_message_base_settings_request_dto import AdminMessageBaseSettingsRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of AdminMessageBaseSettingsRequestDto from a JSON string
admin_message_base_settings_request_dto_instance = AdminMessageBaseSettingsRequestDto.from_json(json)
# print the JSON string representation of the object
print(AdminMessageBaseSettingsRequestDto.to_json())

# convert the object into a dict
admin_message_base_settings_request_dto_dict = admin_message_base_settings_request_dto_instance.to_dict()
# create an instance of AdminMessageBaseSettingsRequestDto from a dict
admin_message_base_settings_request_dto_from_dict = AdminMessageBaseSettingsRequestDto.from_dict(admin_message_base_settings_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


