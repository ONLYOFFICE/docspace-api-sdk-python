# LoginEventArrayWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**List[LoginEventDto]**](LoginEventDto.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace_api_sdk.models.login_event_array_wrapper import LoginEventArrayWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of LoginEventArrayWrapper from a JSON string
login_event_array_wrapper_instance = LoginEventArrayWrapper.from_json(json)
# print the JSON string representation of the object
print(LoginEventArrayWrapper.to_json())

# convert the object into a dict
login_event_array_wrapper_dict = login_event_array_wrapper_instance.to_dict()
# create an instance of LoginEventArrayWrapper from a dict
login_event_array_wrapper_from_dict = LoginEventArrayWrapper.from_dict(login_event_array_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


