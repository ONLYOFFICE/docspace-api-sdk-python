# GroupSummaryPayload

A group referenced from another webhook payload.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | The ID of the group; &#x60;GET api/2.0/group/{id}&#x60; returns the group with its members by it. | [optional] 
**name** | **str** | The name of the group as it is shown in the portal. | [optional] 
**manager** | **str** | The user name of the user who manages the group, not an ID. Absent when the group has no manager. | [optional] 
**is_system** | **bool** | &#x60;true&#x60; for a built-in system group, whose members follow from the user types rather than from membership changes. Absent for every other group, never &#x60;false&#x60;. | [optional] 

## Example

```python
from docspace_webhooks_sdk.models.group_summary_payload import GroupSummaryPayload

# TODO update the JSON string below
json = "{}"
# create an instance of GroupSummaryPayload from a JSON string
group_summary_payload_instance = GroupSummaryPayload.from_json(json)
# print the JSON string representation of the object
print(GroupSummaryPayload.to_json())

# convert the object into a dict
group_summary_payload_dict = group_summary_payload_instance.to_dict()
# create an instance of GroupSummaryPayload from a dict
group_summary_payload_from_dict = GroupSummaryPayload.from_dict(group_summary_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


