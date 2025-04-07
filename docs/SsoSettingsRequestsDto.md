# SsoSettingsRequestsDto

SSO settings request parameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**serialize_settings** | **str** | Serialized SSO settings | [optional] 

## Example

```python
from docspace.models.sso_settings_requests_dto import SsoSettingsRequestsDto

# TODO update the JSON string below
json = "{}"
# create an instance of SsoSettingsRequestsDto from a JSON string
sso_settings_requests_dto_instance = SsoSettingsRequestsDto.from_json(json)
# print the JSON string representation of the object
print(SsoSettingsRequestsDto.to_json())

# convert the object into a dict
sso_settings_requests_dto_dict = sso_settings_requests_dto_instance.to_dict()
# create an instance of SsoSettingsRequestsDto from a dict
sso_settings_requests_dto_from_dict = SsoSettingsRequestsDto.from_dict(sso_settings_requests_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


