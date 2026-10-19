# AiProfilesCreate400Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | True when the profile was persisted. | 
**profile** | [**AiProfile**](AiProfile.md) | The persisted profile. Present on success. | [optional] 
**error** | **str** | The error message, ready to be shown to the caller. | 

## Example

```python
from docspace_api_sdk.models.ai_profiles_create400_response import AiProfilesCreate400Response

# TODO update the JSON string below
json = "{}"
# create an instance of AiProfilesCreate400Response from a JSON string
ai_profiles_create400_response_instance = AiProfilesCreate400Response.from_json(json)
# print the JSON string representation of the object
print(AiProfilesCreate400Response.to_json())

# convert the object into a dict
ai_profiles_create400_response_dict = ai_profiles_create400_response_instance.to_dict()
# create an instance of AiProfilesCreate400Response from a dict
ai_profiles_create400_response_from_dict = AiProfilesCreate400Response.from_dict(ai_profiles_create400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


