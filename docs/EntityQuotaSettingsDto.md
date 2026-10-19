# EntityQuotaSettingsDto
The default storage quota of users, rooms or AI agents, as it is stored.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_quota** | **bool** | Specifies if the quota is enabled for the tenant entity or not. | [optional] 
**default_quota** | **int** | The default quota of the tenant entity. | [optional] 
**last_recalculate_date** | **datetime** | The date of the last quota recalculation. | [optional] 
**last_modified** | **datetime** | The timestamp indicating when the settings were last modified. | [optional] 

## Example

```python
from docspace_api_sdk.models.entity_quota_settings_dto import EntityQuotaSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of EntityQuotaSettingsDto from a JSON string
entity_quota_settings_dto_instance = EntityQuotaSettingsDto.from_json(json)
# print the JSON string representation of the object
print(EntityQuotaSettingsDto.to_json())

# convert the object into a dict
entity_quota_settings_dto_dict = entity_quota_settings_dto_instance.to_dict()
# create an instance of EntityQuotaSettingsDto from a dict
entity_quota_settings_dto_from_dict = EntityQuotaSettingsDto.from_dict(entity_quota_settings_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


