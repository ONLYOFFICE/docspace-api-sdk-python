# AiProvider
Minimal provider connection configuration. Used to connect to a provider API.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**AiProviderType**](AiProviderType.md) | Provider type identifier. | 
**name** | **str** | User-defined display name for this provider connection. | 
**key** | **str** | API key or token. Optional for local providers (Ollama, LM Studio). | [optional] 
**base_url** | **str** | Base URL of the provider API. | 

## Example

```python
from docspace_api_sdk.models.ai_provider import AiProvider

# TODO update the JSON string below
json = "{}"
# create an instance of AiProvider from a JSON string
ai_provider_instance = AiProvider.from_json(json)
# print the JSON string representation of the object
print(AiProvider.to_json())

# convert the object into a dict
ai_provider_dict = ai_provider_instance.to_dict()
# create an instance of AiProvider from a dict
ai_provider_from_dict = AiProvider.from_dict(ai_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


