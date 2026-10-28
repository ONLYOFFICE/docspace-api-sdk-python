# DocsCloudServerConfigDto
Represents the server configuration of a Docs Connect tenant.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_anonymous_support** | **bool** | Whether anonymous access is supported. | [optional] 
**file_size_limit** | **int** | The maximum file size in bytes. | [optional] 

## Example

```python
from docspace_api_sdk.models.docs_cloud_server_config_dto import DocsCloudServerConfigDto

# TODO update the JSON string below
json = "{}"
# create an instance of DocsCloudServerConfigDto from a JSON string
docs_cloud_server_config_dto_instance = DocsCloudServerConfigDto.from_json(json)
# print the JSON string representation of the object
print(DocsCloudServerConfigDto.to_json())

# convert the object into a dict
docs_cloud_server_config_dto_dict = docs_cloud_server_config_dto_instance.to_dict()
# create an instance of DocsCloudServerConfigDto from a dict
docs_cloud_server_config_dto_from_dict = DocsCloudServerConfigDto.from_dict(docs_cloud_server_config_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


