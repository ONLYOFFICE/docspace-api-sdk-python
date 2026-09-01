# AiPromptsImportBundleRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bundle** | [**AiPromptBundle**](AiPromptBundle.md) | Bundle to restore. | 
**options** | [**AiPromptsImportBundleRequestOptions**](AiPromptsImportBundleRequestOptions.md) |  | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_prompts_import_bundle_request import AiPromptsImportBundleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AiPromptsImportBundleRequest from a JSON string
ai_prompts_import_bundle_request_instance = AiPromptsImportBundleRequest.from_json(json)
# print the JSON string representation of the object
print(AiPromptsImportBundleRequest.to_json())

# convert the object into a dict
ai_prompts_import_bundle_request_dict = ai_prompts_import_bundle_request_instance.to_dict()
# create an instance of AiPromptsImportBundleRequest from a dict
ai_prompts_import_bundle_request_from_dict = AiPromptsImportBundleRequest.from_dict(ai_prompts_import_bundle_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


