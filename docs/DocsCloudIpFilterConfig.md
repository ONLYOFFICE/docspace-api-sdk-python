# DocsCloudIpFilterConfig
Represents the IP filter configuration of a DocsCloud tenant.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rules** | [**List[DocsCloudIpFilterRule]**](DocsCloudIpFilterRule.md) | The IP filter rules. | [optional] 

## Example

```python
from docspace_api_sdk.models.docs_cloud_ip_filter_config import DocsCloudIpFilterConfig

# TODO update the JSON string below
json = "{}"
# create an instance of DocsCloudIpFilterConfig from a JSON string
docs_cloud_ip_filter_config_instance = DocsCloudIpFilterConfig.from_json(json)
# print the JSON string representation of the object
print(DocsCloudIpFilterConfig.to_json())

# convert the object into a dict
docs_cloud_ip_filter_config_dict = docs_cloud_ip_filter_config_instance.to_dict()
# create an instance of DocsCloudIpFilterConfig from a dict
docs_cloud_ip_filter_config_from_dict = DocsCloudIpFilterConfig.from_dict(docs_cloud_ip_filter_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


