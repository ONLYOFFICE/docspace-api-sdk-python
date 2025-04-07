# AuditEventArrayWrapper


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**List[AuditEventDto]**](AuditEventDto.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace.models.audit_event_array_wrapper import AuditEventArrayWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of AuditEventArrayWrapper from a JSON string
audit_event_array_wrapper_instance = AuditEventArrayWrapper.from_json(json)
# print the JSON string representation of the object
print(AuditEventArrayWrapper.to_json())

# convert the object into a dict
audit_event_array_wrapper_dict = audit_event_array_wrapper_instance.to_dict()
# create an instance of AuditEventArrayWrapper from a dict
audit_event_array_wrapper_from_dict = AuditEventArrayWrapper.from_dict(audit_event_array_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


