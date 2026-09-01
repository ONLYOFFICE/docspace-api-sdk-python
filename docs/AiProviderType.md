# AiProviderType
Provider type identifier. Accepts all 17 built-in types with autocomplete, plus any custom `string` for dynamically registered providers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from docspace_api_sdk.models.ai_provider_type import AiProviderType

# TODO update the JSON string below
json = "{}"
# create an instance of AiProviderType from a JSON string
ai_provider_type_instance = AiProviderType.from_json(json)
# print the JSON string representation of the object
print(AiProviderType.to_json())

# convert the object into a dict
ai_provider_type_dict = ai_provider_type_instance.to_dict()
# create an instance of AiProviderType from a dict
ai_provider_type_from_dict = AiProviderType.from_dict(ai_provider_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


