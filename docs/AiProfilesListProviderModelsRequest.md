# AiProfilesListProviderModelsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_type** | [**AiProviderType**](AiProviderType.md) | Provider whose catalog to list. | 
**base_url** | **str** | Provider API base URL. | 
**api_key** | **str** | Provider API key. | 

## Example

```python
from docspace_api_sdk.models.ai_profiles_list_provider_models_request import AiProfilesListProviderModelsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AiProfilesListProviderModelsRequest from a JSON string
ai_profiles_list_provider_models_request_instance = AiProfilesListProviderModelsRequest.from_json(json)
# print the JSON string representation of the object
print(AiProfilesListProviderModelsRequest.to_json())

# convert the object into a dict
ai_profiles_list_provider_models_request_dict = ai_profiles_list_provider_models_request_instance.to_dict()
# create an instance of AiProfilesListProviderModelsRequest from a dict
ai_profiles_list_provider_models_request_from_dict = AiProfilesListProviderModelsRequest.from_dict(ai_profiles_list_provider_models_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


