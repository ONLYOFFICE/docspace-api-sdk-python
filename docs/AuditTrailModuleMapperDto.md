# AuditTrailModuleMapperDto
The audit trail actions of one module.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**module_type** | **str** | The location inside the product, as the `moduleType` filter of `GET api/2.0/security/audit/events/filter`  spells it. | [optional] 
**actions** | [**List[AuditTrailActionMapperDto]**](AuditTrailActionMapperDto.md) | Every action this module can record. Each action appears under exactly one module, so this tree is where a  caller learns which module a given action belongs to. | [optional] 

## Example

```python
from docspace_api_sdk.models.audit_trail_module_mapper_dto import AuditTrailModuleMapperDto

# TODO update the JSON string below
json = "{}"
# create an instance of AuditTrailModuleMapperDto from a JSON string
audit_trail_module_mapper_dto_instance = AuditTrailModuleMapperDto.from_json(json)
# print the JSON string representation of the object
print(AuditTrailModuleMapperDto.to_json())

# convert the object into a dict
audit_trail_module_mapper_dto_dict = audit_trail_module_mapper_dto_instance.to_dict()
# create an instance of AuditTrailModuleMapperDto from a dict
audit_trail_module_mapper_dto_from_dict = AuditTrailModuleMapperDto.from_dict(audit_trail_module_mapper_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


