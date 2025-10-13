# AuthKey
The authentication key parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The authentication key name. | 
**value** | **str** | The authentication key value. | 
**title** | **str** | The authentication key title. | 

## Example

```python
from docspace_api_sdk.models.auth_key import AuthKey

# TODO update the JSON string below
json = "{}"
# create an instance of AuthKey from a JSON string
auth_key_instance = AuthKey.from_json(json)
# print the JSON string representation of the object
print(AuthKey.to_json())

# convert the object into a dict
auth_key_dict = auth_key_instance.to_dict()
# create an instance of AuthKey from a dict
auth_key_from_dict = AuthKey.from_dict(auth_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


