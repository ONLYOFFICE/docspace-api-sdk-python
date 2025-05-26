# MemberRequestDto

The user request parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | The user password. | [optional] 
**password_hash** | **str** | The user password hash. | [optional] 
**email** | **str** | The user email address. | [optional] 
**type** | [**EmployeeType**](EmployeeType.md) |  | [optional] 
**is_user** | **bool** | Specifies if this is a guest or a user. | [optional] 
**first_name** | **str** | The user first name. | [optional] 
**last_name** | **str** | The user last name. | [optional] 
**department** | **List[str]** | The list of the user departments IDs. | [optional] 
**title** | **str** | The user title. | [optional] 
**location** | **str** | The user location. | [optional] 
**sex** | [**SexEnum**](SexEnum.md) |  | [optional] 
**birthday** | [**ApiDateTime**](ApiDateTime.md) |  | [optional] 
**worksfrom** | [**ApiDateTime**](ApiDateTime.md) |  | [optional] 
**comment** | **str** | The user comment. | [optional] 
**contacts** | [**List[Contact]**](Contact.md) | The list of the user contacts. | [optional] 
**files** | **str** | The avatar photo URL. | [optional] 
**from_invite_link** | **bool** | Specifies if the user is added via the invitation link or not. | [optional] 
**key** | **str** | The user key. | [optional] 
**culture_name** | **str** | The user culture code. | [optional] 
**target** | **str** | The user target ID. | [optional] 
**spam** | **bool** | Specifies if tips, updates and offers are allowed to be sent to the user or not. | [optional] 

## Example

```python
from docspace.models.member_request_dto import MemberRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of MemberRequestDto from a JSON string
member_request_dto_instance = MemberRequestDto.from_json(json)
# print the JSON string representation of the object
print(MemberRequestDto.to_json())

# convert the object into a dict
member_request_dto_dict = member_request_dto_instance.to_dict()
# create an instance of MemberRequestDto from a dict
member_request_dto_from_dict = MemberRequestDto.from_dict(member_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


