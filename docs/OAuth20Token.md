# OAuth20Token
The OAuth 2.0 token issued by a third-party provider.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | The token sent to the provider with every request made on behalf of the account. | [optional] 
**refresh_token** | **str** | The token used to obtain a new access token when the current one expires. A provider that issues no refresh  token leaves it empty, and the account then has to be connected again to keep working. | [optional] 
**expires_in** | **int** | How long the access token stays usable, in seconds counted from `timestamp`. Zero means the provider did not  say, and the token is then treated as expired. | [optional] 
**client_id** | **str** | The OAuth 2.0 client ID of the application the token was issued to. | [optional] 
**client_secret** | **str** | The client secret of the application the token was issued to, needed when the token is refreshed. | [optional] 
**redirect_uri** | **str** | The redirect URL the authorization code behind this token was obtained with; providers require the same value  again when the token is refreshed. | [optional] 
**timestamp** | **datetime** | When the token was issued, in UTC. This is the point `expires_in` is counted from. | [optional] 
**is_expired** | **bool** | Whether the access token can no longer be used and has to be refreshed. It is also true when the provider did  not say how long the token lives. | [optional] [readonly] 

## Example

```python
from docspace_api_sdk.models.o_auth20_token import OAuth20Token

# TODO update the JSON string below
json = "{}"
# create an instance of OAuth20Token from a JSON string
o_auth20_token_instance = OAuth20Token.from_json(json)
# print the JSON string representation of the object
print(OAuth20Token.to_json())

# convert the object into a dict
o_auth20_token_dict = o_auth20_token_instance.to_dict()
# create an instance of OAuth20Token from a dict
o_auth20_token_from_dict = OAuth20Token.from_dict(o_auth20_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


