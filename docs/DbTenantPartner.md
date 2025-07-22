# DbTenantPartner
The database tenant partner parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **int** | The tenant ID. | [optional] 
**partner_id** | **str** | The partner ID. | [optional] 
**affiliate_id** | **str** | The affiliate ID. | [optional] 
**campaign** | **str** | The tenant partner campaign. | [optional] 

## Example

```python
from docspace-api-sdk.models.db_tenant_partner import DbTenantPartner

# TODO update the JSON string below
json = "{}"
# create an instance of DbTenantPartner from a JSON string
db_tenant_partner_instance = DbTenantPartner.from_json(json)
# print the JSON string representation of the object
print(DbTenantPartner.to_json())

# convert the object into a dict
db_tenant_partner_dict = db_tenant_partner_instance.to_dict()
# create an instance of DbTenantPartner from a dict
db_tenant_partner_from_dict = DbTenantPartner.from_dict(db_tenant_partner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


