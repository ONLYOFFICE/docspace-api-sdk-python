# ErrorApiResponseError
What went wrong.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | The human-readable error message. | [optional] 
**type** | **str** | The .NET type of the underlying exception. Only sent when stack traces are enabled. | [optional] 
**stack** | **str** | The stack trace of the underlying exception. Only sent when stack traces are enabled. | [optional] 
**hresult** | **int** | The HRESULT of the underlying exception. Only sent when stack traces are enabled. | [optional] 

## Example

```python
from docspace_api_sdk.models.error_api_response_error import ErrorApiResponseError

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorApiResponseError from a JSON string
error_api_response_error_instance = ErrorApiResponseError.from_json(json)
# print the JSON string representation of the object
print(ErrorApiResponseError.to_json())

# convert the object into a dict
error_api_response_error_dict = error_api_response_error_instance.to_dict()
# create an instance of ErrorApiResponseError from a dict
error_api_response_error_from_dict = ErrorApiResponseError.from_dict(error_api_response_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


