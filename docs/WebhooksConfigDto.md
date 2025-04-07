# WebhooksConfigDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**name** | **str** | Name | [optional] 
**uri** | **str** | URI | [optional] 
**secret_key** | **str** | Secret key | [optional] 
**enabled** | **bool** | Specifies if the webhooks are enabled or not | [optional] 
**ssl** | **bool** | SSL | [optional] 

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


