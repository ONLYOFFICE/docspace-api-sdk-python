# DocsCloudUsageDto
Represents the usage statistics of a Docs Connect tenant.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**since** | **datetime** | The date and time the usage statistics are counted from. | [optional] 
**active_count** | **int** | The number of active users. | [optional] 

## Example

```python
from docspace_api_sdk.models.docs_cloud_usage_dto import DocsCloudUsageDto

# TODO update the JSON string below
json = "{}"
# create an instance of DocsCloudUsageDto from a JSON string
docs_cloud_usage_dto_instance = DocsCloudUsageDto.from_json(json)
# print the JSON string representation of the object
print(DocsCloudUsageDto.to_json())

# convert the object into a dict
docs_cloud_usage_dto_dict = docs_cloud_usage_dto_instance.to_dict()
# create an instance of DocsCloudUsageDto from a dict
docs_cloud_usage_dto_from_dict = DocsCloudUsageDto.from_dict(docs_cloud_usage_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


