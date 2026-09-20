# CreateFileJsonElement
The parameters of a file that the portal creates from a template or a blank document.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The title of the new file. The extension in it decides the format, and one of a known text, spreadsheet or  presentation format is rewritten to the DOCX, XLSX or PPTX of the portal unless `enableExternalExt` says  otherwise; a title with no extension gets DOCX added. | 
**template_id** | [**CreateFileJsonElementTemplateId**](CreateFileJsonElementTemplateId.md) |  | [optional] 
**enable_external_ext** | **bool** | Whether the extension of the title is kept as it is: `true` stores the title verbatim, `false` rewrites a  known foreign format to the format the portal edits itself. | [optional] 
**form_id** | **int** | A ready form from the form gallery of the portal to copy instead of a template, named by the identifier the  gallery reports for it. It takes precedence over `templateId`; 0 means no form. | [optional] 

## Example

```python
from docspace_api_sdk.models.create_file_json_element import CreateFileJsonElement

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFileJsonElement from a JSON string
create_file_json_element_instance = CreateFileJsonElement.from_json(json)
# print the JSON string representation of the object
print(CreateFileJsonElement.to_json())

# convert the object into a dict
create_file_json_element_dict = create_file_json_element_instance.to_dict()
# create an instance of CreateFileJsonElement from a dict
create_file_json_element_from_dict = CreateFileJsonElement.from_dict(create_file_json_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


