# CopyAsJsonElement
The parameters for copying a file.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dest_title** | **str** | The copied file name. | 
**dest_folder_id** | [**CopyAsJsonElementDestFolderId**](CopyAsJsonElementDestFolderId.md) |  | 
**enable_external_ext** | **bool** | Specifies whether to allow creating the copied file of an external extension or not. | [optional] 
**password** | **str** | The copied file password. | [optional] 
**to_form** | **bool** | Specifies whether to convert the file to form or not. | [optional] 

## Example

```python
from docspace_api_sdk.models.copy_as_json_element import CopyAsJsonElement

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


