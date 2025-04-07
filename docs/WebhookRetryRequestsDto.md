# WebhookRetryRequestsDto

Request parameters to retry webhooks

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[int]** | List of webhook IDs | [optional] 

## Example

```python
from docspace.models.webhook_retry_requests_dto import WebhookRetryRequestsDto

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


