# TenantRoomQuotaSettingsWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**TenantRoomQuotaSettings**](TenantRoomQuotaSettings.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace_api_sdk.models.tenant_room_quota_settings_wrapper import TenantRoomQuotaSettingsWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of TenantRoomQuotaSettingsWrapper from a JSON string
tenant_room_quota_settings_wrapper_instance = TenantRoomQuotaSettingsWrapper.from_json(json)
# print the JSON string representation of the object
print(TenantRoomQuotaSettingsWrapper.to_json())

# convert the object into a dict
tenant_room_quota_settings_wrapper_dict = tenant_room_quota_settings_wrapper_instance.to_dict()
# create an instance of TenantRoomQuotaSettingsWrapper from a dict
tenant_room_quota_settings_wrapper_from_dict = TenantRoomQuotaSettingsWrapper.from_dict(tenant_room_quota_settings_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


