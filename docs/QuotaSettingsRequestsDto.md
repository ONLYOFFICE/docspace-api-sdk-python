# QuotaSettingsRequestsDto

Request parameters for the user quota settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_quota** | **bool** | Specifies if the quota settings are enabled or not | [optional] 
**default_quota** | [**QuotaSettingsRequestsDtoDefaultQuota**](QuotaSettingsRequestsDtoDefaultQuota.md) |  | [optional] 

## Example

```python
from docspace.models.quota_settings_requests_dto import QuotaSettingsRequestsDto

# TODO update the JSON string below
json = "{}"
# create an instance of QuotaSettingsRequestsDto from a JSON string
quota_settings_requests_dto_instance = QuotaSettingsRequestsDto.from_json(json)
# print the JSON string representation of the object
print(QuotaSettingsRequestsDto.to_json())

# convert the object into a dict
quota_settings_requests_dto_dict = quota_settings_requests_dto_instance.to_dict()
# create an instance of QuotaSettingsRequestsDto from a dict
quota_settings_requests_dto_from_dict = QuotaSettingsRequestsDto.from_dict(quota_settings_requests_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


