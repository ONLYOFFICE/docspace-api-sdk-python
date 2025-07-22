# WebhooksConfigWithStatusDto
The webhook configuration with its status.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configs** | [**WebhooksConfigDto**](WebhooksConfigDto.md) |  | [optional] 
**status** | **int** | The webhook status. | [optional] 

## Example

```python
from docspace-api-sdk.models.webhooks_config_with_status_dto import WebhooksConfigWithStatusDto

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


