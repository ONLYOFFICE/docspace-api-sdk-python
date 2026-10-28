# AiOpenaiImagesGenerations403ResponseError

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Human-readable description of the failure. | 
**type** | **str** | OpenAI error class, for example `invalid_request_error`. | 
**code** | **str** | Machine-readable code, when the provider supplies one. | [optional] 
**param** | **str** | The request parameter at fault, when the failure names one. | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_openai_images_generations403_response_error import AiOpenaiImagesGenerations403ResponseError

# TODO update the JSON string below
json = "{}"
# create an instance of AiOpenaiImagesGenerations403ResponseError from a JSON string
ai_openai_images_generations403_response_error_instance = AiOpenaiImagesGenerations403ResponseError.from_json(json)
# print the JSON string representation of the object
print(AiOpenaiImagesGenerations403ResponseError.to_json())

# convert the object into a dict
ai_openai_images_generations403_response_error_dict = ai_openai_images_generations403_response_error_instance.to_dict()
# create an instance of AiOpenaiImagesGenerations403ResponseError from a dict
ai_openai_images_generations403_response_error_from_dict = AiOpenaiImagesGenerations403ResponseError.from_dict(ai_openai_images_generations403_response_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


