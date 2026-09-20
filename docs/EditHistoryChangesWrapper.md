# EditHistoryChangesWrapper
One single change inside a saved revision of a file.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**EditHistoryAuthor**](EditHistoryAuthor.md) | The account that made this change, as the editing service reported it; an account it could not name is  reported as a guest. | [optional] 
**created** | [**ApiDateTime**](ApiDateTime.md) | When this change was made, written with the offset of the portal's time zone rather than as plain UTC. | [optional] 
**document_sha256** | **str** | The SHA-256 hash of the document as it stood after this change, where the editing service recorded one, so  that a client can check a stored copy against the change it claims to hold. Empty when the change record  carries no hash. | [optional] 

## Example

```python
from docspace_api_sdk.models.edit_history_changes_wrapper import EditHistoryChangesWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of EditHistoryChangesWrapper from a JSON string
edit_history_changes_wrapper_instance = EditHistoryChangesWrapper.from_json(json)
# print the JSON string representation of the object
print(EditHistoryChangesWrapper.to_json())

# convert the object into a dict
edit_history_changes_wrapper_dict = edit_history_changes_wrapper_instance.to_dict()
# create an instance of EditHistoryChangesWrapper from a dict
edit_history_changes_wrapper_from_dict = EditHistoryChangesWrapper.from_dict(edit_history_changes_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


