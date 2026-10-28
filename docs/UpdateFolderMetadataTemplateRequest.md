# UpdateFolderMetadataTemplateRequest
The new state of a template assignment on a folder: whether the template cascades to the content of the folder and how.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cascade** | **bool** | Whether the template cascades from the folder to the folders and files below it: true turns the cascade on,  false turns it off while the template stays on the folder. | [optional] 
**conflict_resolve_type** | [**MetadataConflictResolveType**](MetadataConflictResolveType.md) | How the cascade treats a value an entry below already holds. | [optional] 

## Example

```python
from docspace_api_sdk.models.update_folder_metadata_template_request import UpdateFolderMetadataTemplateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateFolderMetadataTemplateRequest from a JSON string
update_folder_metadata_template_request_instance = UpdateFolderMetadataTemplateRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateFolderMetadataTemplateRequest.to_json())

# convert the object into a dict
update_folder_metadata_template_request_dict = update_folder_metadata_template_request_instance.to_dict()
# create an instance of UpdateFolderMetadataTemplateRequest from a dict
update_folder_metadata_template_request_from_dict = UpdateFolderMetadataTemplateRequest.from_dict(update_folder_metadata_template_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


