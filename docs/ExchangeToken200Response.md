# ExchangeToken200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | The access token issued by the authorization server. | [optional] 
**token_type** | **str** | The type of token issued, typically &#39;Bearer&#39;. | [optional] 
**expires_in** | **int** | The number of seconds until the access token expires. | [optional] 
**refresh_token** | **str** | The token used to obtain a new access token when the current one expires. | [optional] 

## Example

```python
from docspace_api_sdk.models.exchange_token200_response import ExchangeToken200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ExchangeToken200Response from a JSON string
exchange_token200_response_instance = ExchangeToken200Response.from_json(json)
# print the JSON string representation of the object
print(ExchangeToken200Response.to_json())

# convert the object into a dict
exchange_token200_response_dict = exchange_token200_response_instance.to_dict()
# create an instance of ExchangeToken200Response from a dict
exchange_token200_response_from_dict = ExchangeToken200Response.from_dict(exchange_token200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


