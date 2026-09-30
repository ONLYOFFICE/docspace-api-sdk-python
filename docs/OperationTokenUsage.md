# OperationTokenUsage
Tokens an AI operation consumed, as recorded in the operation metadata. A kind the provider did not report is `0`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_tokens** | **int** | All tokens of the request: prompt plus completion. | [optional] 
**prompt_tokens** | **int** | Tokens sent to the model, cached ones included. | [optional] 
**completion_tokens** | **int** | Tokens the model generated, reasoning ones included. | [optional] 
**cached_tokens** | **int** | Part of the prompt tokens read from the provider cache. | [optional] 
**cache_write_tokens** | **int** | Part of the prompt tokens written to the provider cache. | [optional] 
**reasoning_tokens** | **int** | Part of the completion tokens the model spent on reasoning. | [optional] 
**image_tokens** | **int** | Tokens spent on images. | [optional] 

## Example

```python
from docspace_api_sdk.models.operation_token_usage import OperationTokenUsage

# TODO update the JSON string below
json = "{}"
# create an instance of OperationTokenUsage from a JSON string
operation_token_usage_instance = OperationTokenUsage.from_json(json)
# print the JSON string representation of the object
print(OperationTokenUsage.to_json())

# convert the object into a dict
operation_token_usage_dict = operation_token_usage_instance.to_dict()
# create an instance of OperationTokenUsage from a dict
operation_token_usage_from_dict = OperationTokenUsage.from_dict(operation_token_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


