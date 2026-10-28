# AuditTrailTypesWrapper
The successful API response containing the AuditTrailTypesDto object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**AuditTrailTypesDto**](AuditTrailTypesDto.md) | The AuditTrailTypesDto object returned by the operation. | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.audit_trail_types_wrapper import AuditTrailTypesWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of AuditTrailTypesWrapper from a JSON string
audit_trail_types_wrapper_instance = AuditTrailTypesWrapper.from_json(json)
# print the JSON string representation of the object
print(AuditTrailTypesWrapper.to_json())

# convert the object into a dict
audit_trail_types_wrapper_dict = audit_trail_types_wrapper_instance.to_dict()
# create an instance of AuditTrailTypesWrapper from a dict
audit_trail_types_wrapper_from_dict = AuditTrailTypesWrapper.from_dict(audit_trail_types_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


