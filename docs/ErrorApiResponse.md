# ErrorApiResponse
The error body returned with every failed request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | The response status flag. Always 1 on an error, as opposed to 0 on success. | [optional] 
**status_code** | **int** | The HTTP status code of the response, repeated in the body. | [optional] 
**error** | [**ErrorApiResponseError**](ErrorApiResponseError.md) |  | [optional] 

## Example

```python
from docspace_api_sdk.models.error_api_response import ErrorApiResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorApiResponse from a JSON string
error_api_response_instance = ErrorApiResponse.from_json(json)
# print the JSON string representation of the object
print(ErrorApiResponse.to_json())

# convert the object into a dict
error_api_response_dict = error_api_response_instance.to_dict()
# create an instance of ErrorApiResponse from a dict
error_api_response_from_dict = ErrorApiResponse.from_dict(error_api_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


