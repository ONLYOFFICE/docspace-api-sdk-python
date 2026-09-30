# CheckFillFormDraft
The revision of the form to open and what the caller intends to do with it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **int** | The revision of the form to open. Pass 0 for the current revision; a positive number addresses that entry of  the file history and is accepted only from a caller who may read the history, so a member who only has  fill-forms access must send 0. | 
**action** | **str** | What the caller intends to do with the form. `view` asks for a read-only address and `embedded` for an address  to be shown inside a frame; both only resolve the address and leave the file untouched. Leave it out to enter  the filling flow, where the personal draft is created or reused. The value is matched case-insensitively, and  anything else behaves like an empty value. | [optional] 
**request_view** | **bool** | Whether the caller asked for a read-only address. The server derives it from `action` being `view` and ignores  any value sent with the request. | [optional] [readonly] 
**request_embedded** | **bool** | Whether the caller asked for an address to be shown inside a frame. The server derives it from `action` being  `embedded` and ignores any value sent with the request. | [optional] [readonly] 

## Example

```python
from docspace_api_sdk.models.check_fill_form_draft import CheckFillFormDraft

# TODO update the JSON string below
json = "{}"
# create an instance of CheckFillFormDraft from a JSON string
check_fill_form_draft_instance = CheckFillFormDraft.from_json(json)
# print the JSON string representation of the object
print(CheckFillFormDraft.to_json())

# convert the object into a dict
check_fill_form_draft_dict = check_fill_form_draft_instance.to_dict()
# create an instance of CheckFillFormDraft from a dict
check_fill_form_draft_from_dict = CheckFillFormDraft.from_dict(check_fill_form_draft_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


