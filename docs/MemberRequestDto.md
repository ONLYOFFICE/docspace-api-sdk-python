# MemberRequestDto

Member request parameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | Password | [optional] 
**password_hash** | **str** | Password hash | [optional] 
**email** | **str** | Email | [optional] 
**type** | [**EmployeeType**](EmployeeType.md) |  | [optional] 
**is_user** | **bool** | Specifies if this is a guest or a user | [optional] 
**first_name** | **str** | First name | [optional] 
**last_name** | **str** | Last name | [optional] 
**department** | **List[str]** | List of user departments | [optional] 
**title** | **str** | Title | [optional] 
**location** | **str** | Location | [optional] 
**sex** | [**SexEnum**](SexEnum.md) |  | [optional] 
**birthday** | [**ApiDateTime**](ApiDateTime.md) |  | [optional] 
**worksfrom** | [**ApiDateTime**](ApiDateTime.md) |  | [optional] 
**comment** | **str** | Comment | [optional] 
**contacts** | [**List[Contact]**](Contact.md) | List of user contacts | [optional] 
**files** | **str** | Avatar photo URL | [optional] 
**from_invite_link** | **bool** | Specifies if the user is added via the invitation link or not | [optional] 
**key** | **str** | Key | [optional] 
**culture_name** | **str** | Language | [optional] 
**target** | **str** | Target | [optional] 
**spam** | **bool** | Spam | [optional] 

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


