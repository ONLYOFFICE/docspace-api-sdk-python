# DbTenantPartner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **int** | Tenant id | [optional] 
**partner_id** | **str** | Partner id | [optional] 
**affiliate_id** | **str** | Affiliate id | [optional] 
**campaign** | **str** | Campaign | [optional] 

## Example

```python
from docspace.models.db_tenant_partner import DbTenantPartner

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


