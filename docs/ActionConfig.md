# ActionConfig
The information about the action in the document that will be scrolled to.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **str** | The action data that will be scrolled to. | [optional] 
**type** | **str** | The action type. | [optional] 

## Example

```python
from docspace_api_sdk.models.action_config import ActionConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ActionConfig from a JSON string
action_config_instance = ActionConfig.from_json(json)
# print the JSON string representation of the object
print(ActionConfig.to_json())

# convert the object into a dict
action_config_dict = action_config_instance.to_dict()
# create an instance of ActionConfig from a dict
action_config_from_dict = ActionConfig.from_dict(action_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


