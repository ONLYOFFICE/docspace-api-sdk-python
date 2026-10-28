# UpdateGroupRequest
The request for updating a group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**members_to_add** | **List[UUID]** | The accounts to add to the group. An account that is a guest, is disabled or does not exist is skipped  without an error, so the answer has to be read to see what was applied. | [optional] 
**members_to_remove** | **List[UUID]** | The accounts to remove from the group. Removals are applied after the additions, so an account named in both  lists ends up removed, and an ID that is not a member is skipped without an error. | [optional] 
**group_manager** | **UUID** | The account to make the manager of the group, which also adds it to the group. Omit it to keep the current  manager - it cannot be cleared through this operation. | [optional] 
**group_name** | **str** | The new name of the group, up to 128 characters. Omit it to keep the current name. | [optional] 

## Example

```python
from docspace_api_sdk.models.update_group_request import UpdateGroupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateGroupRequest from a JSON string
update_group_request_instance = UpdateGroupRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateGroupRequest.to_json())

# convert the object into a dict
update_group_request_dict = update_group_request_instance.to_dict()
# create an instance of UpdateGroupRequest from a dict
update_group_request_from_dict = UpdateGroupRequest.from_dict(update_group_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


