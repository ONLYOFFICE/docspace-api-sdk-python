# EntityQuotaDto
The default storage quota the portal applies to each user, room or AI agent.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_quota** | **bool** | Specifies if the quota is enabled for the tenant entity or not. | [optional] 
**default_quota** | **int** | The default quota of the tenant entity. | [optional] 
**last_recalculate_date** | **datetime** | The date of the last quota recalculation. | [optional] 

## Example

```python
from docspace_api_sdk.models.entity_quota_dto import EntityQuotaDto

# TODO update the JSON string below
json = "{}"
# create an instance of EntityQuotaDto from a JSON string
entity_quota_dto_instance = EntityQuotaDto.from_json(json)
# print the JSON string representation of the object
print(EntityQuotaDto.to_json())

# convert the object into a dict
entity_quota_dto_dict = entity_quota_dto_instance.to_dict()
# create an instance of EntityQuotaDto from a dict
entity_quota_dto_from_dict = EntityQuotaDto.from_dict(entity_quota_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


