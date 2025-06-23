# DraftLocationInteger

The file draft parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**folder_id** | **int** | The InProcess folder ID of the draft. | [optional] 
**folder_title** | **str** | The InProcess folder title of the draft. | [optional] 
**file_id** | **int** | The draft ID. | [optional] 
**file_title** | **str** | The draft title. | [optional] 

## Example

```python
from docspace.models.draft_location_integer import DraftLocationInteger

# TODO update the JSON string below
json = "{}"
# create an instance of DraftLocationInteger from a JSON string
draft_location_integer_instance = DraftLocationInteger.from_json(json)
# print the JSON string representation of the object
print(DraftLocationInteger.to_json())

# convert the object into a dict
draft_location_integer_dict = draft_location_integer_instance.to_dict()
# create an instance of DraftLocationInteger from a dict
draft_location_integer_from_dict = DraftLocationInteger.from_dict(draft_location_integer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


