# CreateTextOrHtmlFileRequest
The parameters of a text or HTML file created from content sent in the request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The title of the file. The extension the operation stands for is appended unless the title already ends with  it, so Notes becomes Notes.txt or Notes.html. | 
**content** | **str** | The content of the file, as plain text or as HTML markup. A request carrying none is rejected as an invalid  request, and for a text file content that looks like markup makes the portal store it as HTML instead. | [optional] 
**create_new_if_exist** | **bool** | What to do when the folder already holds a file of this title, the other way round than the name reads: `true`  updates that file and adds a version to its history, `false` creates another file and makes its title unique,  as in Notes (1).txt. | [optional] 

## Example

```python
from docspace_api_sdk.models.create_text_or_html_file_request import CreateTextOrHtmlFileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTextOrHtmlFileRequest from a JSON string
create_text_or_html_file_request_instance = CreateTextOrHtmlFileRequest.from_json(json)
# print the JSON string representation of the object
print(CreateTextOrHtmlFileRequest.to_json())

# convert the object into a dict
create_text_or_html_file_request_dict = create_text_or_html_file_request_instance.to_dict()
# create an instance of CreateTextOrHtmlFileRequest from a dict
create_text_or_html_file_request_from_dict = CreateTextOrHtmlFileRequest.from_dict(create_text_or_html_file_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


