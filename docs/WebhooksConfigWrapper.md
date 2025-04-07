# WebhooksConfigWrapper


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**WebhooksConfigDto**](WebhooksConfigDto.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace.models.webhooks_config_wrapper import WebhooksConfigWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of WebhooksConfigWrapper from a JSON string
webhooks_config_wrapper_instance = WebhooksConfigWrapper.from_json(json)
# print the JSON string representation of the object
print(WebhooksConfigWrapper.to_json())

# convert the object into a dict
webhooks_config_wrapper_dict = webhooks_config_wrapper_instance.to_dict()
# create an instance of WebhooksConfigWrapper from a dict
webhooks_config_wrapper_from_dict = WebhooksConfigWrapper.from_dict(webhooks_config_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


