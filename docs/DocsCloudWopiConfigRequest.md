# DocsCloudWopiConfigRequest
Represents the WOPI configuration of a Docs Connect tenant.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** | Whether WOPI is enabled. | [optional] 

## Example

```python
from docspace_api_sdk.models.docs_cloud_wopi_config_request import DocsCloudWopiConfigRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DocsCloudWopiConfigRequest from a JSON string
docs_cloud_wopi_config_request_instance = DocsCloudWopiConfigRequest.from_json(json)
# print the JSON string representation of the object
print(DocsCloudWopiConfigRequest.to_json())

# convert the object into a dict
docs_cloud_wopi_config_request_dict = docs_cloud_wopi_config_request_instance.to_dict()
# create an instance of DocsCloudWopiConfigRequest from a dict
docs_cloud_wopi_config_request_from_dict = DocsCloudWopiConfigRequest.from_dict(docs_cloud_wopi_config_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


