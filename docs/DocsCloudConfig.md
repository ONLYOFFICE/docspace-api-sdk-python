# DocsCloudConfig
Represents the configuration of a DocsCloud tenant.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_name** | **str** | The tenant name. | [optional] 
**security** | [**DocsCloudSecurityConfig**](DocsCloudSecurityConfig.md) | The security configuration. | [optional] 
**server** | [**DocsCloudServerConfig**](DocsCloudServerConfig.md) | The server configuration. | [optional] 
**wopi** | [**DocsCloudWopiConfig**](DocsCloudWopiConfig.md) | The WOPI configuration. | [optional] 
**ip_filter** | [**DocsCloudIpFilterConfig**](DocsCloudIpFilterConfig.md) | The IP filter configuration. | [optional] 

## Example

```python
from docspace_api_sdk.models.docs_cloud_config import DocsCloudConfig

# TODO update the JSON string below
json = "{}"
# create an instance of DocsCloudConfig from a JSON string
docs_cloud_config_instance = DocsCloudConfig.from_json(json)
# print the JSON string representation of the object
print(DocsCloudConfig.to_json())

# convert the object into a dict
docs_cloud_config_dict = docs_cloud_config_instance.to_dict()
# create an instance of DocsCloudConfig from a dict
docs_cloud_config_from_dict = DocsCloudConfig.from_dict(docs_cloud_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


