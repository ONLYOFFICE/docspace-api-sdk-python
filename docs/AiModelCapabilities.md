# AiModelCapabilities
The AI model capabilities.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vision** | **bool** | Indicates whether the model supports image and vision input. | [optional] 
**tool_calling** | **bool** | Indicates whether the model supports tool (function) calling. | [optional] 
**thinking** | **bool** | Indicates whether the model supports extended thinking and reasoning. | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_model_capabilities import AiModelCapabilities

# TODO update the JSON string below
json = "{}"
# create an instance of AiModelCapabilities from a JSON string
ai_model_capabilities_instance = AiModelCapabilities.from_json(json)
# print the JSON string representation of the object
print(AiModelCapabilities.to_json())

# convert the object into a dict
ai_model_capabilities_dict = ai_model_capabilities_instance.to_dict()
# create an instance of AiModelCapabilities from a dict
ai_model_capabilities_from_dict = AiModelCapabilities.from_dict(ai_model_capabilities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


