# InvitationLinkUpdateRequestDto
The request parameters for updating an invitation link.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | The ID of the invitation link. | 
**expiration** | **datetime** | The expiration date of the invitation link. | [optional] 
**max_use_count** | **int** | The maximum number of times the invitation link can be used. | [optional] 

## Example

```python
from docspace_api_sdk.models.invitation_link_update_request_dto import InvitationLinkUpdateRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of InvitationLinkUpdateRequestDto from a JSON string
invitation_link_update_request_dto_instance = InvitationLinkUpdateRequestDto.from_json(json)
# print the JSON string representation of the object
print(InvitationLinkUpdateRequestDto.to_json())

# convert the object into a dict
invitation_link_update_request_dto_dict = invitation_link_update_request_dto_instance.to_dict()
# create an instance of InvitationLinkUpdateRequestDto from a dict
invitation_link_update_request_dto_from_dict = InvitationLinkUpdateRequestDto.from_dict(invitation_link_update_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


