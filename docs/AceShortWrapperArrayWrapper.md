# AceShortWrapperArrayWrapper
The successful API response containing the list of AceShortWrapper objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**List[AceShortWrapper]**](AceShortWrapper.md) | The list of AceShortWrapper objects returned by the operation. | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.ace_short_wrapper_array_wrapper import AceShortWrapperArrayWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of AceShortWrapperArrayWrapper from a JSON string
ace_short_wrapper_array_wrapper_instance = AceShortWrapperArrayWrapper.from_json(json)
# print the JSON string representation of the object
print(AceShortWrapperArrayWrapper.to_json())

# convert the object into a dict
ace_short_wrapper_array_wrapper_dict = ace_short_wrapper_array_wrapper_instance.to_dict()
# create an instance of AceShortWrapperArrayWrapper from a dict
ace_short_wrapper_array_wrapper_from_dict = AceShortWrapperArrayWrapper.from_dict(ace_short_wrapper_array_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


