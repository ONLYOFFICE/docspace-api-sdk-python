# ConfirmDto
Whether a confirmation link may still be used, and what it leads to when it invites into a room.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**ValidationResult**](ValidationResult.md) | The outcome of the check. Only `Ok` means the action behind the link may be carried out: `Invalid` and  `Expired` fault the key itself, while `UserExisted`, `UserExcluded`, `TariffLimit` and `QuotaFailed` mean  the key is sound but the invitation behind it cannot be accepted as it stands. | 
**room_id** | **str** | The room the invitation leads into - a numeric folder ID for a room of the portal, a provider-specific  string for a third-party one. It is empty for an invitation to the portal as a whole, for a room that has  been removed or that the invited account may not see, and whenever `result` is neither `Ok` nor  `UserExisted`. | [optional] 
**title** | **str** | The title of that room, present exactly when `roomId` is and meant to be shown on the confirmation page. | [optional] 
**email** | **str** | The address the link was issued for, echoed back only when `result` is `Ok` so that a sign-up form can be  prefilled with it. Every other outcome leaves it empty, `UserExisted` included. | [optional] 
**is_agent** | **bool** | Whether the room behind the link is an AI room rather than an ordinary one, which decides where the invited  person is taken. It is `false` whenever `roomId` is empty. | [optional] 

## Example

```python
from docspace_api_sdk.models.confirm_dto import ConfirmDto

# TODO update the JSON string below
json = "{}"
# create an instance of ConfirmDto from a JSON string
confirm_dto_instance = ConfirmDto.from_json(json)
# print the JSON string representation of the object
print(ConfirmDto.to_json())

# convert the object into a dict
confirm_dto_dict = confirm_dto_instance.to_dict()
# create an instance of ConfirmDto from a dict
confirm_dto_from_dict = ConfirmDto.from_dict(confirm_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


