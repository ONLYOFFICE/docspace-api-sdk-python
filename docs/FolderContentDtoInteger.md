# FolderContentDtoInteger
The folder content information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**files** | [**List[FileEntryBaseDto]**](FileEntryBaseDto.md) | The list of files in the folder. | [optional] 
**folders** | [**List[FileEntryBaseDto]**](FileEntryBaseDto.md) | The list of folders in the folder. | [optional] 
**current** | [**FolderDtoInteger**](FolderDtoInteger.md) |  | [optional] 
**path_parts** | **object** | The folder path. | [optional] 
**start_index** | **int** | The folder start index. | [optional] 
**count** | **int** | The number of folder elements. | [optional] 
**total** | **int** | The total number of elements in the folder. | [optional] 
**new** | **int** | The new element index in the folder. | [optional] 

## Example

```python
from docspace_api_sdk.models.folder_content_dto_integer import FolderContentDtoInteger

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


