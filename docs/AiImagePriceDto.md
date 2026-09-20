# AiImagePriceDto
What an image model charges: the tokens of the request and the images that come out of it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prompt** | **float** | The cost of one million tokens sent to the image model, which is the prompt describing the picture. | [optional] 
**completion** | **float** | The cost of one million tokens the image model writes back alongside the picture. | [optional] 
**image** | **float** | The cost of one produced image, charged on top of the token amounts above. | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_image_price_dto import AiImagePriceDto

# TODO update the JSON string below
json = "{}"
# create an instance of AiImagePriceDto from a JSON string
ai_image_price_dto_instance = AiImagePriceDto.from_json(json)
# print the JSON string representation of the object
print(AiImagePriceDto.to_json())

# convert the object into a dict
ai_image_price_dto_dict = ai_image_price_dto_instance.to_dict()
# create an instance of AiImagePriceDto from a dict
ai_image_price_dto_from_dict = AiImagePriceDto.from_dict(ai_image_price_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


