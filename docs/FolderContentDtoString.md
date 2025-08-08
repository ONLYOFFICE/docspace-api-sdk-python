# FolderContentDtoString
The folder content information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**files** | [**List[FileEntryBaseDto]**](FileEntryBaseDto.md) | The list of files in the folder. | [optional] 
**folders** | [**List[FileEntryBaseDto]**](FileEntryBaseDto.md) | The list of folders in the folder. | [optional] 
**current** | [**FolderDtoString**](FolderDtoString.md) |  | [optional] 
**path_parts** | **object** | The folder path. | [optional] 
**start_index** | **int** | The folder start index. | [optional] 
**count** | **int** | The number of folder elements. | [optional] 
**total** | **int** | The total number of elements in the folder. | [optional] 
**new** | **int** | The new element index in the folder. | [optional] 

## Example

```python
from docspace_api_sdk.models.folder_content_dto_string import FolderContentDtoString

# TODO update the JSON string below
json = "{}"
# create an instance of FolderContentDtoString from a JSON string
folder_content_dto_string_instance = FolderContentDtoString.from_json(json)
# print the JSON string representation of the object
print(FolderContentDtoString.to_json())

# convert the object into a dict
folder_content_dto_string_dict = folder_content_dto_string_instance.to_dict()
# create an instance of FolderContentDtoString from a dict
folder_content_dto_string_from_dict = FolderContentDtoString.from_dict(folder_content_dto_string_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


