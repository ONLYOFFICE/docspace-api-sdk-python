# AiProjectModelProfile

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The profile id. | 
**name** | **str** | The profile name; empty when the profile is gone. | 
**provider** | **str** | The provider type of the profile; `null` when the profile is gone. | 
**available** | **bool** | `false` when the profile is gone or cannot chat: the project's rounds are refused. | 

## Example

```python
from docspace_api_sdk.models.ai_project_model_profile import AiProjectModelProfile

# TODO update the JSON string below
json = "{}"
# create an instance of AiProjectModelProfile from a JSON string
ai_project_model_profile_instance = AiProjectModelProfile.from_json(json)
# print the JSON string representation of the object
print(AiProjectModelProfile.to_json())

# convert the object into a dict
ai_project_model_profile_dict = ai_project_model_profile_instance.to_dict()
# create an instance of AiProjectModelProfile from a dict
ai_project_model_profile_from_dict = AiProjectModelProfile.from_dict(ai_project_model_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


