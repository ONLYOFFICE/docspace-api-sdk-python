# CustomFilterParameters

The parameters for setting the Custom Filter editing mode.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Specifies whether the Custom Filter editing mode is enabled or not. | [optional] 

## Example

```python
from docspace.models.custom_filter_parameters import CustomFilterParameters

# TODO update the JSON string below
json = "{}"
# create an instance of CustomFilterParameters from a JSON string
custom_filter_parameters_instance = CustomFilterParameters.from_json(json)
# print the JSON string representation of the object
print(CustomFilterParameters.to_json())

# convert the object into a dict
custom_filter_parameters_dict = custom_filter_parameters_instance.to_dict()
# create an instance of CustomFilterParameters from a dict
custom_filter_parameters_from_dict = CustomFilterParameters.from_dict(custom_filter_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


