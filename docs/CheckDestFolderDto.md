# CheckDestFolderDto
The verdict on placing the requested files in the destination folder.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**CheckDestFolderResult**](CheckDestFolderResult.md) | Whether the destination folder accepts all of the requested files, only some of them or none at all. | [optional] 
**files** | [**List[FileEntryBaseDto]**](FileEntryBaseDto.md) | The requested files the destination accepts, each with the information it was listed under. The files it  rejects are absent, so an empty list means that none of them is accepted. | [optional] 

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


