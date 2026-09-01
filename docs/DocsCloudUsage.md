# DocsCloudUsage
Represents the usage statistics of a DocsCloud tenant.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**since** | **datetime** | The date and time the usage statistics are counted from. | [optional] 
**active_count** | **int** | The number of active users. | [optional] 

## Example

```python
from docspace_api_sdk.models.docs_cloud_usage import DocsCloudUsage

# TODO update the JSON string below
json = "{}"
# create an instance of DocsCloudUsage from a JSON string
docs_cloud_usage_instance = DocsCloudUsage.from_json(json)
# print the JSON string representation of the object
print(DocsCloudUsage.to_json())

# convert the object into a dict
docs_cloud_usage_dict = docs_cloud_usage_instance.to_dict()
# create an instance of DocsCloudUsage from a dict
docs_cloud_usage_from_dict = DocsCloudUsage.from_dict(docs_cloud_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


