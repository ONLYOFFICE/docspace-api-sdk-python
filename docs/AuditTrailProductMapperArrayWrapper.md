# AuditTrailProductMapperArrayWrapper
The successful API response containing the list of AuditTrailProductMapperDto objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**List[AuditTrailProductMapperDto]**](AuditTrailProductMapperDto.md) | The list of AuditTrailProductMapperDto objects returned by the operation. | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.audit_trail_product_mapper_array_wrapper import AuditTrailProductMapperArrayWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of AuditTrailProductMapperArrayWrapper from a JSON string
audit_trail_product_mapper_array_wrapper_instance = AuditTrailProductMapperArrayWrapper.from_json(json)
# print the JSON string representation of the object
print(AuditTrailProductMapperArrayWrapper.to_json())

# convert the object into a dict
audit_trail_product_mapper_array_wrapper_dict = audit_trail_product_mapper_array_wrapper_instance.to_dict()
# create an instance of AuditTrailProductMapperArrayWrapper from a dict
audit_trail_product_mapper_array_wrapper_from_dict = AuditTrailProductMapperArrayWrapper.from_dict(audit_trail_product_mapper_array_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


