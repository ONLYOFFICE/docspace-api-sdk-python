# AdminMessageBaseSettingsRequestsDto
The request parameters for the administrator message configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | The email address used for sending administrator messages. | 
**culture** | **str** | The locale identifier for message localization. | [optional] 

## Example

```python
from docspace-api-sdk.models.admin_message_base_settings_requests_dto import AdminMessageBaseSettingsRequestsDto

# TODO update the JSON string below
json = "{}"
# create an instance of AdminMessageBaseSettingsRequestsDto from a JSON string
admin_message_base_settings_requests_dto_instance = AdminMessageBaseSettingsRequestsDto.from_json(json)
# print the JSON string representation of the object
print(AdminMessageBaseSettingsRequestsDto.to_json())

# convert the object into a dict
admin_message_base_settings_requests_dto_dict = admin_message_base_settings_requests_dto_instance.to_dict()
# create an instance of AdminMessageBaseSettingsRequestsDto from a dict
admin_message_base_settings_requests_dto_from_dict = AdminMessageBaseSettingsRequestsDto.from_dict(admin_message_base_settings_requests_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


