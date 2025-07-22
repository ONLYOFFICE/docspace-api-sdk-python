# FormsItemArrayWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**List[FormsItemDto]**](FormsItemDto.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace-api-sdk.models.forms_item_array_wrapper import FormsItemArrayWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of FormsItemArrayWrapper from a JSON string
forms_item_array_wrapper_instance = FormsItemArrayWrapper.from_json(json)
# print the JSON string representation of the object
print(FormsItemArrayWrapper.to_json())

# convert the object into a dict
forms_item_array_wrapper_dict = forms_item_array_wrapper_instance.to_dict()
# create an instance of FormsItemArrayWrapper from a dict
forms_item_array_wrapper_from_dict = FormsItemArrayWrapper.from_dict(forms_item_array_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


