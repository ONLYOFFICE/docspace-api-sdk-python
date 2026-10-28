# InvitationLinkCreateRequestDto
The role a new invitation link grants, and the limits placed on it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employee_type** | [**EmployeeType**](EmployeeType.md) | The role whoever follows the link joins with. Only `DocSpaceAdmin`, `RoomAdmin` and `User` are accepted, and  the role cannot be changed afterwards - delete the link and create one for the other role instead. | 
**expiration** | **datetime** | When the link stops letting anyone in, read in the portal time zone. It has to lie in the future; leaving it  out creates a link with no deadline at all. | [optional] 
**max_use_count** | **int** | How many accounts may join through the link in total. Leaving it out creates a link with no use limit; the  uses spent so far are reported as `currentUseCount`. | [optional] 

## Example

```python
from docspace_api_sdk.models.invitation_link_create_request_dto import InvitationLinkCreateRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of InvitationLinkCreateRequestDto from a JSON string
invitation_link_create_request_dto_instance = InvitationLinkCreateRequestDto.from_json(json)
# print the JSON string representation of the object
print(InvitationLinkCreateRequestDto.to_json())

# convert the object into a dict
invitation_link_create_request_dto_dict = invitation_link_create_request_dto_instance.to_dict()
# create an instance of InvitationLinkCreateRequestDto from a dict
invitation_link_create_request_dto_from_dict = InvitationLinkCreateRequestDto.from_dict(invitation_link_create_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


