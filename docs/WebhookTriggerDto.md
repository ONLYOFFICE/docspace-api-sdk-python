# WebhookTriggerDto
The webhook trigger with its availability for the current user.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The trigger name. | [optional] 
**id** | **int** | The trigger bit value. | [optional] 
**available** | **bool** | Specifies whether this trigger is available for the current user's role. | [optional] 

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


