# AiPromptBundle
Versioned, self-contained bundle of every saved prompt and folder. Stable wire format — `version` lets the import path migrate older shapes if the schema ever changes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **float** | The bundle format version, so an import can migrate an older export. | 
**folders** | [**List[AiPromptFolder]**](AiPromptFolder.md) | Every exported prompt folder. | 
**prompts** | [**List[AiPrompt]**](AiPrompt.md) | Every exported prompt. | 

## Example

```python
from docspace_api_sdk.models.ai_prompt_bundle import AiPromptBundle

# TODO update the JSON string below
json = "{}"
# create an instance of AiPromptBundle from a JSON string
ai_prompt_bundle_instance = AiPromptBundle.from_json(json)
# print the JSON string representation of the object
print(AiPromptBundle.to_json())

# convert the object into a dict
ai_prompt_bundle_dict = ai_prompt_bundle_instance.to_dict()
# create an instance of AiPromptBundle from a dict
ai_prompt_bundle_from_dict = AiPromptBundle.from_dict(ai_prompt_bundle_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


