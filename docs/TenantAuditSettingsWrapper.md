# TenantAuditSettingsWrapper
The successful API response containing the TenantAuditSettingsDto object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**TenantAuditSettingsDto**](TenantAuditSettingsDto.md) | The TenantAuditSettingsDto object returned by the operation. | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.tenant_audit_settings_wrapper import TenantAuditSettingsWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of TenantAuditSettingsWrapper from a JSON string
tenant_audit_settings_wrapper_instance = TenantAuditSettingsWrapper.from_json(json)
# print the JSON string representation of the object
print(TenantAuditSettingsWrapper.to_json())

# convert the object into a dict
tenant_audit_settings_wrapper_dict = tenant_audit_settings_wrapper_instance.to_dict()
# create an instance of TenantAuditSettingsWrapper from a dict
tenant_audit_settings_wrapper_from_dict = TenantAuditSettingsWrapper.from_dict(tenant_audit_settings_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


