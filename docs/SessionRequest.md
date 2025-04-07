# SessionRequest

Session parameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_name** | **str** | File name | [optional] 
**file_size** | **int** | File length in bytes | [optional] 
**relative_path** | **str** | Relative path to the folder | [optional] 
**create_on** | [**ApiDateTime**](ApiDateTime.md) |  | [optional] 
**encrypted** | **bool** | Specifies whether to encrypt a file or not | [optional] 
**create_new_if_exist** | **bool** | Create new if exists | [optional] 

## Example

```python
from docspace.models.session_request import SessionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SessionRequest from a JSON string
session_request_instance = SessionRequest.from_json(json)
# print the JSON string representation of the object
print(SessionRequest.to_json())

# convert the object into a dict
session_request_dict = session_request_instance.to_dict()
# create an instance of SessionRequest from a dict
session_request_from_dict = SessionRequest.from_dict(session_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


