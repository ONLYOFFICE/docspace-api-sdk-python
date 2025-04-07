# DraftLocationInteger


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**folder_id** | **int** | InProcess folder ID | [optional] 
**folder_title** | **str** | InProcess folder title | [optional] 
**file_id** | **int** | Draft ID | [optional] 
**file_title** | **str** | Draft title | [optional] 

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


