# CheckFillFormDraft
The parameters for checking the form draft filling.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **int** | The file version of the form draft. | [optional] 
**action** | **str** | The action with the form draft. | [optional] 
**request_view** | **bool** | Specifies whether to request the form for viewing or not. | [optional] [readonly] 
**request_embedded** | **bool** | Specifies whether to request an embedded form or not. | [optional] [readonly] 

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


