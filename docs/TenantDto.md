# TenantDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affiliate_id** | **str** | Affiliate ID | [optional] 
**tenant_alias** | **str** | Tenant alias | [optional] 
**calls** | **bool** | Specifies if the calls are available for this tenant or not | [optional] 
**campaign** | **str** | Campaign | [optional] 
**creation_date_time** | **datetime** | Creation date and time | [optional] [readonly] 
**hosted_region** | **str** | Hosted region | [optional] 
**tenant_id** | **int** | Tenant ID | [optional] [readonly] 
**industry** | [**TenantIndustry**](TenantIndustry.md) |  | [optional] 
**language** | **str** | Language | [optional] 
**last_modified** | **datetime** | Last modified date | [optional] 
**mapped_domain** | **str** | Mapped domain | [optional] 
**name** | **str** | Name | [optional] 
**owner_id** | **str** | Owner ID | [optional] 
**payment_id** | **str** | Payment ID | [optional] 
**spam** | **bool** | Specifies if the ONLYOFFICE newsletter is allowed or not | [optional] 
**status** | [**TenantStatus**](TenantStatus.md) |  | [optional] 
**status_change_date** | **datetime** | The date and time when the tenant status was changed | [optional] [readonly] 
**time_zone** | **str** | Time zone | [optional] 
**trusted_domains** | **List[str]** | List of trusted domains | [optional] 
**trusted_domains_raw** | **str** | Trusted domains in the string format | [optional] 
**trusted_domains_type** | [**TenantTrustedDomainsType**](TenantTrustedDomainsType.md) |  | [optional] 
**version** | **int** | Version | [optional] 
**version_changed** | **datetime** | The date and time when the tenant version was changed | [optional] 
**region** | **str** | AWS region | [optional] 

## Example

```python
from docspace.models.tenant_dto import TenantDto

# TODO update the JSON string below
json = "{}"
# create an instance of TenantDto from a JSON string
tenant_dto_instance = TenantDto.from_json(json)
# print the JSON string representation of the object
print(TenantDto.to_json())

# convert the object into a dict
tenant_dto_dict = tenant_dto_instance.to_dict()
# create an instance of TenantDto from a dict
tenant_dto_from_dict = TenantDto.from_dict(tenant_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


