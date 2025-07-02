# StartFillingForm
The parameters of the button that starts filling out the form.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | The caption of the button that starts filling out the form. | [optional] 

## Example

```python
from docspace-api-python.models.start_filling_form import StartFillingForm

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


