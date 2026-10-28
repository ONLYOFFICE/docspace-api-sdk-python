# DocsCloudConfigDto
Represents the configuration of a Docs Connect tenant.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_name** | **str** | The tenant name. | [optional] 
**security** | [**DocsCloudSecurityConfigDto**](DocsCloudSecurityConfigDto.md) | The security configuration. | [optional] 
**server** | [**DocsCloudServerConfigDto**](DocsCloudServerConfigDto.md) | The server configuration. | [optional] 
**wopi** | [**DocsCloudWopiConfigDto**](DocsCloudWopiConfigDto.md) | The WOPI configuration. | [optional] 
**ip_filter** | [**DocsCloudIpFilterConfigDto**](DocsCloudIpFilterConfigDto.md) | The IP filter configuration. | [optional] 

## Example

```python
from docspace_api_sdk.models.docs_cloud_config_dto import DocsCloudConfigDto

# TODO update the JSON string below
json = "{}"
# create an instance of DocsCloudConfigDto from a JSON string
docs_cloud_config_dto_instance = DocsCloudConfigDto.from_json(json)
# print the JSON string representation of the object
print(DocsCloudConfigDto.to_json())

# convert the object into a dict
docs_cloud_config_dto_dict = docs_cloud_config_dto_instance.to_dict()
# create an instance of DocsCloudConfigDto from a dict
docs_cloud_config_dto_from_dict = DocsCloudConfigDto.from_dict(docs_cloud_config_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


