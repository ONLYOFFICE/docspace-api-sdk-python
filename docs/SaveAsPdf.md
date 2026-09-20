# SaveAsPdf
The place and the name the PDF copy of a file is stored under.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**folder_id** | **int** | The folder the PDF is created in; the caller has to be allowed to create files there. | 
**title** | **str** | The name of the PDF, without an extension - `.pdf` is appended. Left empty, the name of the source file is  reused with its extension replaced. | 

## Example

```python
from docspace_api_sdk.models.save_as_pdf import SaveAsPdf

# TODO update the JSON string below
json = "{}"
# create an instance of SaveAsPdf from a JSON string
save_as_pdf_instance = SaveAsPdf.from_json(json)
# print the JSON string representation of the object
print(SaveAsPdf.to_json())

# convert the object into a dict
save_as_pdf_dict = save_as_pdf_instance.to_dict()
# create an instance of SaveAsPdf from a dict
save_as_pdf_from_dict = SaveAsPdf.from_dict(save_as_pdf_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


