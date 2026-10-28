# TemplatesRequestDto
The files to put on the personal template list of the calling account.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_ids** | **List[int]** | The files to put on the template list, by id, as reported by a folder listing such as  `GET api/2.0/files/{folderId}`. Only a file stored in the portal itself can become a template, which is why an  id here is always numeric. | [optional] 

## Example

```python
from docspace_api_sdk.models.templates_request_dto import TemplatesRequestDto

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


