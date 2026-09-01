# DocsCloudIpFilterRule
Represents the IP filter rule of a DocsCloud tenant.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The IP address. | [optional] 
**allowed** | **bool** | Whether the IP address is allowed. | [optional] 

## Example

```python
from docspace_api_sdk.models.docs_cloud_ip_filter_rule import DocsCloudIpFilterRule

# TODO update the JSON string below
json = "{}"
# create an instance of DocsCloudIpFilterRule from a JSON string
docs_cloud_ip_filter_rule_instance = DocsCloudIpFilterRule.from_json(json)
# print the JSON string representation of the object
print(DocsCloudIpFilterRule.to_json())

# convert the object into a dict
docs_cloud_ip_filter_rule_dict = docs_cloud_ip_filter_rule_instance.to_dict()
# create an instance of DocsCloudIpFilterRule from a dict
docs_cloud_ip_filter_rule_from_dict = DocsCloudIpFilterRule.from_dict(docs_cloud_ip_filter_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


