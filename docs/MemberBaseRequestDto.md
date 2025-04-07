# MemberBaseRequestDto

Request parameters for setting new password

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | Password | [optional] 
**password_hash** | **str** | Password hash | [optional] 
**email** | **str** | Email | [optional] 

## Example

```python
from docspace.models.member_base_request_dto import MemberBaseRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of MemberBaseRequestDto from a JSON string
member_base_request_dto_instance = MemberBaseRequestDto.from_json(json)
# print the JSON string representation of the object
print(MemberBaseRequestDto.to_json())

# convert the object into a dict
member_base_request_dto_dict = member_base_request_dto_instance.to_dict()
# create an instance of MemberBaseRequestDto from a dict
member_base_request_dto_from_dict = MemberBaseRequestDto.from_dict(member_base_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


