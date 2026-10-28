# DeleteFolderRequest
How a folder is to be deleted.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delete_after** | **bool** | Whether the deletion waits for the editing sessions on the contents to end: with true a folder somebody is  working in is removed once they are done, with false the deletion starts at once. | [optional] 
**immediately** | **bool** | Whether the folder is discarded for good instead of being moved to the Trash section: with false it can be  restored from Trash, with true it cannot be recovered. Inside a room there is no Trash and the deletion is  final either way. | [optional] 

## Example

```python
from docspace_api_sdk.models.delete_folder_request import DeleteFolderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteFolderRequest from a JSON string
delete_folder_request_instance = DeleteFolderRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteFolderRequest.to_json())

# convert the object into a dict
delete_folder_request_dict = delete_folder_request_instance.to_dict()
# create an instance of DeleteFolderRequest from a dict
delete_folder_request_from_dict = DeleteFolderRequest.from_dict(delete_folder_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


