# DomainNameRulesDto
The rules a portal name is checked against.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**regex** | **str** | The pattern the portal name has to match. | [optional] 
**min_length** | **int** | The shortest portal name accepted. | [optional] 
**max_length** | **int** | The longest portal name accepted. | [optional] 

## Example

```python
from docspace_api_sdk.models.domain_name_rules_dto import DomainNameRulesDto

# TODO update the JSON string below
json = "{}"
# create an instance of DomainNameRulesDto from a JSON string
domain_name_rules_dto_instance = DomainNameRulesDto.from_json(json)
# print the JSON string representation of the object
print(DomainNameRulesDto.to_json())

# convert the object into a dict
domain_name_rules_dto_dict = domain_name_rules_dto_instance.to_dict()
# create an instance of DomainNameRulesDto from a dict
domain_name_rules_dto_from_dict = DomainNameRulesDto.from_dict(domain_name_rules_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


