# AiMetaGenerate402Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** | Short reason, ready to be shown to the caller. | 
**code** | **str** | Stable classification of the failure: `rate_limit`, `insufficient_funds`, `auth`, `model_not_found`, `timeout`, `network`, `bad_request`, `server`, `unknown`, or a provider-specific code relayed as it came. | 
**provider_message** | **str** | The provider's own error message, cut to 500 characters. Absent when the failure never reached the provider, or was a timeout. | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_meta_generate402_response import AiMetaGenerate402Response

# TODO update the JSON string below
json = "{}"
# create an instance of AiMetaGenerate402Response from a JSON string
ai_meta_generate402_response_instance = AiMetaGenerate402Response.from_json(json)
# print the JSON string representation of the object
print(AiMetaGenerate402Response.to_json())

# convert the object into a dict
ai_meta_generate402_response_dict = ai_meta_generate402_response_instance.to_dict()
# create an instance of AiMetaGenerate402Response from a dict
ai_meta_generate402_response_from_dict = AiMetaGenerate402Response.from_dict(ai_meta_generate402_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


