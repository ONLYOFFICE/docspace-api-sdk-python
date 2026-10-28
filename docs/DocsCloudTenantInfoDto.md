# DocsCloudTenantInfoDto
Represents the license and server information of a Docs Connect tenant, with usage statistics for the current period.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**license** | [**DocsCloudLicenseInfoDto**](DocsCloudLicenseInfoDto.md) | The license information. | [optional] 
**server** | [**DocsCloudServerInfoDto**](DocsCloudServerInfoDto.md) | The Docs Connect server information. | [optional] 
**users_limit** | [**DocsCloudUsersLimitDto**](DocsCloudUsersLimitDto.md) | The user limits of the license. | [optional] 
**stats** | [**DocsCloudStatsDto**](DocsCloudStatsDto.md) | The usage statistics for the current period. | [optional] 

## Example

```python
from docspace_api_sdk.models.docs_cloud_tenant_info_dto import DocsCloudTenantInfoDto

# TODO update the JSON string below
json = "{}"
# create an instance of DocsCloudTenantInfoDto from a JSON string
docs_cloud_tenant_info_dto_instance = DocsCloudTenantInfoDto.from_json(json)
# print the JSON string representation of the object
print(DocsCloudTenantInfoDto.to_json())

# convert the object into a dict
docs_cloud_tenant_info_dto_dict = docs_cloud_tenant_info_dto_instance.to_dict()
# create an instance of DocsCloudTenantInfoDto from a dict
docs_cloud_tenant_info_dto_from_dict = DocsCloudTenantInfoDto.from_dict(docs_cloud_tenant_info_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


