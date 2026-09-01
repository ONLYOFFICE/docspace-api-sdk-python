# TenantAuditSettingsResponseWrapper
The successful API response containing the TenantAuditSettings object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**TenantAuditSettings**](TenantAuditSettings.md) | The TenantAuditSettings object returned by the operation. | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.tenant_audit_settings_response_wrapper import TenantAuditSettingsResponseWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of TenantAuditSettingsResponseWrapper from a JSON string
tenant_audit_settings_response_wrapper_instance = TenantAuditSettingsResponseWrapper.from_json(json)
# print the JSON string representation of the object
print(TenantAuditSettingsResponseWrapper.to_json())

# convert the object into a dict
tenant_audit_settings_response_wrapper_dict = tenant_audit_settings_response_wrapper_instance.to_dict()
# create an instance of TenantAuditSettingsResponseWrapper from a dict
tenant_audit_settings_response_wrapper_from_dict = TenantAuditSettingsResponseWrapper.from_dict(tenant_audit_settings_response_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


