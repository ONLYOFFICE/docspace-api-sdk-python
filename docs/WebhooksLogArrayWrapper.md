# WebhooksLogArrayWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**List[WebhooksLogDto]**](WebhooksLogDto.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace_api_sdk.models.webhooks_log_array_wrapper import WebhooksLogArrayWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of WebhooksLogArrayWrapper from a JSON string
webhooks_log_array_wrapper_instance = WebhooksLogArrayWrapper.from_json(json)
# print the JSON string representation of the object
print(WebhooksLogArrayWrapper.to_json())

# convert the object into a dict
webhooks_log_array_wrapper_dict = webhooks_log_array_wrapper_instance.to_dict()
# create an instance of WebhooksLogArrayWrapper from a dict
webhooks_log_array_wrapper_from_dict = WebhooksLogArrayWrapper.from_dict(webhooks_log_array_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


