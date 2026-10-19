# DocsCloudIpFilterRuleDto
Represents the IP filter rule of a Docs Connect tenant.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The IP address. | [optional] 
**allowed** | **bool** | Whether the IP address is allowed. | [optional] 

## Example

```python
from docspace_api_sdk.models.docs_cloud_ip_filter_rule_dto import DocsCloudIpFilterRuleDto

# TODO update the JSON string below
json = "{}"
# create an instance of DocsCloudIpFilterRuleDto from a JSON string
docs_cloud_ip_filter_rule_dto_instance = DocsCloudIpFilterRuleDto.from_json(json)
# print the JSON string representation of the object
print(DocsCloudIpFilterRuleDto.to_json())

# convert the object into a dict
docs_cloud_ip_filter_rule_dto_dict = docs_cloud_ip_filter_rule_dto_instance.to_dict()
# create an instance of DocsCloudIpFilterRuleDto from a dict
docs_cloud_ip_filter_rule_dto_from_dict = DocsCloudIpFilterRuleDto.from_dict(docs_cloud_ip_filter_rule_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


