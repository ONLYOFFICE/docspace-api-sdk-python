# ChangeHistoryRequest
The change to make to a revision group of a file.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **int** | The version the change applies to; 0 means the current version of the file. | 
**continue_version** | **bool** | What to do with the revision group: `false` completes the named version, storing its content again as a fresh  version that opens a new group, while `true` folds the last group back into the group before it, so the next  save continues that revision. | [optional] 

## Example

```python
from docspace_api_sdk.models.change_history_request import ChangeHistoryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeHistoryRequest from a JSON string
change_history_request_instance = ChangeHistoryRequest.from_json(json)
# print the JSON string representation of the object
print(ChangeHistoryRequest.to_json())

# convert the object into a dict
change_history_request_dict = change_history_request_instance.to_dict()
# create an instance of ChangeHistoryRequest from a dict
change_history_request_from_dict = ChangeHistoryRequest.from_dict(change_history_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


