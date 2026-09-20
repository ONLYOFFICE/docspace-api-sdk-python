# ThirdPartyFolderContentDto
One page of the contents of a folder or of a section: its entries split into files and folders, the folder itself,  and the counters needed to page through the rest.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**files** | [**List[FileEntryBaseDto]**](FileEntryBaseDto.md) | The file entries of this page. It is empty when the folder holds no files, when the filters matched none of  them, and in the sections that list rooms only. | [optional] 
**folders** | [**List[FileEntryBaseDto]**](FileEntryBaseDto.md) | The folder entries of this page. In a section of rooms these entries are the rooms themselves, which is where  their type, tags, logo and quota are read from. | [optional] 
**current** | [**ThirdPartyFolderDto**](ThirdPartyFolderDto.md) | The folder or section the page was read from, with its own title, type and access rights. It describes the  container, not the entries, and is filled in even when the page is empty. | [optional] 
**path_parts** | **object** |  | 
**start_index** | **int** | The position of the first entry of this page in the whole result, echoing the requested start index. Add the  number of entries received to it to ask for the next page. | [optional] 
**count** | **int** | How many entries this page carries, files and folders together. A page shorter than the requested size means  the result is exhausted. | [optional] 
**total** | **int** | How many entries matched before paging was applied, across the whole folder. Page until the start index plus  the entries received reaches it. | 
**new** | **int** | How many entries of this folder are marked as new for the caller. It is 0 for every listing when the account  has switched the new-item badges off, so a zero here does not prove that nothing has changed. | [optional] 

## Example

```python
from docspace_api_sdk.models.third_party_folder_content_dto import ThirdPartyFolderContentDto

# TODO update the JSON string below
json = "{}"
# create an instance of ThirdPartyFolderContentDto from a JSON string
third_party_folder_content_dto_instance = ThirdPartyFolderContentDto.from_json(json)
# print the JSON string representation of the object
print(ThirdPartyFolderContentDto.to_json())

# convert the object into a dict
third_party_folder_content_dto_dict = third_party_folder_content_dto_instance.to_dict()
# create an instance of ThirdPartyFolderContentDto from a dict
third_party_folder_content_dto_from_dict = ThirdPartyFolderContentDto.from_dict(third_party_folder_content_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


