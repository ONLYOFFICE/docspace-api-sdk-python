# CreateWebhooksConfigRequestsDto
The request parameters for creating the webhook configuration.

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

## Example

```python
from docspace-api-sdk.models.create_webhooks_config_requests_dto import CreateWebhooksConfigRequestsDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateWebhooksConfigRequestsDto from a JSON string
create_webhooks_config_requests_dto_instance = CreateWebhooksConfigRequestsDto.from_json(json)
# print the JSON string representation of the object
print(CreateWebhooksConfigRequestsDto.to_json())

# convert the object into a dict
create_webhooks_config_requests_dto_dict = create_webhooks_config_requests_dto_instance.to_dict()
# create an instance of CreateWebhooksConfigRequestsDto from a dict
create_webhooks_config_requests_dto_from_dict = CreateWebhooksConfigRequestsDto.from_dict(create_webhooks_config_requests_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


