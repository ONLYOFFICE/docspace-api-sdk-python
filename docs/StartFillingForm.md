# StartFillingForm
The button the editor shows to begin filling out a form.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | The caption to put on the button, already translated into the language of the caller. | [optional] 

## Example

```python
from docspace_api_sdk.models.start_filling_form import StartFillingForm

# TODO update the JSON string below
json = "{}"
# create an instance of StartFillingForm from a JSON string
start_filling_form_instance = StartFillingForm.from_json(json)
# print the JSON string representation of the object
print(StartFillingForm.to_json())

# convert the object into a dict
start_filling_form_dict = start_filling_form_instance.to_dict()
# create an instance of StartFillingForm from a dict
start_filling_form_from_dict = StartFillingForm.from_dict(start_filling_form_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


