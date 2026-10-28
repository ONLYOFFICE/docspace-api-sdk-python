# TelegramStatusDto
Whether the calling user's account is linked to the portal's Telegram bot.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**RegStatus**](RegStatus.md) | Where the caller's own account stands: not linked, linked, or a registration link issued and the portal  still waiting for it to be opened in Telegram. The waiting state ends on its own when the link expires,  so it is worth polling rather than treating as final. | 
**username** | **str** | The Telegram handle the account is linked to, without the leading `@`. It is filled in only while the  account is linked and comes back empty in the other two states. | [optional] 

## Example

```python
from docspace_api_sdk.models.telegram_status_dto import TelegramStatusDto

# TODO update the JSON string below
json = "{}"
# create an instance of TelegramStatusDto from a JSON string
telegram_status_dto_instance = TelegramStatusDto.from_json(json)
# print the JSON string representation of the object
print(TelegramStatusDto.to_json())

# convert the object into a dict
telegram_status_dto_dict = telegram_status_dto_instance.to_dict()
# create an instance of TelegramStatusDto from a dict
telegram_status_dto_from_dict = TelegramStatusDto.from_dict(telegram_status_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


