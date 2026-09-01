# DocsCloudTenantInfo
Represents the license and server information of a DocsCloud tenant, with usage statistics for the current period.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**license** | [**DocsCloudLicenseInfo**](DocsCloudLicenseInfo.md) | The license information. | [optional] 
**server** | [**DocsCloudServerInfo**](DocsCloudServerInfo.md) | The DocsCloud server information. | [optional] 
**users_limit** | [**DocsCloudUsersLimit**](DocsCloudUsersLimit.md) | The user limits of the license. | [optional] 
**stats** | [**DocsCloudStats**](DocsCloudStats.md) | The usage statistics for the current period. | [optional] 

## Example

```python
from docspace_api_sdk.models.docs_cloud_tenant_info import DocsCloudTenantInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DocsCloudTenantInfo from a JSON string
docs_cloud_tenant_info_instance = DocsCloudTenantInfo.from_json(json)
# print the JSON string representation of the object
print(DocsCloudTenantInfo.to_json())

# convert the object into a dict
docs_cloud_tenant_info_dict = docs_cloud_tenant_info_instance.to_dict()
# create an instance of DocsCloudTenantInfo from a dict
docs_cloud_tenant_info_from_dict = DocsCloudTenantInfo.from_dict(docs_cloud_tenant_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


