# CreateFileRequest
The parameters of a file that the portal creates from a template or a blank document.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The title of the new file. The extension in it decides the format, and one of a known text, spreadsheet or  presentation format is rewritten to the DOCX, XLSX or PPTX of the portal unless `enableExternalExt` says  otherwise; a title with no extension gets DOCX added. | 
**template_id** | [**CreateFileRequestTemplateId**](CreateFileRequestTemplateId.md) |  | [optional] 
**enable_external_ext** | **bool** | Whether the extension of the title is kept as it is: `true` stores the title verbatim, `false` rewrites a  known foreign format to the format the portal edits itself. | [optional] 
**form_id** | **int** | A ready form from the form gallery of the portal to copy instead of a template, named by the identifier the  gallery reports for it. It takes precedence over `templateId`; 0 means no form. | [optional] 

## Example

```python
from docspace_api_sdk.models.create_file_request import CreateFileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFileRequest from a JSON string
create_file_request_instance = CreateFileRequest.from_json(json)
# print the JSON string representation of the object
print(CreateFileRequest.to_json())

# convert the object into a dict
create_file_request_dict = create_file_request_instance.to_dict()
# create an instance of CreateFileRequest from a dict
create_file_request_from_dict = CreateFileRequest.from_dict(create_file_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


