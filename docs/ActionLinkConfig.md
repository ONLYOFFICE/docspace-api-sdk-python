# ActionLinkConfig
The place inside a document that a link should open at.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**ActionConfig**](ActionConfig.md) | The anchor itself. It is passed on to the editor unchanged, so it has to be the value the editor produced for  the comment or the mention it points at. | [optional] 

## Example

```python
from docspace_api_sdk.models.action_link_config import ActionLinkConfig

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


