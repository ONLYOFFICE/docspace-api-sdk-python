# AppWrapper
The successful API response containing the AppDto object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**AppDto**](AppDto.md) | The AppDto object returned by the operation. | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.app_wrapper import AppWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of AppWrapper from a JSON string
app_wrapper_instance = AppWrapper.from_json(json)
# print the JSON string representation of the object
print(AppWrapper.to_json())

# convert the object into a dict
app_wrapper_dict = app_wrapper_instance.to_dict()
# create an instance of AppWrapper from a dict
app_wrapper_from_dict = AppWrapper.from_dict(app_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


