# AiImagePrice

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prompt** | **float** |  | [optional] 
**completion** | **float** |  | [optional] 
**image** | **float** |  | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_image_price import AiImagePrice

# TODO update the JSON string below
json = "{}"
# create an instance of AiImagePrice from a JSON string
ai_image_price_instance = AiImagePrice.from_json(json)
# print the JSON string representation of the object
print(AiImagePrice.to_json())

# convert the object into a dict
ai_image_price_dict = ai_image_price_instance.to_dict()
# create an instance of AiImagePrice from a dict
ai_image_price_from_dict = AiImagePrice.from_dict(ai_image_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


