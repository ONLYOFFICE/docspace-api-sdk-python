# AuthKeyRequest
One key of a provider and the value to store for it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The key name, as `GET api/2.0/settings/authservice` lists it in `props`. | 
**value** | **str** | The value to store. An empty string clears the key. | 
**title** | **str** | Accepted for compatibility with earlier clients and not read: the server keeps its own value. | [optional] 
**type** | **str** | Accepted for compatibility with earlier clients and not read: the server keeps its own value. | [optional] 
**options** | **List[str]** | Accepted for compatibility with earlier clients and not read: the server keeps its own value. | [optional] 
**depends_on** | **str** | Accepted for compatibility with earlier clients and not read: the server keeps its own value. | [optional] 
**depends_on_value** | **str** | Accepted for compatibility with earlier clients and not read: the server keeps its own value. | [optional] 

## Example

```python
from docspace_api_sdk.models.auth_key_request import AuthKeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AuthKeyRequest from a JSON string
auth_key_request_instance = AuthKeyRequest.from_json(json)
# print the JSON string representation of the object
print(AuthKeyRequest.to_json())

# convert the object into a dict
auth_key_request_dict = auth_key_request_instance.to_dict()
# create an instance of AuthKeyRequest from a dict
auth_key_request_from_dict = AuthKeyRequest.from_dict(auth_key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


