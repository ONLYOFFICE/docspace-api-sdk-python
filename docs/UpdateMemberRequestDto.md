# UpdateMemberRequestDto
The request parameters for updating the user information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | The account the change applies to. It is read from this body by `POST api/2.0/people/email`, while  `PUT api/2.0/people/{userid}` takes the account from the route and ignores this field. | [optional] 
**disable** | **bool** | Set it to true to give the account the `Terminated` status and end every session it has, and to false to  bring it back. It is applied only when the caller edits somebody else, and omitting it keeps the current  status. | [optional] 
**email** | **str** | The new email address, up to 255 characters. It is read only by `POST api/2.0/people/email`, which either  mails a confirmation letter or, for an administrator acting on somebody else, applies the address at once;  `PUT api/2.0/people/{userid}` ignores it. | [optional] 
**is_user** | **bool** | Set it to true to turn the account into a guest and to false to turn it back into a member. Either direction  takes a seat and can answer 402, it is applied only when the caller edits somebody else, and a request to  make the portal owner, a DocSpace administrator or a module administrator a guest is ignored. | [optional] 
**first_name** | **str** | The new first name, up to 255 characters. It is applied only to the caller's own profile, is left alone on an  LDAP or SSO account, and a pair the portal does not accept as a name answers 400. | [optional] 
**last_name** | **str** | The new last name, up to 255 characters. It is applied only to the caller's own profile, is left alone on an  LDAP or SSO account, and a pair the portal does not accept as a name answers 400. | [optional] 
**department** | **List[UUID]** | The groups the profile should belong to, by group ID, replacing the current ones. It is applied only to the  caller's own profile. | [optional] 
**location** | **str** | The new free-text location shown on the profile. It is applied only to the caller's own profile and is left  alone on an LDAP or SSO account. | [optional] 
**comment** | **str** | The new free-text note kept with the profile. It is applied only to the caller's own profile. | [optional] 
**contacts** | [**List[Contact]**](Contact.md) | The additional ways to reach the person, replacing the current ones. Each entry is a free-text type such as  `email`, `phone`, `skype` or `telegram` and its value, an entry with an empty value is dropped, and the field  is applied only to the caller's own profile. | [optional] 
**files** | **str** | The address the portal downloads the new avatar from. It is applied only to the caller's own profile, has to  use HTTPS unless the request itself came over HTTP, and passing the address the profile already uses  downloads nothing. | [optional] 
**spam** | **bool** | Whether the account agrees to receive tips, updates and offers. It is applied only to the caller's own  profile, and omitting it on such a request stores false rather than keeping the current value. | [optional] 

## Example

```python
from docspace_api_sdk.models.update_member_request_dto import UpdateMemberRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateMemberRequestDto from a JSON string
update_member_request_dto_instance = UpdateMemberRequestDto.from_json(json)
# print the JSON string representation of the object
print(UpdateMemberRequestDto.to_json())

# convert the object into a dict
update_member_request_dto_dict = update_member_request_dto_instance.to_dict()
# create an instance of UpdateMemberRequestDto from a dict
update_member_request_dto_from_dict = UpdateMemberRequestDto.from_dict(update_member_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


