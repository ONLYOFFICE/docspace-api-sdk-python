# AiErrorResponse
Error body — a single human-readable message.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** | The error message, ready to be shown to the caller. | 

## Example

```python
from docspace_api_sdk.models.ai_error_response import AiErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AiErrorResponse from a JSON string
ai_error_response_instance = AiErrorResponse.from_json(json)
# print the JSON string representation of the object
print(AiErrorResponse.to_json())

# convert the object into a dict
ai_error_response_dict = ai_error_response_instance.to_dict()
# create an instance of AiErrorResponse from a dict
ai_error_response_from_dict = AiErrorResponse.from_dict(ai_error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


