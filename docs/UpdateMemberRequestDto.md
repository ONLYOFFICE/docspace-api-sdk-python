# UpdateMemberRequestDto

Request parameters for updating user information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | User ID | [optional] 
**disable** | **bool** | Specifies whether to disable a user or not | [optional] 
**email** | **str** | Email | [optional] 
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
**culture_name** | **str** | Language | [optional] 
**spam** | **bool** | Spam | [optional] 

## Example

```python
from docspace.models.update_member_request_dto import UpdateMemberRequestDto

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


