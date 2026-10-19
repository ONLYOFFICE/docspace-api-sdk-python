# AuditTrailProductDto
The audit trail actions of one product, grouped by module.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_type** | **str** | The product this branch of the tree belongs to, as the `productType` filter of this operation spells it and  as `GET api/2.0/security/audit/types` lists it under `productTypes`. | [optional] 
**modules** | [**List[AuditTrailModuleDto]**](AuditTrailModuleDto.md) | The locations inside the product. It is empty when `moduleType` was passed and this product has no module  of that name, which is why a product can come back with nothing under it. | [optional] 

## Example

```python
from docspace_api_sdk.models.audit_trail_product_dto import AuditTrailProductDto

# TODO update the JSON string below
json = "{}"
# create an instance of AuditTrailProductDto from a JSON string
audit_trail_product_dto_instance = AuditTrailProductDto.from_json(json)
# print the JSON string representation of the object
print(AuditTrailProductDto.to_json())

# convert the object into a dict
audit_trail_product_dto_dict = audit_trail_product_dto_instance.to_dict()
# create an instance of AuditTrailProductDto from a dict
audit_trail_product_dto_from_dict = AuditTrailProductDto.from_dict(audit_trail_product_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


