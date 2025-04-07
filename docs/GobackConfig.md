# GobackConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | Url | [optional] 

## Example

```python
from docspace.models.goback_config import GobackConfig

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


