# DocsCloudSecurityConfigRequest
Represents the security configuration of a Docs Connect tenant.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secret** | **str** | The security secret. | [optional] 
**header** | **str** | The security header name. | [optional] 

## Example

```python
from docspace_api_sdk.models.docs_cloud_security_config_request import DocsCloudSecurityConfigRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DocsCloudSecurityConfigRequest from a JSON string
docs_cloud_security_config_request_instance = DocsCloudSecurityConfigRequest.from_json(json)
# print the JSON string representation of the object
print(DocsCloudSecurityConfigRequest.to_json())

# convert the object into a dict
docs_cloud_security_config_request_dict = docs_cloud_security_config_request_instance.to_dict()
# create an instance of DocsCloudSecurityConfigRequest from a dict
docs_cloud_security_config_request_from_dict = DocsCloudSecurityConfigRequest.from_dict(docs_cloud_security_config_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


