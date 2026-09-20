# TokenDiagnosticsWrapper
The successful API response containing the TokenDiagnosticsDto object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**TokenDiagnosticsDto**](TokenDiagnosticsDto.md) | The TokenDiagnosticsDto object returned by the operation. | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.token_diagnostics_wrapper import TokenDiagnosticsWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of TokenDiagnosticsWrapper from a JSON string
token_diagnostics_wrapper_instance = TokenDiagnosticsWrapper.from_json(json)
# print the JSON string representation of the object
print(TokenDiagnosticsWrapper.to_json())

# convert the object into a dict
token_diagnostics_wrapper_dict = token_diagnostics_wrapper_instance.to_dict()
# create an instance of TokenDiagnosticsWrapper from a dict
token_diagnostics_wrapper_from_dict = TokenDiagnosticsWrapper.from_dict(token_diagnostics_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


