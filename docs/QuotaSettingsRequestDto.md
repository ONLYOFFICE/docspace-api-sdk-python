# QuotaSettingsRequestDto
The default storage limit given to newly created users, rooms or AI agents, and whether it is enforced.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_quota** | **bool** | Whether the limit is enforced at all. While it is false the size is ignored and nothing created afterwards  carries a limit; objects that already have one keep it either way. | [optional] 
**default_quota** | [**QuotaSettingsRequestDtoDefaultQuota**](QuotaSettingsRequestDtoDefaultQuota.md) |  | 

## Example

```python
from docspace_api_sdk.models.quota_settings_request_dto import QuotaSettingsRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of QuotaSettingsRequestDto from a JSON string
quota_settings_request_dto_instance = QuotaSettingsRequestDto.from_json(json)
# print the JSON string representation of the object
print(QuotaSettingsRequestDto.to_json())

# convert the object into a dict
quota_settings_request_dto_dict = quota_settings_request_dto_instance.to_dict()
# create an instance of QuotaSettingsRequestDto from a dict
quota_settings_request_dto_from_dict = QuotaSettingsRequestDto.from_dict(quota_settings_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


