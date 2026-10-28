# InvitationLinkUpdateRequestDto
The invitation link being changed, with the deadline and use limit it is to have afterwards.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | The link to change, by the `id` that creating or reading it returned. The role behind that id cannot be  changed here. | 
**expiration** | **datetime** | The new deadline, read in the portal time zone. The body is applied as a whole, so leaving it out clears the  deadline rather than keeping the current one; a moment in the past is refused. | [optional] 
**max_use_count** | **int** | The new total number of accounts that may join through the link. It may not be lower than the uses already  spent, which the link reports as `currentUseCount`, and leaving it out removes the limit rather than keeping  the current one. | [optional] 

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


