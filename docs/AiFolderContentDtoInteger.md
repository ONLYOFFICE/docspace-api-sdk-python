# AiFolderContentDtoInteger
The folder content information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**files** | [**List[AiFileEntryBaseDto]**](AiFileEntryBaseDto.md) | The list of files in the folder. | [optional] 
**folders** | [**List[AiFileEntryBaseDto]**](AiFileEntryBaseDto.md) | The list of folders in the folder. | [optional] 
**current** | [**AiFolderDtoInteger**](AiFolderDtoInteger.md) | The current folder information. | [optional] 
**path_parts** | **object** |  | 
**start_index** | **int** | The folder start index. | [optional] 
**count** | **int** | The number of folder elements. | [optional] 
**total** | **int** | The total number of elements in the folder. | 
**new** | **int** | The new element index in the folder. | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_folder_content_dto_integer import AiFolderContentDtoInteger

# TODO update the JSON string below
json = "{}"
# create an instance of AiFolderContentDtoInteger from a JSON string
ai_folder_content_dto_integer_instance = AiFolderContentDtoInteger.from_json(json)
# print the JSON string representation of the object
print(AiFolderContentDtoInteger.to_json())

# convert the object into a dict
ai_folder_content_dto_integer_dict = ai_folder_content_dto_integer_instance.to_dict()
# create an instance of AiFolderContentDtoInteger from a dict
ai_folder_content_dto_integer_from_dict = AiFolderContentDtoInteger.from_dict(ai_folder_content_dto_integer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


