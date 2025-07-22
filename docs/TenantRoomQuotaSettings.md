# TenantRoomQuotaSettings
The room quota settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_quota** | **bool** | Specifies if the quota is enabled for the tenant entity or not. | [optional] 
**default_quota** | **int** | The default quota of the tenant entity. | [optional] 
**last_recalculate_date** | **datetime** | The date of the last quota recalculation. | [optional] 
**last_modified** | **datetime** |  | [optional] 

## Example

```python
from docspace-api-sdk.models.tenant_room_quota_settings import TenantRoomQuotaSettings

# TODO update the JSON string below
json = "{}"
# create an instance of TenantRoomQuotaSettings from a JSON string
tenant_room_quota_settings_instance = TenantRoomQuotaSettings.from_json(json)
# print the JSON string representation of the object
print(TenantRoomQuotaSettings.to_json())

# convert the object into a dict
tenant_room_quota_settings_dict = tenant_room_quota_settings_instance.to_dict()
# create an instance of TenantRoomQuotaSettings from a dict
tenant_room_quota_settings_from_dict = TenantRoomQuotaSettings.from_dict(tenant_room_quota_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


