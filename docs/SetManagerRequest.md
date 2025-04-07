# SetManagerRequest

Request parameters for setting a group manager

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | User ID | [optional] 

## Example

```python
from docspace.models.set_manager_request import SetManagerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetManagerRequest from a JSON string
set_manager_request_instance = SetManagerRequest.from_json(json)
# print the JSON string representation of the object
print(SetManagerRequest.to_json())

# convert the object into a dict
set_manager_request_dict = set_manager_request_instance.to_dict()
# create an instance of SetManagerRequest from a dict
set_manager_request_from_dict = SetManagerRequest.from_dict(set_manager_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


