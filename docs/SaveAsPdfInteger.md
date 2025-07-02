# SaveAsPdfInteger
The parameters for saving the file as PDF.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**folder_id** | **int** | The folder ID to save the file as PDF. | 
**title** | **str** | The file title to save as PDF. | 

## Example

```python
from docspace-api-python.models.save_as_pdf_integer import SaveAsPdfInteger

# TODO update the JSON string below
json = "{}"
# create an instance of SaveAsPdfInteger from a JSON string
save_as_pdf_integer_instance = SaveAsPdfInteger.from_json(json)
# print the JSON string representation of the object
print(SaveAsPdfInteger.to_json())

# convert the object into a dict
save_as_pdf_integer_dict = save_as_pdf_integer_instance.to_dict()
# create an instance of SaveAsPdfInteger from a dict
save_as_pdf_integer_from_dict = SaveAsPdfInteger.from_dict(save_as_pdf_integer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


