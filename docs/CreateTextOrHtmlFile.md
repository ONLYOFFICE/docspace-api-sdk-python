# CreateTextOrHtmlFile
The parameters for creating an HTML or text file.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The file title for text or HTML file. | 
**content** | **str** | The text or HTML file contents. | [optional] 
**create_new_if_exist** | **bool** | Specifies whether to create a new text or HTML file if it exists or not. | [optional] 

## Example

```python
from docspace_api_sdk.models.create_text_or_html_file import CreateTextOrHtmlFile

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTextOrHtmlFile from a JSON string
create_text_or_html_file_instance = CreateTextOrHtmlFile.from_json(json)
# print the JSON string representation of the object
print(CreateTextOrHtmlFile.to_json())

# convert the object into a dict
create_text_or_html_file_dict = create_text_or_html_file_instance.to_dict()
# create an instance of CreateTextOrHtmlFile from a dict
create_text_or_html_file_from_dict = CreateTextOrHtmlFile.from_dict(create_text_or_html_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


