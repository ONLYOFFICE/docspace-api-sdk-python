# DocumentOptionsDto
The document options the editor applies when it opens the file.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**watermark_on_draw** | [**WatermarkOnDrawDto**](WatermarkOnDrawDto.md) | The document watermark parameters. | [optional] 

## Example

```python
from docspace_api_sdk.models.document_options_dto import DocumentOptionsDto

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentOptionsDto from a JSON string
document_options_dto_instance = DocumentOptionsDto.from_json(json)
# print the JSON string representation of the object
print(DocumentOptionsDto.to_json())

# convert the object into a dict
document_options_dto_dict = document_options_dto_instance.to_dict()
# create an instance of DocumentOptionsDto from a dict
document_options_dto_from_dict = DocumentOptionsDto.from_dict(document_options_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


