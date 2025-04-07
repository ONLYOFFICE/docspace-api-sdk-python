# WebhookArrayWrapper


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**List[Webhook]**](Webhook.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace.models.webhook_array_wrapper import WebhookArrayWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookArrayWrapper from a JSON string
webhook_array_wrapper_instance = WebhookArrayWrapper.from_json(json)
# print the JSON string representation of the object
print(WebhookArrayWrapper.to_json())

# convert the object into a dict
webhook_array_wrapper_dict = webhook_array_wrapper_instance.to_dict()
# create an instance of WebhookArrayWrapper from a dict
webhook_array_wrapper_from_dict = WebhookArrayWrapper.from_dict(webhook_array_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


