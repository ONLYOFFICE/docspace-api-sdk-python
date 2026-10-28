# WebhookTriggerDto
One event a webhook can listen to, with the bit that selects it and whether the caller may subscribe to it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The event name exactly as it appears in a delivered payload, so a receiver can match on it. The entry  named `*` is not an event but the catch-all. | [optional] 
**id** | **int** | The bit that stands for this event in the `triggers` bitmask of a subscription. Add the bits of the wanted  events together; the catch-all entry has the value `0` and is used on its own rather than added to  anything. | [optional] 
**available** | **bool** | Whether the caller's own role may subscribe to this event - a plain member cannot subscribe to user, group  or room creation, where a room administrator can. An unavailable event is listed all the same, and sending  its bit to `POST api/2.0/settings/webhook` is refused as an invalid request. | [optional] 

## Example

```python
from docspace_api_sdk.models.webhook_trigger_dto import WebhookTriggerDto

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookTriggerDto from a JSON string
webhook_trigger_dto_instance = WebhookTriggerDto.from_json(json)
# print the JSON string representation of the object
print(WebhookTriggerDto.to_json())

# convert the object into a dict
webhook_trigger_dto_dict = webhook_trigger_dto_instance.to_dict()
# create an instance of WebhookTriggerDto from a dict
webhook_trigger_dto_from_dict = WebhookTriggerDto.from_dict(webhook_trigger_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


