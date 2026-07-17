# InvitationLinkDeleteRequestDto
The request parameters for deleting an invitation link.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | The ID of the invitation link. | 

## Example

```python
from docspace_api_sdk.models.invitation_link_delete_request_dto import InvitationLinkDeleteRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of InvitationLinkDeleteRequestDto from a JSON string
invitation_link_delete_request_dto_instance = InvitationLinkDeleteRequestDto.from_json(json)
# print the JSON string representation of the object
print(InvitationLinkDeleteRequestDto.to_json())

# convert the object into a dict
invitation_link_delete_request_dto_dict = invitation_link_delete_request_dto_instance.to_dict()
# create an instance of InvitationLinkDeleteRequestDto from a dict
invitation_link_delete_request_dto_from_dict = InvitationLinkDeleteRequestDto.from_dict(invitation_link_delete_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


