# AuditEventDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**var_date** | [**ApiDateTime**](ApiDateTime.md) |  | [optional] 
**user** | **str** | User | [optional] 
**user_id** | **str** | User ID | [optional] 
**action** | **str** | Action | [optional] 
**action_id** | [**MessageAction**](MessageAction.md) |  | [optional] 
**ip** | **str** | IP | [optional] 
**country** | **str** | Country | [optional] 
**city** | **str** | City | [optional] 
**browser** | **str** | Browser | [optional] 
**platform** | **str** | Platform | [optional] 
**page** | **str** | Page | [optional] 
**action_type** | [**ActionType**](ActionType.md) |  | [optional] 
**product** | [**ProductType**](ProductType.md) |  | [optional] 
**module** | [**ModuleType**](ModuleType.md) |  | [optional] 
**target** | **List[str]** | List of targets | [optional] 
**entries** | [**List[EntryType]**](EntryType.md) | List of entry types | [optional] 
**context** | **str** | Context | [optional] 

## Example

```python
from docspace.models.audit_event_dto import AuditEventDto

# TODO update the JSON string below
json = "{}"
# create an instance of AuditEventDto from a JSON string
audit_event_dto_instance = AuditEventDto.from_json(json)
# print the JSON string representation of the object
print(AuditEventDto.to_json())

# convert the object into a dict
audit_event_dto_dict = audit_event_dto_instance.to_dict()
# create an instance of AuditEventDto from a dict
audit_event_dto_from_dict = AuditEventDto.from_dict(audit_event_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


