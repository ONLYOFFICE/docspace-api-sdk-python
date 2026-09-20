# GobackConfig
The settings for the Open file location menu button and upper right corner button.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | Where the user is taken when they leave the document, normally the folder or the room it lies in. It is empty  when there is nowhere to return to, as in a framed opening. | [optional] 

## Example

```python
from docspace_api_sdk.models.goback_config import GobackConfig

# TODO update the JSON string below
json = "{}"
# create an instance of GobackConfig from a JSON string
goback_config_instance = GobackConfig.from_json(json)
# print the JSON string representation of the object
print(GobackConfig.to_json())

# convert the object into a dict
goback_config_dict = goback_config_instance.to_dict()
# create an instance of GobackConfig from a dict
goback_config_from_dict = GobackConfig.from_dict(goback_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


