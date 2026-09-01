# AiSuccessResponse
Generic success acknowledgement for mutations that return no data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Always true — the mutation completed. | 

## Example

```python
from docspace_api_sdk.models.ai_success_response import AiSuccessResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AiSuccessResponse from a JSON string
ai_success_response_instance = AiSuccessResponse.from_json(json)
# print the JSON string representation of the object
print(AiSuccessResponse.to_json())

# convert the object into a dict
ai_success_response_dict = ai_success_response_instance.to_dict()
# create an instance of AiSuccessResponse from a dict
ai_success_response_from_dict = AiSuccessResponse.from_dict(ai_success_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


