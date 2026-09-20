# SocketSettingsWrapper
The successful API response containing the SocketSettingsDto object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**SocketSettingsDto**](SocketSettingsDto.md) | The SocketSettingsDto object returned by the operation. | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.socket_settings_wrapper import SocketSettingsWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of SocketSettingsWrapper from a JSON string
socket_settings_wrapper_instance = SocketSettingsWrapper.from_json(json)
# print the JSON string representation of the object
print(SocketSettingsWrapper.to_json())

# convert the object into a dict
socket_settings_wrapper_dict = socket_settings_wrapper_instance.to_dict()
# create an instance of SocketSettingsWrapper from a dict
socket_settings_wrapper_from_dict = SocketSettingsWrapper.from_dict(socket_settings_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


