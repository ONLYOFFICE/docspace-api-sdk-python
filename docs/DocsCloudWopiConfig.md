# DocsCloudWopiConfig
Represents the WOPI configuration of a DocsCloud tenant.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** | Whether WOPI is enabled. | [optional] 

## Example

```python
from docspace_api_sdk.models.docs_cloud_wopi_config import DocsCloudWopiConfig

# TODO update the JSON string below
json = "{}"
# create an instance of DocsCloudWopiConfig from a JSON string
docs_cloud_wopi_config_instance = DocsCloudWopiConfig.from_json(json)
# print the JSON string representation of the object
print(DocsCloudWopiConfig.to_json())

# convert the object into a dict
docs_cloud_wopi_config_dict = docs_cloud_wopi_config_instance.to_dict()
# create an instance of DocsCloudWopiConfig from a dict
docs_cloud_wopi_config_from_dict = DocsCloudWopiConfig.from_dict(docs_cloud_wopi_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


