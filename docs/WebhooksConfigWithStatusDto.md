# WebhooksConfigWithStatusDto
A webhook subscription together with how its last delivery ended.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configs** | [**WebhooksConfigDto**](WebhooksConfigDto.md) | The subscription itself. Despite the plural name it is one subscription, not a list. | [optional] 
**status** | **int** | The HTTP status code the target answered on the last attempt. `0` means nothing has been delivered yet,  which is not the same as a failure. | [optional] 

## Example

```python
from docspace_api_sdk.models.webhooks_config_with_status_dto import WebhooksConfigWithStatusDto

# TODO update the JSON string below
json = "{}"
# create an instance of WebhooksConfigWithStatusDto from a JSON string
webhooks_config_with_status_dto_instance = WebhooksConfigWithStatusDto.from_json(json)
# print the JSON string representation of the object
print(WebhooksConfigWithStatusDto.to_json())

# convert the object into a dict
webhooks_config_with_status_dto_dict = webhooks_config_with_status_dto_instance.to_dict()
# create an instance of WebhooksConfigWithStatusDto from a dict
webhooks_config_with_status_dto_from_dict = WebhooksConfigWithStatusDto.from_dict(webhooks_config_with_status_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


