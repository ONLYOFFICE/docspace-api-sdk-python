# CopyAsJsonElement
The parameters of a file copy that may change the format on the way.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dest_title** | **str** | The title of the copy, extension included. That extension decides the format: the same one as the source  copies the content as it is, a different one has it converted first. | 
**dest_folder_id** | [**CopyAsJsonElementDestFolderId**](CopyAsJsonElementDestFolderId.md) |  | 
**enable_external_ext** | **bool** | Whether the extension of the new title may be one the portal does not edit itself. | [optional] 
**password** | **str** | The password that opens the source document, for a file that is protected by one. | [optional] 
**to_form** | **bool** | Whether the copy is to become a PDF form rather than a plain document, which the conversion supports for the  text formats it can read. | [optional] 

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


