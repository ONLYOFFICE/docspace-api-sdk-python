# WebhooksConfigWithStatusArrayWrapper
The successful API response containing the list of WebhooksConfigWithStatusDto objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**List[WebhooksConfigWithStatusDto]**](WebhooksConfigWithStatusDto.md) | The list of WebhooksConfigWithStatusDto objects returned by the operation. | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.webhooks_config_with_status_array_wrapper import WebhooksConfigWithStatusArrayWrapper

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


