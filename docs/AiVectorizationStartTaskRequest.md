# AiVectorizationStartTaskRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**files** | **List[int]** | Identifiers of the files to vectorize. | 

## Example

```python
from docspace_api_sdk.models.ai_vectorization_start_task_request import AiVectorizationStartTaskRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AiVectorizationStartTaskRequest from a JSON string
ai_vectorization_start_task_request_instance = AiVectorizationStartTaskRequest.from_json(json)
# print the JSON string representation of the object
print(AiVectorizationStartTaskRequest.to_json())

# convert the object into a dict
ai_vectorization_start_task_request_dict = ai_vectorization_start_task_request_instance.to_dict()
# create an instance of AiVectorizationStartTaskRequest from a dict
ai_vectorization_start_task_request_from_dict = AiVectorizationStartTaskRequest.from_dict(ai_vectorization_start_task_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


