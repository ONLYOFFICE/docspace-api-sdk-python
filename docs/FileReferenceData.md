# FileReferenceData
The pair of values that names a document across portals, as it is written into a spreadsheet formula.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_key** | **str** | The id of the document inside the portal named below. | [optional] 
**instance_id** | **str** | The portal the document lives in. A reference whose value is not this portal cannot be resolved by the file  key and falls back to the path or the link. | [optional] 
**room_id** | **str** | The room the document lies in. It is filled in only for a document opened in a virtual data room, and stays  empty everywhere else. | [optional] 
**can_edit_room** | **bool** | Whether the caller may manage the room named above; it is only meaningful together with it. | [optional] 

## Example

```python
from docspace_api_sdk.models.file_reference_data import FileReferenceData

# TODO update the JSON string below
json = "{}"
# create an instance of FileReferenceData from a JSON string
file_reference_data_instance = FileReferenceData.from_json(json)
# print the JSON string representation of the object
print(FileReferenceData.to_json())

# convert the object into a dict
file_reference_data_dict = file_reference_data_instance.to_dict()
# create an instance of FileReferenceData from a dict
file_reference_data_from_dict = FileReferenceData.from_dict(file_reference_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


