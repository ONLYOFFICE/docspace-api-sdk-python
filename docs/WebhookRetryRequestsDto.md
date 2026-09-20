# WebhookRetryRequestsDto
Which past webhook deliveries are sent again.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[int]** | The delivery records to send again, by the identifiers `GET api/2.0/settings/webhooks/log` reports. An  identifier that exists nowhere, and one belonging to another member subscription when the caller is not a  DocSpace administrator, is skipped in silence rather than failing the call, so compare the number of records  that come back against the number sent. An empty list is accepted and queues nothing. | [optional] 

## Example

```python
from docspace_api_sdk.models.webhook_retry_requests_dto import WebhookRetryRequestsDto

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookRetryRequestsDto from a JSON string
webhook_retry_requests_dto_instance = WebhookRetryRequestsDto.from_json(json)
# print the JSON string representation of the object
print(WebhookRetryRequestsDto.to_json())

# convert the object into a dict
webhook_retry_requests_dto_dict = webhook_retry_requests_dto_instance.to_dict()
# create an instance of WebhookRetryRequestsDto from a dict
webhook_retry_requests_dto_from_dict = WebhookRetryRequestsDto.from_dict(webhook_retry_requests_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


