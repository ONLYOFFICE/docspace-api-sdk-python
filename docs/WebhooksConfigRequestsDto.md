# WebhooksConfigRequestsDto

The request parameters for creating or updating the webhook configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The webhook configuration ID. | [optional] 
**name** | **str** | The human-readable name of the webhook configuration. | 
**uri** | **str** | The destination URL where the webhook events will be sent. | 
**secret_key** | **str** | The webhook secret key used to sign the webhook payloads for the security verification. | [optional] 
**enabled** | **bool** | Specifies whether the webhook configuration is active or not. | [optional] 
**ssl** | **bool** | Specifies whether the SSL certificate verification is required or not. | [optional] 
**triggers** | [**WebhookTrigger**](WebhookTrigger.md) |  | [optional] 
**target_id** | **str** | Target ID | [optional] 

## Example

```python
from docspace.models.webhooks_config_requests_dto import WebhooksConfigRequestsDto

# TODO update the JSON string below
json = "{}"
# create an instance of WebhooksConfigRequestsDto from a JSON string
webhooks_config_requests_dto_instance = WebhooksConfigRequestsDto.from_json(json)
# print the JSON string representation of the object
print(WebhooksConfigRequestsDto.to_json())

# convert the object into a dict
webhooks_config_requests_dto_dict = webhooks_config_requests_dto_instance.to_dict()
# create an instance of WebhooksConfigRequestsDto from a dict
webhooks_config_requests_dto_from_dict = WebhooksConfigRequestsDto.from_dict(webhooks_config_requests_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


