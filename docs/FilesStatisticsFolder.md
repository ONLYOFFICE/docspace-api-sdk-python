# FilesStatisticsFolder
One section of the portal and the space its documents take.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The name of the section as the interface shows it, translated into the language used by the caller, so it  suits display but not matching - which section an entry describes is told by the field that carries it. | [optional] 
**used_space** | **int** | The size of the files kept in the section, in bytes, counting every folder and room inside it; 0 means the  section holds nothing. The counter is brought up to date as an operation finishes, so a reading taken right  after an upload or a delete can still show the previous value. | [optional] 

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


