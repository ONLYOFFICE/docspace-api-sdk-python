# RestrictedModelsResponseWrapper
The successful API response containing the RestrictedModelsResponse object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**RestrictedModelsResponse**](RestrictedModelsResponse.md) | The RestrictedModelsResponse object returned by the operation. | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.restricted_models_response_wrapper import RestrictedModelsResponseWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of RestrictedModelsResponseWrapper from a JSON string
restricted_models_response_wrapper_instance = RestrictedModelsResponseWrapper.from_json(json)
# print the JSON string representation of the object
print(RestrictedModelsResponseWrapper.to_json())

# convert the object into a dict
restricted_models_response_wrapper_dict = restricted_models_response_wrapper_instance.to_dict()
# create an instance of RestrictedModelsResponseWrapper from a dict
restricted_models_response_wrapper_from_dict = RestrictedModelsResponseWrapper.from_dict(restricted_models_response_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


