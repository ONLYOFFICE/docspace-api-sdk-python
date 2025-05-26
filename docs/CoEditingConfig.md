# CoEditingConfig

The co-editing configuration parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**change** | **bool** | Specifies if the co-editing mode can be changed in the editor interface or not. | [optional] 
**fast** | **bool** | Specifies if the co-editing mode is fast. | [optional] 
**mode** | [**CoEditingConfigMode**](CoEditingConfigMode.md) |  | [optional] 

## Example

```python
from docspace.models.co_editing_config import CoEditingConfig

# TODO update the JSON string below
json = "{}"
# create an instance of CoEditingConfig from a JSON string
co_editing_config_instance = CoEditingConfig.from_json(json)
# print the JSON string representation of the object
print(CoEditingConfig.to_json())

# convert the object into a dict
co_editing_config_dict = co_editing_config_instance.to_dict()
# create an instance of CoEditingConfig from a dict
co_editing_config_from_dict = CoEditingConfig.from_dict(co_editing_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


