# AdminMessageSettingsRequestsDto

Request parameters for administrator message settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Message | [optional] 
**email** | **str** | Email | [optional] 
**culture** | **str** | Culture | [optional] 

## Example

```python
from docspace.models.admin_message_settings_requests_dto import AdminMessageSettingsRequestsDto

# TODO update the JSON string below
json = "{}"
# create an instance of AdminMessageSettingsRequestsDto from a JSON string
admin_message_settings_requests_dto_instance = AdminMessageSettingsRequestsDto.from_json(json)
# print the JSON string representation of the object
print(AdminMessageSettingsRequestsDto.to_json())

# convert the object into a dict
admin_message_settings_requests_dto_dict = admin_message_settings_requests_dto_instance.to_dict()
# create an instance of AdminMessageSettingsRequestsDto from a dict
admin_message_settings_requests_dto_from_dict = AdminMessageSettingsRequestsDto.from_dict(admin_message_settings_requests_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


