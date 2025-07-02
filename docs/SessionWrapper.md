# SessionWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**Session**](Session.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace-api-python.models.session_wrapper import SessionWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of SessionWrapper from a JSON string
session_wrapper_instance = SessionWrapper.from_json(json)
# print the JSON string representation of the object
print(SessionWrapper.to_json())

# convert the object into a dict
session_wrapper_dict = session_wrapper_instance.to_dict()
# create an instance of SessionWrapper from a dict
session_wrapper_from_dict = SessionWrapper.from_dict(session_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


