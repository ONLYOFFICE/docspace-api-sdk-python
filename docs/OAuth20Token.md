# OAuth20Token

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** |  | [optional] 
**refresh_token** | **str** |  | [optional] 
**expires_in** | **int** |  | [optional] 
**client_id** | **str** |  | [optional] 
**client_secret** | **str** |  | [optional] 
**redirect_uri** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**is_expired** | **bool** |  | [optional] [readonly] 

## Example

```python
from docspace-api-sdk.models.o_auth20_token import OAuth20Token

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


