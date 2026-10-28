# ExternalResourceDto
The external resource parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | The external resource domain. | [optional] 
**entries** | **Dict[str, Optional[str]]** | The external resource entries. | [optional] 

## Example

```python
from docspace_api_sdk.models.external_resource_dto import ExternalResourceDto

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalResourceDto from a JSON string
external_resource_dto_instance = ExternalResourceDto.from_json(json)
# print the JSON string representation of the object
print(ExternalResourceDto.to_json())

# convert the object into a dict
external_resource_dto_dict = external_resource_dto_instance.to_dict()
# create an instance of ExternalResourceDto from a dict
external_resource_dto_from_dict = ExternalResourceDto.from_dict(external_resource_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


