# UpdateGroupRequest

The request for updating a group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**members_to_add** | **List[str]** | The list of user IDs to add to the group. | [optional] 
**members_to_remove** | **List[str]** | The list of user IDs to remove from the group. | [optional] 
**group_manager** | **str** | The group manager ID. | [optional] 
**group_name** | **str** | The group name. | [optional] 

## Example

```python
from docspace.models.update_group_request import UpdateGroupRequest

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


