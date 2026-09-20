# DeleteFolder
How a folder is to be deleted.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delete_after** | **bool** | Whether the deletion waits for the editing sessions on the contents to end: with true a folder somebody is  working in is removed once they are done, with false the deletion starts at once. | [optional] 
**immediately** | **bool** | Whether the folder is discarded for good instead of being moved to the Trash section: with false it can be  restored from Trash, with true it cannot be recovered. Inside a room there is no Trash and the deletion is  final either way. | [optional] 

## Example

```python
from docspace_api_sdk.models.delete_folder import DeleteFolder

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteFolder from a JSON string
delete_folder_instance = DeleteFolder.from_json(json)
# print the JSON string representation of the object
print(DeleteFolder.to_json())

# convert the object into a dict
delete_folder_dict = delete_folder_instance.to_dict()
# create an instance of DeleteFolder from a dict
delete_folder_from_dict = DeleteFolder.from_dict(delete_folder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


