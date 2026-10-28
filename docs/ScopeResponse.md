# ScopeResponse
One scope from the tenant scope catalogue, as it may be requested by a client.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The scope exactly as it is written in an authorization request, for example files:read or openid. | [optional] 
**group** | **str** | The area of the portal the scope belongs to, which is what groups the scopes on the consent screen: files, rooms, contacts, profiles or openid. | [optional] 
**type** | **str** | What the scope allows inside its group: read for read-only access, write for changes, and openid for the identity scope itself. | [optional] 

## Example

```python
from docspace_api_sdk.models.scope_response import ScopeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ScopeResponse from a JSON string
scope_response_instance = ScopeResponse.from_json(json)
# print the JSON string representation of the object
print(ScopeResponse.to_json())

# convert the object into a dict
scope_response_dict = scope_response_instance.to_dict()
# create an instance of ScopeResponse from a dict
scope_response_from_dict = ScopeResponse.from_dict(scope_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


