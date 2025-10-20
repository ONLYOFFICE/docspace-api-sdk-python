# UpdateWebhooksConfigRequestsDto
The request parameters for updating the webhook configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The human-readable name of the webhook configuration. | 
**uri** | **str** | The destination URL where the webhook events will be sent. | 
**secret_key** | **str** | The webhook secret key used to sign the webhook payloads for the security verification. | [optional] 
**enabled** | **bool** | Specifies whether the webhook configuration is active or not. | [optional] 
**ssl** | **bool** | Specifies whether the SSL certificate verification is required or not. | [optional] 
**triggers** | [**WebhookTrigger**](WebhookTrigger.md) |  | [optional] 
**target_id** | **str** | Target ID | [optional] 
**id** | **int** | The webhook configuration ID. | 

## Example

```python
from docspace_api_sdk.models.update_webhooks_config_requests_dto import UpdateWebhooksConfigRequestsDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateWebhooksConfigRequestsDto from a JSON string
update_webhooks_config_requests_dto_instance = UpdateWebhooksConfigRequestsDto.from_json(json)
# print the JSON string representation of the object
print(UpdateWebhooksConfigRequestsDto.to_json())

# convert the object into a dict
update_webhooks_config_requests_dto_dict = update_webhooks_config_requests_dto_instance.to_dict()
# create an instance of UpdateWebhooksConfigRequestsDto from a dict
update_webhooks_config_requests_dto_from_dict = UpdateWebhooksConfigRequestsDto.from_dict(update_webhooks_config_requests_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


