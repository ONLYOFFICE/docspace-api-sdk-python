# DraftLocation
Where the caller's own filling draft of a form is kept.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**folder_id** | **int** | The folder holding the draft: the sub-folder that the room for filling keeps for drafts of this particular  form. | [optional] 
**folder_title** | **str** | The title of that folder, which the portal takes from the form itself when the form is released for filling. | [optional] 
**file_id** | **int** | The draft itself - the copy the caller fills in, not the original form, and the identifier to pass to the file  operations while filling. | [optional] 
**file_title** | **str** | The title of the draft, which the portal builds from the name of the person filling it and the name of the  form. Null when the draft the record points at no longer exists. | [optional] 

## Example

```python
from docspace_api_sdk.models.draft_location import DraftLocation

# TODO update the JSON string below
json = "{}"
# create an instance of DraftLocation from a JSON string
draft_location_instance = DraftLocation.from_json(json)
# print the JSON string representation of the object
print(DraftLocation.to_json())

# convert the object into a dict
draft_location_dict = draft_location_instance.to_dict()
# create an instance of DraftLocation from a dict
draft_location_from_dict = DraftLocation.from_dict(draft_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


