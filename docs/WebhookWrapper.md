# WebhookWrapper


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**Webhook**](Webhook.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace.models.webhook_wrapper import WebhookWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookWrapper from a JSON string
webhook_wrapper_instance = WebhookWrapper.from_json(json)
# print the JSON string representation of the object
print(WebhookWrapper.to_json())

# convert the object into a dict
webhook_wrapper_dict = webhook_wrapper_instance.to_dict()
# create an instance of WebhookWrapper from a dict
webhook_wrapper_from_dict = WebhookWrapper.from_dict(webhook_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


