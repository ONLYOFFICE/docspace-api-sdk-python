# DocsCloudUserStats
Represents the usage statistics of a single DocsCloud user category (editor or viewer).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **int** | The number of active users. | [optional] 
**internal** | **int** | The number of internal users. | [optional] 
**external** | **int** | The number of external users. | [optional] 
**remaining** | **int** | The number of remaining users before the limit is reached. | [optional] 
**critical_remaining** | **bool** | Whether the number of remaining users is critically low. | [optional] 

## Example

```python
from docspace_api_sdk.models.docs_cloud_user_stats import DocsCloudUserStats

# TODO update the JSON string below
json = "{}"
# create an instance of DocsCloudUserStats from a JSON string
docs_cloud_user_stats_instance = DocsCloudUserStats.from_json(json)
# print the JSON string representation of the object
print(DocsCloudUserStats.to_json())

# convert the object into a dict
docs_cloud_user_stats_dict = docs_cloud_user_stats_instance.to_dict()
# create an instance of DocsCloudUserStats from a dict
docs_cloud_user_stats_from_dict = DocsCloudUserStats.from_dict(docs_cloud_user_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


