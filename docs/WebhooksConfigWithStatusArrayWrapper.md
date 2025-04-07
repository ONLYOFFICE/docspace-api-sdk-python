# WebhooksConfigWithStatusArrayWrapper


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**List[WebhooksConfigWithStatusDto]**](WebhooksConfigWithStatusDto.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace.models.webhooks_config_with_status_array_wrapper import WebhooksConfigWithStatusArrayWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of WebhooksConfigWithStatusArrayWrapper from a JSON string
webhooks_config_with_status_array_wrapper_instance = WebhooksConfigWithStatusArrayWrapper.from_json(json)
# print the JSON string representation of the object
print(WebhooksConfigWithStatusArrayWrapper.to_json())

# convert the object into a dict
webhooks_config_with_status_array_wrapper_dict = webhooks_config_with_status_array_wrapper_instance.to_dict()
# create an instance of WebhooksConfigWithStatusArrayWrapper from a dict
webhooks_config_with_status_array_wrapper_from_dict = WebhooksConfigWithStatusArrayWrapper.from_dict(webhooks_config_with_status_array_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


