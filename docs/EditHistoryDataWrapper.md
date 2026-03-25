# EditHistoryDataWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**EditHistoryDataDto**](EditHistoryDataDto.md) |  | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.edit_history_data_wrapper import EditHistoryDataWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of EditHistoryDataWrapper from a JSON string
edit_history_data_wrapper_instance = EditHistoryDataWrapper.from_json(json)
# print the JSON string representation of the object
print(EditHistoryDataWrapper.to_json())

# convert the object into a dict
edit_history_data_wrapper_dict = edit_history_data_wrapper_instance.to_dict()
# create an instance of EditHistoryDataWrapper from a dict
edit_history_data_wrapper_from_dict = EditHistoryDataWrapper.from_dict(edit_history_data_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


