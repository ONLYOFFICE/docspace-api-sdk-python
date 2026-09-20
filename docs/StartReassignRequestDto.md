# StartReassignRequestDto
The request parameters for starting the reassignment process.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_user_id** | **UUID** | The ID of the user whose rooms and shared files are transferred away. The account has to have the `Terminated`  status already, and it cannot be a system account, the portal owner or the caller. | 
**to_user_id** | **UUID** | The ID of the user who receives the data. The account has to be an active room admin or DocSpace admin, so a  guest, a system account or a disabled account is rejected. | 
**delete_profile** | **bool** | Specifies whether to delete the source profile once the transfer succeeds. When false, which is the default,  the emptied profile is kept and can be deleted later through `DELETE api/2.0/people/{userid}`. | [optional] 

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


