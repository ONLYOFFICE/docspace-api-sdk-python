# WebhooksLogWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**WebhooksLogDto**](WebhooksLogDto.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace-api-sdk.models.webhooks_log_wrapper import WebhooksLogWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of WebhooksLogWrapper from a JSON string
webhooks_log_wrapper_instance = WebhooksLogWrapper.from_json(json)
# print the JSON string representation of the object
print(WebhooksLogWrapper.to_json())

# convert the object into a dict
webhooks_log_wrapper_dict = webhooks_log_wrapper_instance.to_dict()
# create an instance of WebhooksLogWrapper from a dict
webhooks_log_wrapper_from_dict = WebhooksLogWrapper.from_dict(webhooks_log_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


