# UpdateMemberRequestDto
The request parameters for updating the user information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | The user ID. | [optional] 
**disable** | **bool** | Specifies whether to disable a user or not. | [optional] 
**email** | **str** | The user email address. | [optional] 
**is_user** | **bool** | Specifies if this is a guest or a user. | [optional] 
**first_name** | **str** | The user first name. | [optional] 
**last_name** | **str** | The user last name. | [optional] 
**department** | **List[str]** | The list of the user departments. | [optional] 
**title** | **str** | The user title. | [optional] 
**location** | **str** | The user location. | [optional] 
**sex** | [**SexEnum**](SexEnum.md) |  | [optional] 
**birthday** | [**ApiDateTime**](ApiDateTime.md) |  | [optional] 
**worksfrom** | [**ApiDateTime**](ApiDateTime.md) |  | [optional] 
**comment** | **str** | The user comment. | [optional] 
**contacts** | [**List[Contact]**](Contact.md) | The list of the user contacts. | [optional] 
**files** | **str** | The user avatar photo URL. | [optional] 
**spam** | **bool** | Specifies if tips, updates and offers are allowed to be sent to the user or not. | [optional] 

## Example

```python
from docspace-api-python.models.update_member_request_dto import UpdateMemberRequestDto

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


