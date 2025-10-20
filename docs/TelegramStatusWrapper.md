# TelegramStatusWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**TelegramStatusDto**](TelegramStatusDto.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

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


