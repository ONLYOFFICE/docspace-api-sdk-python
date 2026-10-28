# SignupAccountRequestDto
The request parameters for creating a third-party account.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employee_type** | [**EmployeeType**](EmployeeType.md) | The type the invitation link is looked up as, defaulting to `RoomAdmin`. It does not decide the resulting  type: the link itself does, and this value only has to match the kind of link that was issued. | [optional] 
**key** | **str** | The key of the invitation link being accepted, taken from the link the invitation email or the room  invitation contains. An expired or already used key is rejected with 403. | 
**culture** | **str** | The culture to set on the new profile, as a culture code. It is applied only when the portal has that culture  enabled, and otherwise the portal default is kept. | [optional] 
**serialized_profile** | **str** | The profile a completed provider authorization produced, in the serialized form the login flow hands back.  Pass that value unchanged; the first name, the last name, the email and the avatar of the new profile are  taken from it. | 

## Example

```python
from docspace_api_sdk.models.signup_account_request_dto import SignupAccountRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of SignupAccountRequestDto from a JSON string
signup_account_request_dto_instance = SignupAccountRequestDto.from_json(json)
# print the JSON string representation of the object
print(SignupAccountRequestDto.to_json())

# convert the object into a dict
signup_account_request_dto_dict = signup_account_request_dto_instance.to_dict()
# create an instance of SignupAccountRequestDto from a dict
signup_account_request_dto_from_dict = SignupAccountRequestDto.from_dict(signup_account_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


