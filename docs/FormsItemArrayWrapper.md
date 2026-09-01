# FormsItemArrayWrapper
The successful API response containing the list of FormsItemDto objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**List[FormsItemDto]**](FormsItemDto.md) | The list of FormsItemDto objects returned by the operation. | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.forms_item_array_wrapper import FormsItemArrayWrapper

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


