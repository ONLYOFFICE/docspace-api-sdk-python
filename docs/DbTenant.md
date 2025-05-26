# DbTenant

The database tenant parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The tenant ID. | [optional] 
**name** | **str** | The tenant name. | [optional] 
**alias** | **str** | The tenant alias. | [optional] 
**mapped_domain** | **str** | Mapped domain | [optional] 
**version** | **int** | The tenant version. | [optional] 
**version_changed** | **datetime** | The Version_changed field. | [optional] 
**version_changed** | **datetime** | The date and time when the version was changed. | [optional] 
**language** | **str** | The tenant language. | [optional] 
**time_zone** | **str** | The tenant time zone. | [optional] 
**trusted_domains_raw** | **str** | The tenant trusted domains raw. | [optional] 
**trusted_domains_enabled** | [**TenantTrustedDomainsType**](TenantTrustedDomainsType.md) |  | [optional] 
**status** | [**TenantStatus**](TenantStatus.md) |  | [optional] 
**status_changed** | **datetime** | The date and time when the tenant status was changed. | [optional] 
**status_changed_hack** | **datetime** | The hacked date and time when the tenant status was changed. | [optional] 
**creation_date_time** | **datetime** | The tenant creation date. | [optional] 
**owner_id** | **str** | The tenant owner ID. | [optional] 
**payment_id** | **str** | The tenant payment ID. | [optional] 
**industry** | [**TenantIndustry**](TenantIndustry.md) |  | [optional] 
**last_modified** | **datetime** | The date and time when the tenant was last modified. | [optional] 
**calls** | **bool** | Specifies if the calls are available for the current tenant or not. | [optional] 
**partner** | [**DbTenantPartner**](DbTenantPartner.md) |  | [optional] 

## Example

```python
from docspace.models.db_tenant import DbTenant

# TODO update the JSON string below
json = "{}"
# create an instance of DbTenant from a JSON string
db_tenant_instance = DbTenant.from_json(json)
# print the JSON string representation of the object
print(DbTenant.to_json())

# convert the object into a dict
db_tenant_dict = db_tenant_instance.to_dict()
# create an instance of DbTenant from a dict
db_tenant_from_dict = DbTenant.from_dict(db_tenant_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


