# HistoryAction

The action performed on the file.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**MessageAction**](MessageAction.md) |  | [optional] 
**key** | **str** |  | [optional] 

## Example

```python
from docspace.models.history_action import HistoryAction

# TODO update the JSON string below
json = "{}"
# create an instance of HistoryAction from a JSON string
history_action_instance = HistoryAction.from_json(json)
# print the JSON string representation of the object
print(HistoryAction.to_json())

# convert the object into a dict
history_action_dict = history_action_instance.to_dict()
# create an instance of HistoryAction from a dict
history_action_from_dict = HistoryAction.from_dict(history_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


