# DocsCloudConfigRequestDto
Represents the configuration of a Docs Connect tenant.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_name** | **str** | The tenant name. | [optional] 
**security** | [**DocsCloudSecurityConfigRequest**](DocsCloudSecurityConfigRequest.md) | The security configuration. | [optional] 
**server** | [**DocsCloudServerConfigRequest**](DocsCloudServerConfigRequest.md) | The server configuration. | [optional] 
**wopi** | [**DocsCloudWopiConfigRequest**](DocsCloudWopiConfigRequest.md) | The WOPI configuration. | [optional] 
**ip_filter** | [**DocsCloudIpFilterConfigRequest**](DocsCloudIpFilterConfigRequest.md) | The IP filter configuration. | [optional] 

## Example

```python
from docspace_api_sdk.models.docs_cloud_config_request_dto import DocsCloudConfigRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of DocsCloudConfigRequestDto from a JSON string
docs_cloud_config_request_dto_instance = DocsCloudConfigRequestDto.from_json(json)
# print the JSON string representation of the object
print(DocsCloudConfigRequestDto.to_json())

# convert the object into a dict
docs_cloud_config_request_dto_dict = docs_cloud_config_request_dto_instance.to_dict()
# create an instance of DocsCloudConfigRequestDto from a dict
docs_cloud_config_request_dto_from_dict = DocsCloudConfigRequestDto.from_dict(docs_cloud_config_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


