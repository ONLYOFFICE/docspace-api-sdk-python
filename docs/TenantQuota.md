# TenantQuota


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **int** | Tenant ID | [optional] 
**name** | **str** | Name | [optional] 
**price** | **float** | Price | [optional] 
**price_currency_symbol** | **str** | Price currency symbol | [optional] 
**product_id** | **str** | Product ID | [optional] 
**visible** | **bool** | Specifies if the tenant quota is visible or not | [optional] 
**features** | **str** | Tenant quota features | [optional] 
**max_file_size** | **int** | Maximum file size | [optional] 
**max_total_size** | **int** | Maximum total size | [optional] 
**count_user** | **int** | Number of portal users | [optional] 
**count_room_admin** | **int** | Number of portal room administrators | [optional] 
**users_in_room** | **int** | Number of room users | [optional] 
**count_room** | **int** | Number of rooms | [optional] 
**non_profit** | **bool** | Specifies if the tenant quota is nonprofit or not | [optional] 
**trial** | **bool** | Specifies if the tenant quota is trial or not | [optional] 
**free** | **bool** | Specifies if the tenant quota is free or not | [optional] 
**update** | **bool** | Specifies if the tenant quota is updated or not | [optional] 
**audit** | **bool** | Specifies if the audit trail is available or not | [optional] 
**docs_edition** | **bool** | Specifies if this tenant quota is Docs edition or not | [optional] 
**ldap** | **bool** | Specifies if the LDAP settings are available or not | [optional] 
**sso** | **bool** | Specifies if the SSO settings are available or not | [optional] 
**statistic** | **bool** | Specifies if the statistic settings are available or not | [optional] 
**branding** | **bool** | Specifies if the branding settings are available or not | [optional] 
**customization** | **bool** | Specifies if the customization settings are available or not | [optional] 
**lifetime** | **bool** | Specifies if the license is lifetime or not | [optional] 
**custom** | **bool** | Specifies if the custom domain URL is available or not | [optional] 
**auto_backup_restore** | **bool** | Specifies if the automatic Backup&amp;Restore feature is available or not | [optional] 
**oauth** | **bool** | Specifies if Oauth is available or not | [optional] 
**content_search** | **bool** | Specifies if the content search is available or not | [optional] 
**third_party** | **bool** | Specifies if the third-party accounts linking is available or not | [optional] 
**year** | **bool** | Specifies if the tenant quota is yearly subscription or not | [optional] 

## Example

```python
from docspace.models.tenant_quota import TenantQuota

# TODO update the JSON string below
json = "{}"
# create an instance of TenantQuota from a JSON string
tenant_quota_instance = TenantQuota.from_json(json)
# print the JSON string representation of the object
print(TenantQuota.to_json())

# convert the object into a dict
tenant_quota_dict = tenant_quota_instance.to_dict()
# create an instance of TenantQuota from a dict
tenant_quota_from_dict = TenantQuota.from_dict(tenant_quota_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


