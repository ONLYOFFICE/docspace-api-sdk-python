# AuditTrailTypesDto
The vocabularies the audit and login-history filters accept, one array of names per dimension of an event.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | **List[str]** | Every action name the build can record, spelled as the `action` filter of  `GET api/2.0/security/audit/events/filter` and `GET api/2.0/security/audit/login/filter` expects it. It is  the whole vocabulary, not the actions this portal has recorded, and only a handful of the names are the  sign-in actions the login filter accepts. | [optional] 
**action_types** | **List[str]** | The kinds of change an action can stand for, spelled as the `actionType` filter of  `GET api/2.0/security/audit/events/filter` expects it. | [optional] 
**product_types** | **List[str]** | The products an action can belong to, spelled as the `productType` filter of  `GET api/2.0/security/audit/mappers` expects it. The audit trail itself cannot be filtered by product. | [optional] 
**module_types** | **List[str]** | The locations inside those products, spelled as the `moduleType` filter of  `GET api/2.0/security/audit/events/filter` and `GET api/2.0/security/audit/mappers` expects it. | [optional] 
**entry_types** | **List[str]** | The kinds of object an action can be applied to, spelled as the `entryType` filter of  `GET api/2.0/security/audit/events/filter` expects it. | [optional] 

## Example

```python
from docspace_api_sdk.models.audit_trail_types_dto import AuditTrailTypesDto

# TODO update the JSON string below
json = "{}"
# create an instance of AuditTrailTypesDto from a JSON string
audit_trail_types_dto_instance = AuditTrailTypesDto.from_json(json)
# print the JSON string representation of the object
print(AuditTrailTypesDto.to_json())

# convert the object into a dict
audit_trail_types_dto_dict = audit_trail_types_dto_instance.to_dict()
# create an instance of AuditTrailTypesDto from a dict
audit_trail_types_dto_from_dict = AuditTrailTypesDto.from_dict(audit_trail_types_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


