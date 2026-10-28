# AiErrorData
A field-scoped validation error: which form field was rejected, and why.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | The rejected field. | 
**message** | **str** | The human-readable reason the field was rejected. | 
**code** | [**AiErrorCode**](AiErrorCode.md) | Optional: producers that know the reason set it (the prompts engine does). | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_error_data import AiErrorData

# TODO update the JSON string below
json = "{}"
# create an instance of AiErrorData from a JSON string
ai_error_data_instance = AiErrorData.from_json(json)
# print the JSON string representation of the object
print(AiErrorData.to_json())

# convert the object into a dict
ai_error_data_dict = ai_error_data_instance.to_dict()
# create an instance of AiErrorData from a dict
ai_error_data_from_dict = AiErrorData.from_dict(ai_error_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


