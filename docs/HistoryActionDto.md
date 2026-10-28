# HistoryActionDto
The action performed on the file.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**MessageAction**](MessageAction.md) | The action performed on the file. | [optional] 
**key** | **str** | The same action as a camel-case key, for a client to look up its own wording by. | [optional] 

## Example

```python
from docspace_api_sdk.models.history_action_dto import HistoryActionDto

# TODO update the JSON string below
json = "{}"
# create an instance of HistoryActionDto from a JSON string
history_action_dto_instance = HistoryActionDto.from_json(json)
# print the JSON string representation of the object
print(HistoryActionDto.to_json())

# convert the object into a dict
history_action_dto_dict = history_action_dto_instance.to_dict()
# create an instance of HistoryActionDto from a dict
history_action_dto_from_dict = HistoryActionDto.from_dict(history_action_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


