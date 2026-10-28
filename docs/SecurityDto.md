# SecurityDto
How access to one portal module is configured: whether it is restricted, and who is let in.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**web_item_id** | **str** | The module this entry is about, echoed from the identifier that was asked about. When several identifiers  are asked about at once, entries come back one per identifier and in the order they were sent, so they can  also be matched by position. | [optional] 
**users** | [**List[EmployeeDto]**](EmployeeDto.md) | The individual members the rule was stored for. Members the caller is not allowed to see are left out, so  the same module can come back with different lists for different callers and an empty list does not prove  that nobody was granted access. | [optional] 
**groups** | [**List[GroupSummaryDto]**](GroupSummaryDto.md) | The groups the rule was stored for, listed in full - unlike `users`, nothing is filtered out of it. | [optional] 
**enabled** | **bool** | Whether access to the module is restricted to the subjects listed here. It is `false` for a module nobody  has ever configured, in which case the two lists say nothing about who may open it. | [optional] 
**is_sub_item** | **bool** | Whether the module hangs under another one rather than standing on its own. A sub-module is never returned  by `GET api/2.0/settings/security/modules`, which lists top-level modules only. | [optional] 

## Example

```python
from docspace_api_sdk.models.security_dto import SecurityDto

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityDto from a JSON string
security_dto_instance = SecurityDto.from_json(json)
# print the JSON string representation of the object
print(SecurityDto.to_json())

# convert the object into a dict
security_dto_dict = security_dto_instance.to_dict()
# create an instance of SecurityDto from a dict
security_dto_from_dict = SecurityDto.from_dict(security_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


