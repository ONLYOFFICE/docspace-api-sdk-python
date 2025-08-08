# GroupRequestDto
The group request parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**members** | **List[str]** | The list of group member IDs. | [optional] 
**group_manager** | **str** | Group manager ID | 
**group_name** | **str** | Group name | [optional] 

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


