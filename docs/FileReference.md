# FileReference
The file reference parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference_data** | [**FileReferenceData**](FileReferenceData.md) |  | [optional] 
**error** | **str** | The error message text. | [optional] 
**path** | **str** | The file name or relative path for the formula editor. | [optional] 
**url** | **str** | The URL address to download the current file. | [optional] 
**file_type** | **str** | An extension of the document specified with the url parameter. | [optional] 
**key** | **str** | The unique document identifier used by the service to take the data from the co-editing session. | [optional] 
**link** | **str** | The file URL. | [optional] 
**token** | **str** | The encrypted signature added to the parameter in the form of a token. | [optional] 

## Example

```python
from docspace_api_sdk.models.file_reference import FileReference

# TODO update the JSON string below
json = "{}"
# create an instance of FileReference from a JSON string
file_reference_instance = FileReference.from_json(json)
# print the JSON string representation of the object
print(FileReference.to_json())

# convert the object into a dict
file_reference_dict = file_reference_instance.to_dict()
# create an instance of FileReference from a dict
file_reference_from_dict = FileReference.from_dict(file_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


