# AuditEventDto
The audit event parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The audit event ID. | [optional] 
**var_date** | [**ApiDateTime**](ApiDateTime.md) |  | [optional] 
**user** | **str** | The name of the user who triggered the audit event. | [optional] 
**user_id** | **str** | The ID of the user who triggered the audit event. | [optional] 
**action** | **str** | The audit event action. | [optional] 
**action_id** | [**MessageAction**](MessageAction.md) |  | [optional] 
**ip** | **str** | The audit event IP. | [optional] 
**country** | **str** | The audit event country. | [optional] 
**city** | **str** | The audit event city. | [optional] 
**browser** | **str** | The audit event browser. | [optional] 
**platform** | **str** | The audit event platform. | [optional] 
**page** | **str** | The audit event page. | [optional] 
**action_type** | [**ActionType**](ActionType.md) |  | [optional] 
**product** | [**ProductType**](ProductType.md) |  | [optional] 
**module** | [**ModuleType**](ModuleType.md) |  | [optional] 
**target** | **List[str]** | The list of target objects affected by the audit event (e.g., document ID, user account). | [optional] 
**entries** | [**List[EntryType]**](EntryType.md) | The list of audit entry types (e.g., Folder, User, File). | [optional] 
**context** | **str** | The audit event context. | [optional] 

## Example

```python
from docspace-api-python.models.audit_event_dto import AuditEventDto

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


