# ActionLinkConfig

The config parameter which contains the information about the action in the document that will be scrolled to.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**ActionConfig**](ActionConfig.md) |  | [optional] 

## Example

```python
from docspace.models.action_link_config import ActionLinkConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ActionLinkConfig from a JSON string
action_link_config_instance = ActionLinkConfig.from_json(json)
# print the JSON string representation of the object
print(ActionLinkConfig.to_json())

# convert the object into a dict
action_link_config_dict = action_link_config_instance.to_dict()
# create an instance of ActionLinkConfig from a dict
action_link_config_from_dict = ActionLinkConfig.from_dict(action_link_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


