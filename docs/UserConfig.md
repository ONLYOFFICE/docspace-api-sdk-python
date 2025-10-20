# UserConfig
The configuration parameters of the user currently viewing or editing the document.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The user ID. | [optional] 
**name** | **str** | The full name of the user. | [optional] 
**image** | **str** | The path to the user&#39;s avatar. | [optional] 
**roles** | **List[str]** | Roles | [optional] 

## Example

```python
from docspace_api_sdk.models.user_config import UserConfig

# TODO update the JSON string below
json = "{}"
# create an instance of UserConfig from a JSON string
user_config_instance = UserConfig.from_json(json)
# print the JSON string representation of the object
print(UserConfig.to_json())

# convert the object into a dict
user_config_dict = user_config_instance.to_dict()
# create an instance of UserConfig from a dict
user_config_from_dict = UserConfig.from_dict(user_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


