# WebhookTargetId

The ID of the entity a subscription is scoped to, which depends on the trigger family: the GUID of the user or group, as a string, for user.* and group.* events, and an entry ID for file, folder, room, form and agent events - an integer for DocSpace's own storage, a string for a third-party provider. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from docspace_webhooks_sdk.models.webhook_target_id import WebhookTargetId

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookTargetId from a JSON string
webhook_target_id_instance = WebhookTargetId.from_json(json)
# print the JSON string representation of the object
print(WebhookTargetId.to_json())

# convert the object into a dict
webhook_target_id_dict = webhook_target_id_instance.to_dict()
# create an instance of WebhookTargetId from a dict
webhook_target_id_from_dict = WebhookTargetId.from_dict(webhook_target_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


