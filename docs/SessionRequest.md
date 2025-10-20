# SessionRequest
The session request parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_name** | **str** | The file name. | 
**file_size** | **int** | The file size. | [optional] 
**relative_path** | **str** | The relative path to the file. | [optional] 
**create_on** | [**ApiDateTime**](ApiDateTime.md) |  | [optional] 
**encrypted** | **bool** | Specifies whether the file is encrypted or not. | [optional] 
**create_new_if_exist** | **bool** | Specifies whether to create a new file if it already exists. | [optional] 

## Example

```python
from docspace_api_sdk.models.session_request import SessionRequest

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


