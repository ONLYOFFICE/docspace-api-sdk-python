# TenantQuotaSettingsWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**TenantQuotaSettings**](TenantQuotaSettings.md) |  | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.tenant_quota_settings_wrapper import TenantQuotaSettingsWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of TenantQuotaSettingsWrapper from a JSON string
tenant_quota_settings_wrapper_instance = TenantQuotaSettingsWrapper.from_json(json)
# print the JSON string representation of the object
print(TenantQuotaSettingsWrapper.to_json())

# convert the object into a dict
tenant_quota_settings_wrapper_dict = tenant_quota_settings_wrapper_instance.to_dict()
# create an instance of TenantQuotaSettingsWrapper from a dict
tenant_quota_settings_wrapper_from_dict = TenantQuotaSettingsWrapper.from_dict(tenant_quota_settings_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


