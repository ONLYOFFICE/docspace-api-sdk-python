# DocsCloudSecurityConfigDto
Represents the security configuration of a Docs Connect tenant.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secret** | **str** | The security secret. | [optional] 
**header** | **str** | The security header name. | [optional] 

## Example

```python
from docspace_api_sdk.models.docs_cloud_security_config_dto import DocsCloudSecurityConfigDto

# TODO update the JSON string below
json = "{}"
# create an instance of DocsCloudSecurityConfigDto from a JSON string
docs_cloud_security_config_dto_instance = DocsCloudSecurityConfigDto.from_json(json)
# print the JSON string representation of the object
print(DocsCloudSecurityConfigDto.to_json())

# convert the object into a dict
docs_cloud_security_config_dto_dict = docs_cloud_security_config_dto_instance.to_dict()
# create an instance of DocsCloudSecurityConfigDto from a dict
docs_cloud_security_config_dto_from_dict = DocsCloudSecurityConfigDto.from_dict(docs_cloud_security_config_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


