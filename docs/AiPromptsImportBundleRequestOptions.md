# AiPromptsImportBundleRequestOptions
Import options.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | [**AiImportMode**](AiImportMode.md) |  | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_prompts_import_bundle_request_options import AiPromptsImportBundleRequestOptions

# TODO update the JSON string below
json = "{}"
# create an instance of AiPromptsImportBundleRequestOptions from a JSON string
ai_prompts_import_bundle_request_options_instance = AiPromptsImportBundleRequestOptions.from_json(json)
# print the JSON string representation of the object
print(AiPromptsImportBundleRequestOptions.to_json())

# convert the object into a dict
ai_prompts_import_bundle_request_options_dict = ai_prompts_import_bundle_request_options_instance.to_dict()
# create an instance of AiPromptsImportBundleRequestOptions from a dict
ai_prompts_import_bundle_request_options_from_dict = AiPromptsImportBundleRequestOptions.from_dict(ai_prompts_import_bundle_request_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


