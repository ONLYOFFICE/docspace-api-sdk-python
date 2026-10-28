# SecurityArrayWrapper
The successful API response containing the list of SecurityDto objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**List[SecurityDto]**](SecurityDto.md) | The list of SecurityDto objects returned by the operation. | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.security_array_wrapper import SecurityArrayWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityArrayWrapper from a JSON string
security_array_wrapper_instance = SecurityArrayWrapper.from_json(json)
# print the JSON string representation of the object
print(SecurityArrayWrapper.to_json())

# convert the object into a dict
security_array_wrapper_dict = security_array_wrapper_instance.to_dict()
# create an instance of SecurityArrayWrapper from a dict
security_array_wrapper_from_dict = SecurityArrayWrapper.from_dict(security_array_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


