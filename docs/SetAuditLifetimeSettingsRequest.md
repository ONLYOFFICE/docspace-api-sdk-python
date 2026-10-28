# SetAuditLifetimeSettingsRequest
How long the portal keeps its two security logs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**login_history_life_time** | **int** | How many days login events are kept, from 1 to 180. | [optional] 
**audit_trail_life_time** | **int** | How many days audit trail events are kept, from 1 to 180. | [optional] 
**last_modified** | **datetime** | Accepted for compatibility with earlier clients and not read: the server keeps its own value. | [optional] 

## Example

```python
from docspace_api_sdk.models.set_audit_lifetime_settings_request import SetAuditLifetimeSettingsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetAuditLifetimeSettingsRequest from a JSON string
set_audit_lifetime_settings_request_instance = SetAuditLifetimeSettingsRequest.from_json(json)
# print the JSON string representation of the object
print(SetAuditLifetimeSettingsRequest.to_json())

# convert the object into a dict
set_audit_lifetime_settings_request_dict = set_audit_lifetime_settings_request_instance.to_dict()
# create an instance of SetAuditLifetimeSettingsRequest from a dict
set_audit_lifetime_settings_request_from_dict = SetAuditLifetimeSettingsRequest.from_dict(set_audit_lifetime_settings_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


