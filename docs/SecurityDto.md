# SecurityDto
The security information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**web_item_id** | **str** | The module ID. | [optional] 
**users** | [**List[EmployeeDto]**](EmployeeDto.md) | The list of users with the access to the module. | [optional] 
**groups** | [**List[GroupSummaryDto]**](GroupSummaryDto.md) | The list of groups with the access to the module. | [optional] 
**enabled** | **bool** | Specifies if the security settings are enabled or not. | [optional] 
**is_sub_item** | **bool** | Specifies if the module is a subitem or not. | [optional] 

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


