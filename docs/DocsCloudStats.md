# DocsCloudStats
Represents the usage statistics of a DocsCloud tenant for the current period.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period_day** | **int** | The length of the statistics period in days. | [optional] 
**editor** | [**DocsCloudUserStats**](DocsCloudUserStats.md) | The statistics for editor users. | [optional] 
**viewer** | [**DocsCloudUserStats**](DocsCloudUserStats.md) | The statistics for viewer users. | [optional] 

## Example

```python
from docspace_api_sdk.models.docs_cloud_stats import DocsCloudStats

# TODO update the JSON string below
json = "{}"
# create an instance of DocsCloudStats from a JSON string
docs_cloud_stats_instance = DocsCloudStats.from_json(json)
# print the JSON string representation of the object
print(DocsCloudStats.to_json())

# convert the object into a dict
docs_cloud_stats_dict = docs_cloud_stats_instance.to_dict()
# create an instance of DocsCloudStats from a dict
docs_cloud_stats_from_dict = DocsCloudStats.from_dict(docs_cloud_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


