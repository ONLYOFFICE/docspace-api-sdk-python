# FireBaseUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID | [optional] 
**user_id** | **str** | User ID | [optional] 
**tenant_id** | **int** | Tenant ID | [optional] 
**firebase_device_token** | **str** | Firebase device token | [optional] 
**application** | **str** | Application | [optional] 
**is_subscribed** | **bool** | Specifies if the user is subscribed to the push notifications or not | [optional] 
**tenant** | [**DbTenant**](DbTenant.md) |  | [optional] 

## Example

```python
from docspace.models.fire_base_user import FireBaseUser

# TODO update the JSON string below
json = "{}"
# create an instance of FireBaseUser from a JSON string
fire_base_user_instance = FireBaseUser.from_json(json)
# print the JSON string representation of the object
print(FireBaseUser.to_json())

# convert the object into a dict
fire_base_user_dict = fire_base_user_instance.to_dict()
# create an instance of FireBaseUser from a dict
fire_base_user_from_dict = FireBaseUser.from_dict(fire_base_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


