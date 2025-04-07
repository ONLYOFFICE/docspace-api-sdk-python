# TemplatesRequestDto

Request parameters for adding files to the template list

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_ids** | **List[int]** | List of file IDs | [optional] 

## Example

```python
from docspace.models.templates_request_dto import TemplatesRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of TemplatesRequestDto from a JSON string
templates_request_dto_instance = TemplatesRequestDto.from_json(json)
# print the JSON string representation of the object
print(TemplatesRequestDto.to_json())

# convert the object into a dict
templates_request_dto_dict = templates_request_dto_instance.to_dict()
# create an instance of TemplatesRequestDto from a dict
templates_request_dto_from_dict = TemplatesRequestDto.from_dict(templates_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


