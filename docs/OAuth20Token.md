# OAuth20Token
The OAuth 2.0 token issued by a third-party provider.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | Access token | [optional] 
**refresh_token** | **str** | Refresh token | [optional] 
**expires_in** | **int** | Expires in | [optional] 
**client_id** | **str** | Client id | [optional] 
**client_secret** | **str** | Client secret | [optional] 
**redirect_uri** | **str** | Redirect uri | [optional] 
**timestamp** | **datetime** | Timestamp | [optional] 
**is_expired** | **bool** | Is expired | [optional] [readonly] 

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


