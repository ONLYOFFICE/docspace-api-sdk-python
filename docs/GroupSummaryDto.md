# GroupSummaryDto
The group summary parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The group ID. | [optional] 
**name** | **str** | The group name. | [optional] 
**manager** | **str** | The group manager. | [optional] 

## Example

```python
from docspace_api_sdk.models.group_summary_dto import GroupSummaryDto

# TODO update the JSON string below
json = "{}"
# create an instance of GroupSummaryDto from a JSON string
group_summary_dto_instance = GroupSummaryDto.from_json(json)
# print the JSON string representation of the object
print(GroupSummaryDto.to_json())

# convert the object into a dict
group_summary_dto_dict = group_summary_dto_instance.to_dict()
# create an instance of GroupSummaryDto from a dict
group_summary_dto_from_dict = GroupSummaryDto.from_dict(group_summary_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


