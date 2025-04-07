# DbTenant


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Id | [optional] 
**name** | **str** | Name | [optional] 
**alias** | **str** | Alias | [optional] 
**mapped_domain** | **str** | Mapped domain | [optional] 
**version** | **int** | Version | [optional] 
**version_changed** | **datetime** | Version_changed | [optional] 
**version_changed** | **datetime** | Version changed | [optional] 
**language** | **str** | Language | [optional] 
**time_zone** | **str** | Time zone | [optional] 
**trusted_domains_raw** | **str** | Trusted domains raw | [optional] 
**trusted_domains_enabled** | [**TenantTrustedDomainsType**](TenantTrustedDomainsType.md) |  | [optional] 
**status** | [**TenantStatus**](TenantStatus.md) |  | [optional] 
**status_changed** | **datetime** | Status changed | [optional] 
**status_changed_hack** | **datetime** | Status changed hack | [optional] 
**creation_date_time** | **datetime** | Creation date time | [optional] 
**owner_id** | **str** | Owner id | [optional] 
**payment_id** | **str** | Payment id | [optional] 
**industry** | [**TenantIndustry**](TenantIndustry.md) |  | [optional] 
**last_modified** | **datetime** | Last modified | [optional] 
**calls** | **bool** | Calls | [optional] 
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


