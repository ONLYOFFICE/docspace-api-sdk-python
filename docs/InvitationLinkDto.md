# InvitationLinkDto
The invitation link parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | The ID of the invitation link. | [optional] 
**employee_type** | [**EmployeeType**](EmployeeType.md) | The type of employee role for the invitation link. | 
**expiration** | **datetime** | The expiration date of the invitation link. | [optional] 
**is_expired** | **bool** | Indicates whether the invitation link has expired. | [optional] 
**max_use_count** | **int** | The maximum number of times the invitation link can be used. | [optional] 
**current_use_count** | **int** | The current number of times the invitation link has been used. | [optional] 
**url** | **str** | The URL of the invitation link. | [optional] 

## Example

```python
from docspace_api_sdk.models.invitation_link_dto import InvitationLinkDto

# TODO update the JSON string below
json = "{}"
# create an instance of InvitationLinkDto from a JSON string
invitation_link_dto_instance = InvitationLinkDto.from_json(json)
# print the JSON string representation of the object
print(InvitationLinkDto.to_json())

# convert the object into a dict
invitation_link_dto_dict = invitation_link_dto_instance.to_dict()
# create an instance of InvitationLinkDto from a dict
invitation_link_dto_from_dict = InvitationLinkDto.from_dict(invitation_link_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


