# Run
The text run parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fill** | **List[int]** | The fill color of the text run in RGB format. | [optional] 
**text** | **str** | The run text. | [optional] 
**font_size** | **str** | The font size of the text run in points. | [optional] 

## Example

```python
from docspace-api-python.models.run import Run

# TODO update the JSON string below
json = "{}"
# create an instance of Run from a JSON string
run_instance = Run.from_json(json)
# print the JSON string representation of the object
print(Run.to_json())

# convert the object into a dict
run_dict = run_instance.to_dict()
# create an instance of Run from a dict
run_from_dict = Run.from_dict(run_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


