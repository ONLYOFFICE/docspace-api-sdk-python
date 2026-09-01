# AiTProvider
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
from docspace_api_sdk.models.ai_t_provider import AiTProvider

# TODO update the JSON string below
json = "{}"
# create an instance of AiTProvider from a JSON string
ai_t_provider_instance = AiTProvider.from_json(json)
# print the JSON string representation of the object
print(AiTProvider.to_json())

# convert the object into a dict
ai_t_provider_dict = ai_t_provider_instance.to_dict()
# create an instance of AiTProvider from a dict
ai_t_provider_from_dict = AiTProvider.from_dict(ai_t_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


