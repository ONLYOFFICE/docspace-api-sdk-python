# AuditTrailActionMapperDto
One audit trail action, with the kind of change it stands for and the kind of object it applies to.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_action** | **str** | The action name to send as the `action` filter of `GET api/2.0/security/audit/events/filter`, and the value  that comes back as `actionId` on an event. | [optional] 
**action_type** | **str** | The kind of change the action makes, accepted by the `actionType` filter of the same operation. | [optional] 
**entity** | **str** | The kind of object the action applies to, accepted by the `entryType` filter. It is `None` for an action  that targets no object, such as a settings change, and an action with a second object type reports only the  first one here. | [optional] 

## Example

```python
from docspace_api_sdk.models.audit_trail_action_mapper_dto import AuditTrailActionMapperDto

# TODO update the JSON string below
json = "{}"
# create an instance of AuditTrailActionMapperDto from a JSON string
audit_trail_action_mapper_dto_instance = AuditTrailActionMapperDto.from_json(json)
# print the JSON string representation of the object
print(AuditTrailActionMapperDto.to_json())

# convert the object into a dict
audit_trail_action_mapper_dto_dict = audit_trail_action_mapper_dto_instance.to_dict()
# create an instance of AuditTrailActionMapperDto from a dict
audit_trail_action_mapper_dto_from_dict = AuditTrailActionMapperDto.from_dict(audit_trail_action_mapper_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


