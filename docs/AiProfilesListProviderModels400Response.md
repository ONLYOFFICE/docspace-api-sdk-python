# AiProfilesListProviderModels400Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** | The error message, ready to be shown to the caller. | 
**var_field** | **str** | Name of the request field that was missing or rejected. | 

## Example

```python
from docspace_api_sdk.models.ai_profiles_list_provider_models400_response import AiProfilesListProviderModels400Response

# TODO update the JSON string below
json = "{}"
# create an instance of AiProfilesListProviderModels400Response from a JSON string
ai_profiles_list_provider_models400_response_instance = AiProfilesListProviderModels400Response.from_json(json)
# print the JSON string representation of the object
print(AiProfilesListProviderModels400Response.to_json())

# convert the object into a dict
ai_profiles_list_provider_models400_response_dict = ai_profiles_list_provider_models400_response_instance.to_dict()
# create an instance of AiProfilesListProviderModels400Response from a dict
ai_profiles_list_provider_models400_response_from_dict = AiProfilesListProviderModels400Response.from_dict(ai_profiles_list_provider_models400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


