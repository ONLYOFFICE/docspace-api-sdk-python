# Delete
The parameters of a single file deletion.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delete_after** | **bool** | When to delete: `true` waits until the editing session on the file has ended, `false` deletes at once, pulling  the file away from whoever is working on it. | [optional] 
**immediately** | **bool** | Where the file goes: `false` moves it to Trash, from where it can be restored, `true` deletes it for good.  Inside a room, where there is no Trash, deletion is always final. | [optional] 

## Example

```python
from docspace_api_sdk.models.delete import Delete

# TODO update the JSON string below
json = "{}"
# create an instance of Delete from a JSON string
delete_instance = Delete.from_json(json)
# print the JSON string representation of the object
print(Delete.to_json())

# convert the object into a dict
delete_dict = delete_instance.to_dict()
# create an instance of Delete from a dict
delete_from_dict = Delete.from_dict(delete_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


