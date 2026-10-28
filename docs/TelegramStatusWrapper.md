# TelegramStatusWrapper
The successful API response containing the TelegramStatusDto object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**TelegramStatusDto**](TelegramStatusDto.md) | The TelegramStatusDto object returned by the operation. | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.telegram_status_wrapper import TelegramStatusWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of TelegramStatusWrapper from a JSON string
telegram_status_wrapper_instance = TelegramStatusWrapper.from_json(json)
# print the JSON string representation of the object
print(TelegramStatusWrapper.to_json())

# convert the object into a dict
telegram_status_wrapper_dict = telegram_status_wrapper_instance.to_dict()
# create an instance of TelegramStatusWrapper from a dict
telegram_status_wrapper_from_dict = TelegramStatusWrapper.from_dict(telegram_status_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


