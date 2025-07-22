# WhiteLabelItemArrayWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**List[WhiteLabelItemDto]**](WhiteLabelItemDto.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace-api-sdk.models.white_label_item_array_wrapper import WhiteLabelItemArrayWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of WhiteLabelItemArrayWrapper from a JSON string
white_label_item_array_wrapper_instance = WhiteLabelItemArrayWrapper.from_json(json)
# print the JSON string representation of the object
print(WhiteLabelItemArrayWrapper.to_json())

# convert the object into a dict
white_label_item_array_wrapper_dict = white_label_item_array_wrapper_instance.to_dict()
# create an instance of WhiteLabelItemArrayWrapper from a dict
white_label_item_array_wrapper_from_dict = WhiteLabelItemArrayWrapper.from_dict(white_label_item_array_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


