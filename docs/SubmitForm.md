# SubmitForm

The \"Complete & Submit\" button settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**visible** | **bool** | Specifies whether the \&quot;Complete  &amp; Submit\&quot; button will be displayed or hidden on the top toolbar. | [optional] 
**result_message** | **str** | A message displayed after forms are submitted. | [optional] 

## Example

```python
from docspace.models.submit_form import SubmitForm

# TODO update the JSON string below
json = "{}"
# create an instance of SubmitForm from a JSON string
submit_form_instance = SubmitForm.from_json(json)
# print the JSON string representation of the object
print(SubmitForm.to_json())

# convert the object into a dict
submit_form_dict = submit_form_instance.to_dict()
# create an instance of SubmitForm from a dict
submit_form_from_dict = SubmitForm.from_dict(submit_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


