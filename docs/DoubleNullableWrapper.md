# DoubleNullableWrapper
The successful API response containing the double value.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | **float** | The double value returned by the operation. | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.double_nullable_wrapper import DoubleNullableWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of DoubleNullableWrapper from a JSON string
double_nullable_wrapper_instance = DoubleNullableWrapper.from_json(json)
# print the JSON string representation of the object
print(DoubleNullableWrapper.to_json())

# convert the object into a dict
double_nullable_wrapper_dict = double_nullable_wrapper_instance.to_dict()
# create an instance of DoubleNullableWrapper from a dict
double_nullable_wrapper_from_dict = DoubleNullableWrapper.from_dict(double_nullable_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


