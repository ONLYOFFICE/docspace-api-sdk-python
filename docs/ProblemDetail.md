# ProblemDetail
RFC 7807 problem details returned by the registration API for failed requests.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | A URI reference that identifies the problem type. This service sets it to the DocSpace API getting-started page. | [optional] 
**title** | **str** | A short, human-readable summary of the problem type, typically the HTTP status reason phrase. | [optional] 
**status** | **int** | The HTTP status code for this occurrence of the problem. | [optional] 
**detail** | **str** | A human-readable explanation specific to this occurrence of the problem. | [optional] 
**instance** | **str** | A URI reference that identifies the specific occurrence, set to the request path. | [optional] 
**properties** | **Dict[str, Optional[object]]** | Extension members carried on the problem. Usually empty; validation failures also surface as the top-level errors array. | [optional] 
**errors** | [**List[FieldError]**](FieldError.md) | Field-specific validation errors. Present when the request body or parameters failed validation, or when a named scope is not in the tenant catalogue. | [optional] 

## Example

```python
from docspace_api_sdk.models.problem_detail import ProblemDetail

# TODO update the JSON string below
json = "{}"
# create an instance of ProblemDetail from a JSON string
problem_detail_instance = ProblemDetail.from_json(json)
# print the JSON string representation of the object
print(ProblemDetail.to_json())

# convert the object into a dict
problem_detail_dict = problem_detail_instance.to_dict()
# create an instance of ProblemDetail from a dict
problem_detail_from_dict = ProblemDetail.from_dict(problem_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


