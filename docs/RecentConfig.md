# RecentConfig
The presence or absence of the documents in the \"Open Recent...\" menu option.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**folder** | **str** | The folder where the document is stored. | [optional] 
**title** | **str** | The document title that will be displayed in the Open Recent... menu option. | [optional] 
**url** | **str** | The absolute URL to the document where it is stored. | [optional] 

## Example

```python
from docspace_api_sdk.models.recent_config import RecentConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RecentConfig from a JSON string
recent_config_instance = RecentConfig.from_json(json)
# print the JSON string representation of the object
print(RecentConfig.to_json())

# convert the object into a dict
recent_config_dict = recent_config_instance.to_dict()
# create an instance of RecentConfig from a dict
recent_config_from_dict = RecentConfig.from_dict(recent_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


