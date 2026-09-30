# ThirdPartySaveAsPdf
The place and the name the PDF copy of a file is stored under.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**folder_id** | **str** | The folder the PDF is created in; the caller has to be allowed to create files there. | 
**title** | **str** | The name of the PDF, without an extension - `.pdf` is appended. Left empty, the name of the source file is  reused with its extension replaced. | 

## Example

```python
from docspace_api_sdk.models.third_party_save_as_pdf import ThirdPartySaveAsPdf

# TODO update the JSON string below
json = "{}"
# create an instance of ThirdPartySaveAsPdf from a JSON string
third_party_save_as_pdf_instance = ThirdPartySaveAsPdf.from_json(json)
# print the JSON string representation of the object
print(ThirdPartySaveAsPdf.to_json())

# convert the object into a dict
third_party_save_as_pdf_dict = third_party_save_as_pdf_instance.to_dict()
# create an instance of ThirdPartySaveAsPdf from a dict
third_party_save_as_pdf_from_dict = ThirdPartySaveAsPdf.from_dict(third_party_save_as_pdf_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


