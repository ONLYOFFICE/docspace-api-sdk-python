# RestrictedAiModelsWrapper
The successful API response containing the RestrictedAiModelsDto object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**RestrictedAiModelsDto**](RestrictedAiModelsDto.md) | The RestrictedAiModelsDto object returned by the operation. | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.restricted_ai_models_wrapper import RestrictedAiModelsWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of RestrictedAiModelsWrapper from a JSON string
restricted_ai_models_wrapper_instance = RestrictedAiModelsWrapper.from_json(json)
# print the JSON string representation of the object
print(RestrictedAiModelsWrapper.to_json())

# convert the object into a dict
restricted_ai_models_wrapper_dict = restricted_ai_models_wrapper_instance.to_dict()
# create an instance of RestrictedAiModelsWrapper from a dict
restricted_ai_models_wrapper_from_dict = RestrictedAiModelsWrapper.from_dict(restricted_ai_models_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


