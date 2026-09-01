# LoginEventArrayWrapper
The successful API response containing the list of LoginEventDto objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**List[LoginEventDto]**](LoginEventDto.md) | The list of LoginEventDto objects returned by the operation. | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.login_event_array_wrapper import LoginEventArrayWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of LoginEventArrayWrapper from a JSON string
login_event_array_wrapper_instance = LoginEventArrayWrapper.from_json(json)
# print the JSON string representation of the object
print(LoginEventArrayWrapper.to_json())

# convert the object into a dict
login_event_array_wrapper_dict = login_event_array_wrapper_instance.to_dict()
# create an instance of LoginEventArrayWrapper from a dict
login_event_array_wrapper_from_dict = LoginEventArrayWrapper.from_dict(login_event_array_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


