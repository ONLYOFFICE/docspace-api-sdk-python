# FireBaseUserWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**FireBaseUser**](FireBaseUser.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace-api-sdk.models.fire_base_user_wrapper import FireBaseUserWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of FireBaseUserWrapper from a JSON string
fire_base_user_wrapper_instance = FireBaseUserWrapper.from_json(json)
# print the JSON string representation of the object
print(FireBaseUserWrapper.to_json())

# convert the object into a dict
fire_base_user_wrapper_dict = fire_base_user_wrapper_instance.to_dict()
# create an instance of FireBaseUserWrapper from a dict
fire_base_user_wrapper_from_dict = FireBaseUserWrapper.from_dict(fire_base_user_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


