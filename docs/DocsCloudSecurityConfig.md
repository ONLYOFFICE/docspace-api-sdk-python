# DocsCloudSecurityConfig
Represents the security configuration of a DocsCloud tenant.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secret** | **str** | The security secret. | [optional] 
**header** | **str** | The security header name. | [optional] 

## Example

```python
from docspace_api_sdk.models.docs_cloud_security_config import DocsCloudSecurityConfig

# TODO update the JSON string below
json = "{}"
# create an instance of DocsCloudSecurityConfig from a JSON string
docs_cloud_security_config_instance = DocsCloudSecurityConfig.from_json(json)
# print the JSON string representation of the object
print(DocsCloudSecurityConfig.to_json())

# convert the object into a dict
docs_cloud_security_config_dict = docs_cloud_security_config_instance.to_dict()
# create an instance of DocsCloudSecurityConfig from a dict
docs_cloud_security_config_from_dict = DocsCloudSecurityConfig.from_dict(docs_cloud_security_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


