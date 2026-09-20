# TenantDto
The record of one portal: its name, owner, language, time zone and lifecycle state.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**affiliate_id** | **str** | The partner the portal was signed up through, empty for a portal that came in directly. It is bookkeeping  for the vendor and has no bearing on what the portal may do. | [optional] 
**tenant_alias** | **str** | The portal's own name within the installation, which together with the installation's base domain forms  the address it is reached at. A caller without the portal-settings right gets `tenantId` alone, so an  empty value here is the sign that the rest of this object was withheld rather than unset. | [optional] 
**calls** | **bool** | Whether telephony is switched on for the portal. It is carried over from portal registration and stays  `false` on a DocSpace portal, where the feature does not exist. | [optional] 
**campaign** | **str** | The marketing campaign the portal was signed up under, empty for a portal that came in outside one. Like  `affiliateId`, it is bookkeeping only. | [optional] 
**creation_date_time** | **datetime** | When the portal was created, in UTC rather than in the portal time zone. | [optional] [readonly] 
**hosted_region** | **str** | The data-centre region written on the portal record itself, as opposed to `region`, which is looked up  from the hosting service. It is empty on a server installation. | [optional] 
**tenant_id** | **int** | The numeric identifier of the portal inside the installation. It is the one field every caller gets,  whatever their rights. | [optional] [readonly] 
**industry** | [**TenantIndustry**](TenantIndustry.md) | The line of business chosen when the portal was created. It only steers what the vendor suggests and  restricts nothing. | [optional] 
**language** | **str** | The default language of the portal as a culture name, the same value `GET api/2.0/settings` reports as  `culture`. A member may have a language of their own, which this does not reflect. | [optional] 
**last_modified** | **datetime** | When any field of this record last changed, in UTC. It does not move when portal settings outside this  record are changed. | [optional] 
**mapped_domain** | **str** | The custom domain the portal answers on in addition to its own address, empty when none has been set up. | [optional] 
**name** | **str** | The portal title as shown to people, which is what `GET api/2.0/settings` returns as  `greetingSettings`. It is free text, unlike `tenantAlias`, and empty until someone sets it. | [optional] 
**owner_id** | **UUID** | The portal owner, the one account that cannot be removed or demoted.  `PUT api/2.0/settings/owner` hands the role over. | [optional] 
**payment_id** | **str** | The portal's identifier in the billing system, empty for a portal that has never been billed. The  subscription itself is read with `GET api/2.0/portal/tariff`. | [optional] 
**spam** | **bool** | Whether the owner agreed to receive the vendor's newsletter. Despite the name it does not mark the portal  as a spammer and affects nothing but marketing mail. | [optional] 
**status** | [**TenantStatus**](TenantStatus.md) | The lifecycle state of the portal. Anything other than active means most operations are refused for the  moment, because the portal is being transferred, restored, encrypted or removed. | [optional] 
**status_change_date** | **datetime** | When `status` last changed, in UTC. For a portal pending removal it is the moment the countdown to  deletion started. | [optional] [readonly] 
**time_zone** | **str** | The portal time zone, which is the zone the dates this API calls portal time are expressed in. It may be  stored as a Windows identifier here, while `GET api/2.0/settings` always reports the IANA form. | [optional] 
**trusted_domains** | **List[str]** | The mail domains a new member may register or be invited from without confirming the address. It is empty  whenever `trustedDomainsType` is not `Custom`. | [optional] 
**trusted_domains_raw** | **str** | The same domains as the single stored string they are kept in, separated by commas. Read  `trustedDomains` instead; this one exists because it is what the record holds. | [optional] 
**trusted_domains_type** | [**TenantTrustedDomainsType**](TenantTrustedDomainsType.md) | How the mail domains are applied: no domain trusted, every domain trusted, or only the listed ones. Only  the last of the three makes `trustedDomains` meaningful. | [optional] 
**version** | **int** | The identifier of the portal version the installation pins this portal to, which is an internal number  and not the product version string that `GET api/2.0/settings` reports as `version`. | [optional] 
**version_changed** | **datetime** | When `version` last changed, in UTC. It stays at its zero value on a portal whose version has never been  switched. | [optional] 
**region** | **str** | The data-centre region the portal is actually served from, looked up from the hosting service. It is  empty on a server installation and also whenever the installation's portal cache is switched off, so an  empty value does not mean the portal has no region - `hostedRegion` is the value from the record itself. | [optional] 

## Example

```python
from docspace_api_sdk.models.tenant_dto import TenantDto

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


