# WebhooksLogDto
The webhook log parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The webhook log ID. | [optional] 
**config_name** | **str** | The webhook configuration name. | [optional] 
**trigger** | [**WebhookTrigger**](WebhookTrigger.md) |  | [optional] 
**creation_time** | **datetime** | The webhook creation time. | [optional] 
**method** | **str** | The webhook method. | [optional] 
**route** | **str** | The webhook route. | [optional] 
**request_headers** | **str** | The webhook request headers. | [optional] 
**request_payload** | **str** | The webhook request payload. | [optional] 
**response_headers** | **str** | The webhook response headers. | [optional] 
**response_payload** | **str** | The webhook response payload. | [optional] 
**status** | **int** | The webhook status. | [optional] 
**delivery** | **datetime** | The webhook delivery time. | [optional] 

## Example

```python
from docspace-api-python.models.webhooks_log_dto import WebhooksLogDto

# TODO update the JSON string below
json = "{}"
# create an instance of WebhooksLogDto from a JSON string
webhooks_log_dto_instance = WebhooksLogDto.from_json(json)
# print the JSON string representation of the object
print(WebhooksLogDto.to_json())

# convert the object into a dict
webhooks_log_dto_dict = webhooks_log_dto_instance.to_dict()
# create an instance of WebhooksLogDto from a dict
webhooks_log_dto_from_dict = WebhooksLogDto.from_dict(webhooks_log_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


