# AuthData
The authentication data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**login** | **str** | The authentication login. | [optional] 
**password** | **str** | The authentication password. | [optional] 
**raw_token** | **str** | The authentication raw token. | [optional] 
**url** | **str** | The authentication URL. | [optional] 
**provider** | **str** | The authentication provider. | [optional] 
**token** | [**OAuth20Token**](OAuth20Token.md) |  | [optional] 

## Example

```python
from docspace-api-sdk.models.auth_data import AuthData

# TODO update the JSON string below
json = "{}"
# create an instance of AuthData from a JSON string
auth_data_instance = AuthData.from_json(json)
# print the JSON string representation of the object
print(AuthData.to_json())

# convert the object into a dict
auth_data_dict = auth_data_instance.to_dict()
# create an instance of AuthData from a dict
auth_data_from_dict = AuthData.from_dict(auth_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


