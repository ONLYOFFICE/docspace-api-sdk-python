# FolderContentDtoInteger


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**files** | [**List[FileEntryDto]**](FileEntryDto.md) | List of files | [optional] 
**folders** | [**List[FileEntryDto]**](FileEntryDto.md) | List of folders | [optional] 
**current** | [**FolderDtoInteger**](FolderDtoInteger.md) |  | [optional] 
**path_parts** | **object** | Folder path | [optional] 
**start_index** | **int** | Folder start index | [optional] 
**count** | **int** | Number of folder elements | [optional] 
**total** | **int** | Total number of elements in the folder | [optional] 
**new** | **int** | New element index | [optional] 

## Example

```python
from docspace.models.folder_content_dto_integer import FolderContentDtoInteger

# TODO update the JSON string below
json = "{}"
# create an instance of FolderContentDtoInteger from a JSON string
folder_content_dto_integer_instance = FolderContentDtoInteger.from_json(json)
# print the JSON string representation of the object
print(FolderContentDtoInteger.to_json())

# convert the object into a dict
folder_content_dto_integer_dict = folder_content_dto_integer_instance.to_dict()
# create an instance of FolderContentDtoInteger from a dict
folder_content_dto_integer_from_dict = FolderContentDtoInteger.from_dict(folder_content_dto_integer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


