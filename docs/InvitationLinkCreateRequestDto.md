# InvitationLinkCreateRequestDto
The request parameters for creating an invitation link.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employee_type** | [**EmployeeType**](EmployeeType.md) |  | 
**expiration** | **datetime** | The expiration date of the invitation link. | [optional] 
**max_use_count** | **int** | The maximum number of times the invitation link can be used. | [optional] 

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


