# UnknownNullableWrapper
The successful API response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | **object** |  | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.unknown_nullable_wrapper import UnknownNullableWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of UnknownNullableWrapper from a JSON string
unknown_nullable_wrapper_instance = UnknownNullableWrapper.from_json(json)
# print the JSON string representation of the object
print(UnknownNullableWrapper.to_json())

# convert the object into a dict
unknown_nullable_wrapper_dict = unknown_nullable_wrapper_instance.to_dict()
# create an instance of UnknownNullableWrapper from a dict
unknown_nullable_wrapper_from_dict = UnknownNullableWrapper.from_dict(unknown_nullable_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


