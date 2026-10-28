# QuotaSettingsRequestDtoDefaultQuota
The starting limit, in bytes, written as a JSON number. It has to parse as a whole number and may not exceed  the portal total storage quota, nor, on a self-hosted installation with a portal-wide quota switched on, that  quota; anything larger is refused with 400. It is applied to objects created from now on and leaves the  limits of existing ones as they are.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from docspace_api_sdk.models.quota_settings_request_dto_default_quota import QuotaSettingsRequestDtoDefaultQuota

# TODO update the JSON string below
json = "{}"
# create an instance of QuotaSettingsRequestDtoDefaultQuota from a JSON string
quota_settings_request_dto_default_quota_instance = QuotaSettingsRequestDtoDefaultQuota.from_json(json)
# print the JSON string representation of the object
print(QuotaSettingsRequestDtoDefaultQuota.to_json())

# convert the object into a dict
quota_settings_request_dto_default_quota_dict = quota_settings_request_dto_default_quota_instance.to_dict()
# create an instance of QuotaSettingsRequestDtoDefaultQuota from a dict
quota_settings_request_dto_default_quota_from_dict = QuotaSettingsRequestDtoDefaultQuota.from_dict(quota_settings_request_dto_default_quota_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


