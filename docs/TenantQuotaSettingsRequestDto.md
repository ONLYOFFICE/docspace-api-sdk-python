# TenantQuotaSettingsRequestDto
The storage limit set on one tenant of a self-hosted installation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **int** | The tenant the limit applies to, by tenant ID. Only a self-hosted installation has more than one, which is  why the operation is refused on SaaS. | 
**quota** | **int** | The limit in bytes. A negative value is not a smaller limit but the absence of one: it removes whatever limit  the tenant had. The value is a ceiling on stored data and says nothing about how much of it is already used. | [optional] 

## Example

```python
from docspace_api_sdk.models.tenant_quota_settings_request_dto import TenantQuotaSettingsRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of TenantQuotaSettingsRequestDto from a JSON string
tenant_quota_settings_request_dto_instance = TenantQuotaSettingsRequestDto.from_json(json)
# print the JSON string representation of the object
print(TenantQuotaSettingsRequestDto.to_json())

# convert the object into a dict
tenant_quota_settings_request_dto_dict = tenant_quota_settings_request_dto_instance.to_dict()
# create an instance of TenantQuotaSettingsRequestDto from a dict
tenant_quota_settings_request_dto_from_dict = TenantQuotaSettingsRequestDto.from_dict(tenant_quota_settings_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


