# FilesStatisticsResultDto
The file statistics result parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**my_documents_used_space** | [**FilesStatisticsFolder**](FilesStatisticsFolder.md) | The used space of files in the \\My Documents\\ section. | [optional] 
**trash_used_space** | [**FilesStatisticsFolder**](FilesStatisticsFolder.md) | The used space of files in the \\Trash\\ section. | [optional] 
**archive_used_space** | [**FilesStatisticsFolder**](FilesStatisticsFolder.md) | The used space of files in the \\Archive\\ section. | [optional] 
**rooms_used_space** | [**FilesStatisticsFolder**](FilesStatisticsFolder.md) | The used space of files in the \\Rooms\\ section. | [optional] 
**ai_agents_used_space** | [**FilesStatisticsFolder**](FilesStatisticsFolder.md) | The used space of files in the \\AI agents\\ section. | [optional] 
**forms_used_space** | [**FilesStatisticsFolder**](FilesStatisticsFolder.md) | The used space of files in the \\Forms\\ section. | [optional] 

## Example

```python
from docspace_api_sdk.models.files_statistics_result_dto import FilesStatisticsResultDto

# TODO update the JSON string below
json = "{}"
# create an instance of FilesStatisticsResultDto from a JSON string
files_statistics_result_dto_instance = FilesStatisticsResultDto.from_json(json)
# print the JSON string representation of the object
print(FilesStatisticsResultDto.to_json())

# convert the object into a dict
files_statistics_result_dto_dict = files_statistics_result_dto_instance.to_dict()
# create an instance of FilesStatisticsResultDto from a dict
files_statistics_result_dto_from_dict = FilesStatisticsResultDto.from_dict(files_statistics_result_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


