# PasswordHasher

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**size** | **int** |  | [optional] [readonly] 
**iterations** | **int** |  | [optional] [readonly] 
**salt** | **str** |  | [optional] [readonly] 

## Example

```python
from docspace_api_sdk.models.password_hasher import PasswordHasher

# TODO update the JSON string below
json = "{}"
# create an instance of PasswordHasher from a JSON string
password_hasher_instance = PasswordHasher.from_json(json)
# print the JSON string representation of the object
print(PasswordHasher.to_json())

# convert the object into a dict
password_hasher_dict = password_hasher_instance.to_dict()
# create an instance of PasswordHasher from a dict
password_hasher_from_dict = PasswordHasher.from_dict(password_hasher_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


