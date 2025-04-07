# FilesStatisticsResultWrapper


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**FilesStatisticsResultDto**](FilesStatisticsResultDto.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace.models.files_statistics_result_wrapper import FilesStatisticsResultWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of FilesStatisticsResultWrapper from a JSON string
files_statistics_result_wrapper_instance = FilesStatisticsResultWrapper.from_json(json)
# print the JSON string representation of the object
print(FilesStatisticsResultWrapper.to_json())

# convert the object into a dict
files_statistics_result_wrapper_dict = files_statistics_result_wrapper_instance.to_dict()
# create an instance of FilesStatisticsResultWrapper from a dict
files_statistics_result_wrapper_from_dict = FilesStatisticsResultWrapper.from_dict(files_statistics_result_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


