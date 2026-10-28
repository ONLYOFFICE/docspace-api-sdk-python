# DocsCloudIpFilterRuleRequest
Represents the IP filter rule of a Docs Connect tenant.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The IP address. | [optional] 
**allowed** | **bool** | Whether the IP address is allowed. | [optional] 

## Example

```python
from docspace_api_sdk.models.docs_cloud_ip_filter_rule_request import DocsCloudIpFilterRuleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DocsCloudIpFilterRuleRequest from a JSON string
docs_cloud_ip_filter_rule_request_instance = DocsCloudIpFilterRuleRequest.from_json(json)
# print the JSON string representation of the object
print(DocsCloudIpFilterRuleRequest.to_json())

# convert the object into a dict
docs_cloud_ip_filter_rule_request_dict = docs_cloud_ip_filter_rule_request_instance.to_dict()
# create an instance of DocsCloudIpFilterRuleRequest from a dict
docs_cloud_ip_filter_rule_request_from_dict = DocsCloudIpFilterRuleRequest.from_dict(docs_cloud_ip_filter_rule_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


