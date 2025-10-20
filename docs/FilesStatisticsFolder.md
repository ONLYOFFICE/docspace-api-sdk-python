# FilesStatisticsFolder
The file statictics folder parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The folder title. | [optional] 
**used_space** | **int** | The used space in the folder. | [optional] 

## Example

```python
from docspace_api_sdk.models.files_statistics_folder import FilesStatisticsFolder

# TODO update the JSON string below
json = "{}"
# create an instance of FilesStatisticsFolder from a JSON string
files_statistics_folder_instance = FilesStatisticsFolder.from_json(json)
# print the JSON string representation of the object
print(FilesStatisticsFolder.to_json())

# convert the object into a dict
files_statistics_folder_dict = files_statistics_folder_instance.to_dict()
# create an instance of FilesStatisticsFolder from a dict
files_statistics_folder_from_dict = FilesStatisticsFolder.from_dict(files_statistics_folder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


