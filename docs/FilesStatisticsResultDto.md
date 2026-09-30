# FilesStatisticsResultDto
The space that stored documents take in each section of the portal, in bytes. The figures cover every account of  the portal rather than the caller alone, and a section the portal does not have comes back as null instead of a  zero figure.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**my_documents_used_space** | [**FilesStatisticsFolder**](FilesStatisticsFolder.md) | The space taken by the personal Files sections of all accounts of the portal added together. An item deleted  to the trash keeps taking space and is counted in `trashUsedSpace` until the trash is emptied. | [optional] 
**trash_used_space** | [**FilesStatisticsFolder**](FilesStatisticsFolder.md) | The space held by the items deleted to the trash from any section, which is given back only when the trash is  emptied or the items are erased for good. | [optional] 
**archive_used_space** | [**FilesStatisticsFolder**](FilesStatisticsFolder.md) | The space taken by the content of the archived rooms, the archived form filling rooms included. Restoring a  room moves its space back to `roomsUsedSpace` or `formsUsedSpace`. | [optional] 
**rooms_used_space** | [**FilesStatisticsFolder**](FilesStatisticsFolder.md) | The space taken by the content of the active rooms, except the form filling rooms, whose content is reported  in `formsUsedSpace`. Archiving a room moves its space to `archiveUsedSpace`. | [optional] 
**ai_agents_used_space** | [**FilesStatisticsFolder**](FilesStatisticsFolder.md) | The space taken by the content of the AI agents section, which exists only in a portal where the AI agents  feature is active; creating an AI room is not enough to bring the section into being. | [optional] 
**forms_used_space** | [**FilesStatisticsFolder**](FilesStatisticsFolder.md) | The space taken by the content of the active form filling rooms, which is kept apart from `roomsUsedSpace`  even though those rooms are listed among the rooms. | [optional] 

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


