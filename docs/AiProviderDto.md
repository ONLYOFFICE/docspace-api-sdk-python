# AiProviderDto
AI provider details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | AI provider identifier. | [optional] 
**title** | **str** | AI provider display title. | 
**type** | [**ProviderType**](ProviderType.md) |  | [optional] 
**url** | **str** | API endpoint URL for the AI provider. | [optional] 
**created_on** | [**ApiDateTime**](ApiDateTime.md) |  | 
**modified_on** | [**ApiDateTime**](ApiDateTime.md) |  | 
**need_reset** | **bool** | Indicates whether the provider's API key needs to be reset. | [optional] 
**is_default** | **bool** | Indicates whether this provider is the default provider for the tenant. | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_provider_dto import AiProviderDto

# TODO update the JSON string below
json = "{}"
# create an instance of AiProviderDto from a JSON string
ai_provider_dto_instance = AiProviderDto.from_json(json)
# print the JSON string representation of the object
print(AiProviderDto.to_json())

# convert the object into a dict
ai_provider_dto_dict = ai_provider_dto_instance.to_dict()
# create an instance of AiProviderDto from a dict
ai_provider_dto_from_dict = AiProviderDto.from_dict(ai_provider_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


