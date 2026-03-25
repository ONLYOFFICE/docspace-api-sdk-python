# VectorizationStartRequestBody
Parameters for submitting files for vectorization.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**files** | **List[int]** | The set of file identifiers to submit for vectorization. | 

## Example

```python
from docspace_api_sdk.models.vectorization_start_request_body import VectorizationStartRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of VectorizationStartRequestBody from a JSON string
vectorization_start_request_body_instance = VectorizationStartRequestBody.from_json(json)
# print the JSON string representation of the object
print(VectorizationStartRequestBody.to_json())

# convert the object into a dict
vectorization_start_request_body_dict = vectorization_start_request_body_instance.to_dict()
# create an instance of VectorizationStartRequestBody from a dict
vectorization_start_request_body_from_dict = VectorizationStartRequestBody.from_dict(vectorization_start_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


