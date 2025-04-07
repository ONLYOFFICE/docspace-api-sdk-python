# WebhooksLogDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**config_name** | **str** | Config name | [optional] 
**creation_time** | **datetime** | Creation time | [optional] 
**method** | **str** | Method | [optional] 
**route** | **str** | Route | [optional] 
**request_headers** | **str** | Request headers | [optional] 
**request_payload** | **str** | Request payload | [optional] 
**response_headers** | **str** | Response headers | [optional] 
**response_payload** | **str** | Response payload | [optional] 
**status** | **int** | Status | [optional] 
**delivery** | **datetime** | Delivery time | [optional] 

## Example

```python
from docspace.models.webhooks_log_dto import WebhooksLogDto

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


