# WebhookRetryRequestDto
Which past webhook deliveries are sent again.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[int]** | The delivery records to send again, by the `id` values `GET api/2.0/settings/webhooks/log` reports. The bound  is per call: a longer batch has to be split into several calls. | [optional] 

## Example

```python
from docspace_api_sdk.models.webhook_retry_request_dto import WebhookRetryRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookRetryRequestDto from a JSON string
webhook_retry_request_dto_instance = WebhookRetryRequestDto.from_json(json)
# print the JSON string representation of the object
print(WebhookRetryRequestDto.to_json())

# convert the object into a dict
webhook_retry_request_dto_dict = webhook_retry_request_dto_instance.to_dict()
# create an instance of WebhookRetryRequestDto from a dict
webhook_retry_request_dto_from_dict = WebhookRetryRequestDto.from_dict(webhook_retry_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


