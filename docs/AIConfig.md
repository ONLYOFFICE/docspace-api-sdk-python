# AIConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disabled** | **bool** | Indicates whether the AI feature is disabled. | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_config import AIConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AIConfig from a JSON string
ai_config_instance = AIConfig.from_json(json)
# print the JSON string representation of the object
print(AIConfig.to_json())

# convert the object into a dict
ai_config_dict = ai_config_instance.to_dict()
# create an instance of AIConfig from a dict
ai_config_from_dict = AIConfig.from_dict(ai_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


