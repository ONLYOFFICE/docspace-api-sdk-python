# TimezoneArrayWrapper
The successful API response containing the list of TimezoneDto objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**List[TimezoneDto]**](TimezoneDto.md) | The list of TimezoneDto objects returned by the operation. | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.timezone_array_wrapper import TimezoneArrayWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of TimezoneArrayWrapper from a JSON string
timezone_array_wrapper_instance = TimezoneArrayWrapper.from_json(json)
# print the JSON string representation of the object
print(TimezoneArrayWrapper.to_json())

# convert the object into a dict
timezone_array_wrapper_dict = timezone_array_wrapper_instance.to_dict()
# create an instance of TimezoneArrayWrapper from a dict
timezone_array_wrapper_from_dict = TimezoneArrayWrapper.from_dict(timezone_array_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


