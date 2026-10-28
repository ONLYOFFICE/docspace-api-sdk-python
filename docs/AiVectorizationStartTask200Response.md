# AiVectorizationStartTask200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Envelope field from the internal service; 0 for this operation. | 
**status** | **int** | Envelope status flag from the internal service. | 
**status_code** | **int** | HTTP status the internal service answered with. | 

## Example

```python
from docspace_api_sdk.models.ai_vectorization_start_task200_response import AiVectorizationStartTask200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AiVectorizationStartTask200Response from a JSON string
ai_vectorization_start_task200_response_instance = AiVectorizationStartTask200Response.from_json(json)
# print the JSON string representation of the object
print(AiVectorizationStartTask200Response.to_json())

# convert the object into a dict
ai_vectorization_start_task200_response_dict = ai_vectorization_start_task200_response_instance.to_dict()
# create an instance of AiVectorizationStartTask200Response from a dict
ai_vectorization_start_task200_response_from_dict = AiVectorizationStartTask200Response.from_dict(ai_vectorization_start_task200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


