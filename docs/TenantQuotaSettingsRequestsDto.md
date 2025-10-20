# TenantQuotaSettingsRequestsDto
The request parameters for managing the tenant storage quota settings in a multi-tenant system.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **int** | The ID of the tenant whose quota is being configured. | 
**quota** | **int** | The storage quota limit in bytes allocated to the tenant. | [optional] 

## Example

```python
from docspace_api_sdk.models.tenant_quota_settings_requests_dto import TenantQuotaSettingsRequestsDto

# TODO update the JSON string below
json = "{}"
# create an instance of TenantQuotaSettingsRequestsDto from a JSON string
tenant_quota_settings_requests_dto_instance = TenantQuotaSettingsRequestsDto.from_json(json)
# print the JSON string representation of the object
print(TenantQuotaSettingsRequestsDto.to_json())

# convert the object into a dict
tenant_quota_settings_requests_dto_dict = tenant_quota_settings_requests_dto_instance.to_dict()
# create an instance of TenantQuotaSettingsRequestsDto from a dict
tenant_quota_settings_requests_dto_from_dict = TenantQuotaSettingsRequestsDto.from_dict(tenant_quota_settings_requests_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


