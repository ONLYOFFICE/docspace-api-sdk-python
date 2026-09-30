# CoEditingConfig
How co-editing is preset when the document opens, and whether the user may switch it afterwards.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**change** | **bool** | Whether the user may switch between the two co-editing modes from the editor interface, or is held to the one  the portal preset. | [optional] 
**fast** | **bool** | Whether other participants see each change as it is typed. Left off, changes are exchanged only when a  participant saves, and the paragraph being edited is locked for the others meanwhile. | [optional] 
**mode** | [**CoEditingConfigMode**](CoEditingConfigMode.md) | The mode the two settings above amount to, as the editors name it. | [optional] 

## Example

```python
from docspace_api_sdk.models.co_editing_config import CoEditingConfig

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


