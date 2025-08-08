# CheckDestFolderDto
The destination folder checking information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**CheckDestFolderResult**](CheckDestFolderResult.md) |  | [optional] 
**files** | [**List[FileEntryBaseDto]**](FileEntryBaseDto.md) | The list of files of the destination folder. | [optional] 

## Example

```python
from docspace_api_sdk.models.check_dest_folder_dto import CheckDestFolderDto

# TODO update the JSON string below
json = "{}"
# create an instance of CheckDestFolderDto from a JSON string
check_dest_folder_dto_instance = CheckDestFolderDto.from_json(json)
# print the JSON string representation of the object
print(CheckDestFolderDto.to_json())

# convert the object into a dict
check_dest_folder_dto_dict = check_dest_folder_dto_instance.to_dict()
# create an instance of CheckDestFolderDto from a dict
check_dest_folder_dto_from_dict = CheckDestFolderDto.from_dict(check_dest_folder_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


