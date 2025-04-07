# UserInfoWrapper


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**UserInfo**](UserInfo.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace.models.user_info_wrapper import UserInfoWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of UserInfoWrapper from a JSON string
user_info_wrapper_instance = UserInfoWrapper.from_json(json)
# print the JSON string representation of the object
print(UserInfoWrapper.to_json())

# convert the object into a dict
user_info_wrapper_dict = user_info_wrapper_instance.to_dict()
# create an instance of UserInfoWrapper from a dict
user_info_wrapper_from_dict = UserInfoWrapper.from_dict(user_info_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


