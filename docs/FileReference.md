# FileReference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference_data** | [**FileReferenceData**](FileReferenceData.md) |  | [optional] 
**error** | **str** | Error | [optional] 
**path** | **str** | Path | [optional] 
**url** | **str** | URL | [optional] 
**file_type** | **str** | File type | [optional] 
**key** | **str** | Key | [optional] 
**link** | **str** | Link | [optional] 
**token** | **str** | Token | [optional] 

## Example

```python
from docspace.models.file_reference import FileReference

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


