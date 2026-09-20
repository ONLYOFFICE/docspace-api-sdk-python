# ExchangeToken200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | The token to send as a Bearer credential when calling the portal on the user behalf. | [optional] 
**token_type** | **str** | How the access token is to be presented. It is always Bearer. | [optional] 
**expires_in** | **int** | How many seconds the access token stays valid, counted from the moment it was issued. | [optional] 
**refresh_token** | **str** | The token that buys a new access token once the current one expires. It is present only when the client is registered for the refresh token grant. | [optional] 

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


