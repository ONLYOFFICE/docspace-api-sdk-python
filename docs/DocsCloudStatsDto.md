# DocsCloudStatsDto
Represents the usage statistics of a Docs Connect tenant for the current period.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period_day** | **int** | The length of the statistics period in days. | [optional] 
**editor** | [**DocsCloudUserStatsDto**](DocsCloudUserStatsDto.md) | The statistics for editor users. | [optional] 
**viewer** | [**DocsCloudUserStatsDto**](DocsCloudUserStatsDto.md) | The statistics for viewer users. | [optional] 

## Example

```python
from docspace_api_sdk.models.docs_cloud_stats_dto import DocsCloudStatsDto

# TODO update the JSON string below
json = "{}"
# create an instance of DocsCloudStatsDto from a JSON string
docs_cloud_stats_dto_instance = DocsCloudStatsDto.from_json(json)
# print the JSON string representation of the object
print(DocsCloudStatsDto.to_json())

# convert the object into a dict
docs_cloud_stats_dto_dict = docs_cloud_stats_dto_instance.to_dict()
# create an instance of DocsCloudStatsDto from a dict
docs_cloud_stats_dto_from_dict = DocsCloudStatsDto.from_dict(docs_cloud_stats_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


