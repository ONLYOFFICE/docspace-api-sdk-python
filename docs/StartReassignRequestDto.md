# StartReassignRequestDto
The request parameters for starting the reassignment process.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_user_id** | **str** | The user ID whose data will be reassigned to another user. | 
**to_user_id** | **str** | The user ID to whom all the data will be reassigned. | 
**delete_profile** | **bool** | Specifies whether to delete a profile when the data reassignment will be finished or not. | [optional] 

## Example

```python
from docspace_api_sdk.models.start_reassign_request_dto import StartReassignRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of StartReassignRequestDto from a JSON string
start_reassign_request_dto_instance = StartReassignRequestDto.from_json(json)
# print the JSON string representation of the object
print(StartReassignRequestDto.to_json())

# convert the object into a dict
start_reassign_request_dto_dict = start_reassign_request_dto_instance.to_dict()
# create an instance of StartReassignRequestDto from a dict
start_reassign_request_dto_from_dict = StartReassignRequestDto.from_dict(start_reassign_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


