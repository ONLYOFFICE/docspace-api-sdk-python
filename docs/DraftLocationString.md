# DraftLocationString
The file draft parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**folder_id** | **str** | The InProcess folder ID of the draft. | [optional] 
**folder_title** | **str** | The InProcess folder title of the draft. | [optional] 
**file_id** | **str** | The draft ID. | [optional] 
**file_title** | **str** | The draft title. | [optional] 

## Example

```python
from docspace_api_sdk.models.draft_location_string import DraftLocationString

# TODO update the JSON string below
json = "{}"
# create an instance of DraftLocationString from a JSON string
draft_location_string_instance = DraftLocationString.from_json(json)
# print the JSON string representation of the object
print(DraftLocationString.to_json())

# convert the object into a dict
draft_location_string_dict = draft_location_string_instance.to_dict()
# create an instance of DraftLocationString from a dict
draft_location_string_from_dict = DraftLocationString.from_dict(draft_location_string_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


