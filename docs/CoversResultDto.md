# CoversResultDto

Represents the result of a covers request containing cover image data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the cover | [optional] 
**data** | **str** | The cover image data | [optional] 

## Example

```python
from docspace.models.covers_result_dto import CoversResultDto

# TODO update the JSON string below
json = "{}"
# create an instance of CoversResultDto from a JSON string
covers_result_dto_instance = CoversResultDto.from_json(json)
# print the JSON string representation of the object
print(CoversResultDto.to_json())

# convert the object into a dict
covers_result_dto_dict = covers_result_dto_instance.to_dict()
# create an instance of CoversResultDto from a dict
covers_result_dto_from_dict = CoversResultDto.from_dict(covers_result_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


