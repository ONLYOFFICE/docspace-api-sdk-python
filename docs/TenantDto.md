# TenantDto
The tenant parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affiliate_id** | **str** | The affiliate ID. | [optional] 
**tenant_alias** | **str** | The tenant alias. | [optional] 
**calls** | **bool** | Specifies if the calls are available for this tenant or not. | [optional] 
**campaign** | **str** | The tenant campaign. | [optional] 
**creation_date_time** | **datetime** | The tenant creation date and time. | [optional] [readonly] 
**hosted_region** | **str** | The hosted region. | [optional] 
**tenant_id** | **int** | The tenant ID. | [optional] [readonly] 
**industry** | [**TenantIndustry**](TenantIndustry.md) |  | [optional] 
**language** | **str** | The tenant language. | [optional] 
**last_modified** | **datetime** | The date and time when the tenant was last modified. | [optional] 
**mapped_domain** | **str** | The tenant mapped domain. | [optional] 
**name** | **str** | The tenant name. | [optional] 
**owner_id** | **str** | The tenant owner ID. | [optional] 
**payment_id** | **str** | The tenant payment ID. | [optional] 
**spam** | **bool** | Specifies if the ONLYOFFICE newsletter is allowed or not. | [optional] 
**status** | [**TenantStatus**](TenantStatus.md) |  | [optional] 
**status_change_date** | **datetime** | The date and time when the tenant status was changed. | [optional] [readonly] 
**time_zone** | **str** | The tenant time zone. | [optional] 
**trusted_domains** | **List[str]** | The list of tenant trusted domains. | [optional] 
**trusted_domains_raw** | **str** | The tenant trusted domains in the string format. | [optional] 
**trusted_domains_type** | [**TenantTrustedDomainsType**](TenantTrustedDomainsType.md) |  | [optional] 
**version** | **int** | The tenant version | [optional] 
**version_changed** | **datetime** | The date and time when the tenant version was changed. | [optional] 
**region** | **str** | The tenant AWS region. | [optional] 

## Example

```python
from docspace-api-sdk.models.tenant_dto import TenantDto

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


