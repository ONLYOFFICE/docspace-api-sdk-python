# UpdateMembersRequestDto
The request parameters for updating the user information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_ids** | **List[str]** | The list of user IDs. | [optional] 
**resend_all** | **bool** | Specifies whether to resend invitation letters to all the users or not. | [optional] 

## Example

```python
from docspace-api-python.models.update_members_request_dto import UpdateMembersRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateMembersRequestDto from a JSON string
update_members_request_dto_instance = UpdateMembersRequestDto.from_json(json)
# print the JSON string representation of the object
print(UpdateMembersRequestDto.to_json())

# convert the object into a dict
update_members_request_dto_dict = update_members_request_dto_instance.to_dict()
# create an instance of UpdateMembersRequestDto from a dict
update_members_request_dto_from_dict = UpdateMembersRequestDto.from_dict(update_members_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


