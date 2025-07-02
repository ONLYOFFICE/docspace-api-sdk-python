# EditHistoryArrayWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**List[EditHistoryDto]**](EditHistoryDto.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace-api-python.models.edit_history_array_wrapper import EditHistoryArrayWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of EditHistoryArrayWrapper from a JSON string
edit_history_array_wrapper_instance = EditHistoryArrayWrapper.from_json(json)
# print the JSON string representation of the object
print(EditHistoryArrayWrapper.to_json())

# convert the object into a dict
edit_history_array_wrapper_dict = edit_history_array_wrapper_instance.to_dict()
# create an instance of EditHistoryArrayWrapper from a dict
edit_history_array_wrapper_from_dict = EditHistoryArrayWrapper.from_dict(edit_history_array_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


