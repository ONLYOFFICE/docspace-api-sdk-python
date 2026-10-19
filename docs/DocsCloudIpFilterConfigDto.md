# DocsCloudIpFilterConfigDto
Represents the IP filter configuration of a Docs Connect tenant.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rules** | [**List[DocsCloudIpFilterRuleDto]**](DocsCloudIpFilterRuleDto.md) | The IP filter rules. | [optional] 

## Example

```python
from docspace_api_sdk.models.docs_cloud_ip_filter_config_dto import DocsCloudIpFilterConfigDto

# TODO update the JSON string below
json = "{}"
# create an instance of DocsCloudIpFilterConfigDto from a JSON string
docs_cloud_ip_filter_config_dto_instance = DocsCloudIpFilterConfigDto.from_json(json)
# print the JSON string representation of the object
print(DocsCloudIpFilterConfigDto.to_json())

# convert the object into a dict
docs_cloud_ip_filter_config_dto_dict = docs_cloud_ip_filter_config_dto_instance.to_dict()
# create an instance of DocsCloudIpFilterConfigDto from a dict
docs_cloud_ip_filter_config_dto_from_dict = DocsCloudIpFilterConfigDto.from_dict(docs_cloud_ip_filter_config_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


