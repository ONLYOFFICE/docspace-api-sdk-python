# WebhooksConfigRequestsDto

Webhook request parameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**name** | **str** | Name | 
**uri** | **str** | URI | 
**secret_key** | **str** | Secret key | [optional] 
**enabled** | **bool** | Enabled or not | [optional] 
**ssl** | **bool** | SSL | [optional] 

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


