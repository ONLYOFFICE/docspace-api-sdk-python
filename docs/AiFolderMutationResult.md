# AiFolderMutationResult
Outcome of `createFolder` / `renameFolder` — either the persisted folder or a field-scoped error.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**folder** | [**AiPromptFolder**](AiPromptFolder.md) |  | [optional] 
**error** | [**AiTErrorData**](AiTErrorData.md) |  | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_folder_mutation_result import AiFolderMutationResult

# TODO update the JSON string below
json = "{}"
# create an instance of AiFolderMutationResult from a JSON string
ai_folder_mutation_result_instance = AiFolderMutationResult.from_json(json)
# print the JSON string representation of the object
print(AiFolderMutationResult.to_json())

# convert the object into a dict
ai_folder_mutation_result_dict = ai_folder_mutation_result_instance.to_dict()
# create an instance of AiFolderMutationResult from a dict
ai_folder_mutation_result_from_dict = AiFolderMutationResult.from_dict(ai_folder_mutation_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


