# DeleteFolder
The parameters for deleting a folder.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delete_after** | **bool** | Specifies whether to delete a folder after the editing session is finished or not. | [optional] 
**immediately** | **bool** | Specifies whether to move a folder to the \\\&quot;Trash\\\&quot; folder or delete it immediately. | [optional] 

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


