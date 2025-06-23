# WebhooksConfigDto

The webhook configuration parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The webhook ID. | [optional] 
**name** | **str** | The webhook name. | [optional] 
**uri** | **str** | The webhook URI. | [optional] 
**enabled** | **bool** | Specifies if the webhooks are enabled or not. | [optional] 
**ssl** | **bool** | The webhook SSL verification (enabled or not). | [optional] 
**triggers** | [**WebhookTrigger**](WebhookTrigger.md) |  | [optional] 
**target_id** | **str** | The webhook target ID. | [optional] 
**created_by** | [**EmployeeDto**](EmployeeDto.md) |  | [optional] 
**created_on** | **datetime** | The date and time when the webhook was created. | [optional] 
**modified_by** | [**EmployeeDto**](EmployeeDto.md) |  | [optional] 
**modified_on** | **datetime** | The date and time when the webhook was modified. | [optional] 
**last_failure_on** | **datetime** | The date and time of the webhook last failure. | [optional] 
**last_failure_content** | **str** | The webhook last failure content. | [optional] 
**last_success_on** | **datetime** | The date and time of the webhook last success. | [optional] 

## Example

```python
from docspace.models.webhooks_config_dto import WebhooksConfigDto

# TODO update the JSON string below
json = "{}"
# create an instance of WebhooksConfigDto from a JSON string
webhooks_config_dto_instance = WebhooksConfigDto.from_json(json)
# print the JSON string representation of the object
print(WebhooksConfigDto.to_json())

# convert the object into a dict
webhooks_config_dto_dict = webhooks_config_dto_instance.to_dict()
# create an instance of WebhooksConfigDto from a dict
webhooks_config_dto_from_dict = WebhooksConfigDto.from_dict(webhooks_config_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


