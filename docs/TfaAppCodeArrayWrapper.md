# TfaAppCodeArrayWrapper
The successful API response containing the list of TfaAppCodeDto objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**List[TfaAppCodeDto]**](TfaAppCodeDto.md) | The list of TfaAppCodeDto objects returned by the operation. | [optional] 
**count** | **int** | How many items this response carries: the length of the page for a list, 1 for a single object | [optional] 
**total** | **int** | How many items the whole list holds across all pages, for working out how many pages to request. Sent only by the operations that page their results, and left out of every other response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.tfa_app_code_array_wrapper import TfaAppCodeArrayWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of TfaAppCodeArrayWrapper from a JSON string
tfa_app_code_array_wrapper_instance = TfaAppCodeArrayWrapper.from_json(json)
# print the JSON string representation of the object
print(TfaAppCodeArrayWrapper.to_json())

# convert the object into a dict
tfa_app_code_array_wrapper_dict = tfa_app_code_array_wrapper_instance.to_dict()
# create an instance of TfaAppCodeArrayWrapper from a dict
tfa_app_code_array_wrapper_from_dict = TfaAppCodeArrayWrapper.from_dict(tfa_app_code_array_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


