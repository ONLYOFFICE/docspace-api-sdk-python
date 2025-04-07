# CopyAsJsonElement

Parameters for copying a file

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dest_title** | **str** | Destination file title | [optional] 
**dest_folder_id** | [**BatchRequestDtoDestFolderId**](BatchRequestDtoDestFolderId.md) |  | [optional] 
**enable_external_ext** | **bool** | Specifies whether to allow the creation of external extension files or not | [optional] 
**password** | **str** | Password | [optional] 
**to_form** | **bool** | Convert to form | [optional] 

## Example

```python
from docspace.models.copy_as_json_element import CopyAsJsonElement

# TODO update the JSON string below
json = "{}"
# create an instance of CopyAsJsonElement from a JSON string
copy_as_json_element_instance = CopyAsJsonElement.from_json(json)
# print the JSON string representation of the object
print(CopyAsJsonElement.to_json())

# convert the object into a dict
copy_as_json_element_dict = copy_as_json_element_instance.to_dict()
# create an instance of CopyAsJsonElement from a dict
copy_as_json_element_from_dict = CopyAsJsonElement.from_dict(copy_as_json_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


