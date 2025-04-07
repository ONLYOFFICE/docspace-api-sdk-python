# AuthData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**login** | **str** | Login | [optional] 
**password** | **str** | Password | [optional] 
**raw_token** | **str** | Raw token | [optional] 
**url** | **str** | Url | [optional] 
**provider** | **str** | Provider | [optional] 
**token** | [**OAuth20Token**](OAuth20Token.md) |  | [optional] 

## Example

```python
from docspace.models.auth_data import AuthData

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


