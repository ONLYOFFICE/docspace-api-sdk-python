# HistoryArrayWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**List[HistoryDto]**](HistoryDto.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace-api-python.models.history_array_wrapper import HistoryArrayWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of HistoryArrayWrapper from a JSON string
history_array_wrapper_instance = HistoryArrayWrapper.from_json(json)
# print the JSON string representation of the object
print(HistoryArrayWrapper.to_json())

# convert the object into a dict
history_array_wrapper_dict = history_array_wrapper_instance.to_dict()
# create an instance of HistoryArrayWrapper from a dict
history_array_wrapper_from_dict = HistoryArrayWrapper.from_dict(history_array_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


