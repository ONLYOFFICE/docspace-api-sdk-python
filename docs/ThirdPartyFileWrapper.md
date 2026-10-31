# ThirdPartyFileWrapper
The successful API response containing the ThirdPartyFileDto object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**ThirdPartyFileDto**](ThirdPartyFileDto.md) | The ThirdPartyFileDto object returned by the operation. | [optional] 
**count** | **int** | How many items this response carries: the length of the page for a list, 1 for a single object | [optional] 
**total** | **int** | How many items the whole list holds across all pages, for working out how many pages to request. Sent only by the operations that page their results, and left out of every other response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.third_party_file_wrapper import ThirdPartyFileWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of ThirdPartyFileWrapper from a JSON string
third_party_file_wrapper_instance = ThirdPartyFileWrapper.from_json(json)
# print the JSON string representation of the object
print(ThirdPartyFileWrapper.to_json())

# convert the object into a dict
third_party_file_wrapper_dict = third_party_file_wrapper_instance.to_dict()
# create an instance of ThirdPartyFileWrapper from a dict
third_party_file_wrapper_from_dict = ThirdPartyFileWrapper.from_dict(third_party_file_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


