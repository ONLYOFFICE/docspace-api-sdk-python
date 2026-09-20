# GroupRequestDto
The group request parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**members** | **List[UUID]** | The accounts to put into the new group. Every one of them has to be an active member that is not a guest,  otherwise the whole call is rejected. Omit it to create an empty group. | [optional] 
**group_manager** | **UUID** | The account to make the manager of the new group. It is added to the group as well, so it does not have to be  repeated in `members`. Omit it to create a group without a manager. | [optional] 
**group_name** | **str** | The name of the group, from 1 to 128 characters. It is required, it may not be blank, and it does not have to  be unique. | 

## Example

```python
from docspace_api_sdk.models.group_request_dto import GroupRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of GroupRequestDto from a JSON string
group_request_dto_instance = GroupRequestDto.from_json(json)
# print the JSON string representation of the object
print(GroupRequestDto.to_json())

# convert the object into a dict
group_request_dto_dict = group_request_dto_instance.to_dict()
# create an instance of GroupRequestDto from a dict
group_request_dto_from_dict = GroupRequestDto.from_dict(group_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


