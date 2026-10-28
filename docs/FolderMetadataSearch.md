# FolderMetadataSearch
The typed form of the metadata search of a folder: the same filter the folder listing takes in the metadataTemplateId  and metadataFilters query parameters, with the conditions as objects instead of a JSON string.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata_template_id** | **int** | The ID of the metadata template the entries must be assigned to. On its own it narrows the listing to the entries  carrying the template; together with the conditions it also pins the template the filtered fields belong to. | [optional] 
**metadata_filters** | [**List[MetadataFilterConditionRequest]**](MetadataFilterConditionRequest.md) | The metadata filter conditions, combined with AND. A custom field is addressed by its name instead of the field ID. | [optional] 
**include_hidden_metadata** | **bool** | Whether the text search, and the metadataMatches it reports, also look at the values of the hidden metadata  templates (created with visible false for the metadata a service keeps for itself, which the web client never  shows). False, the default, leaves them out, so an entry is not found by such a value; true takes them in.  metadataTemplateId and metadataFilters are not concerned: a hidden template or field named there is searched  either way. | [optional] 
**filter_value** | **str** | The text to search for in the titles and in the string metadata values of the entries, the custom fields and the  template fields alike; an entry found by its metadata says where in metadataMatches. | [optional] 
**with_sub_folders** | **bool** | Specifies whether to search the whole subtree of the folder (the default) or its direct children only. | [optional] 
**filter_type** | [**FilterType**](FilterType.md) | The filter type. | [optional] 
**count** | **int** | The number of entries to return, from 1 to 100. | [optional] 
**start_index** | **int** | The zero-based index of the first entry to return. | [optional] 
**sort_by** | **str** | The field to sort by, a name of the SortedByType values. | [optional] 
**sort_order** | [**SortOrder**](SortOrder.md) | The sort order. | [optional] 

## Example

```python
from docspace_api_sdk.models.folder_metadata_search import FolderMetadataSearch

# TODO update the JSON string below
json = "{}"
# create an instance of FolderMetadataSearch from a JSON string
folder_metadata_search_instance = FolderMetadataSearch.from_json(json)
# print the JSON string representation of the object
print(FolderMetadataSearch.to_json())

# convert the object into a dict
folder_metadata_search_dict = folder_metadata_search_instance.to_dict()
# create an instance of FolderMetadataSearch from a dict
folder_metadata_search_from_dict = FolderMetadataSearch.from_dict(folder_metadata_search_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


