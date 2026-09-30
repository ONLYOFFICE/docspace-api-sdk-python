# AiWatermarkDto
The watermark drawn over the documents of a room while they are viewed and printed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additions** | [**AiWatermarkAdditions**](AiWatermarkAdditions.md) | Which details of the reader and of the room are stamped alongside the text. The values combine, so a number  that is not a member on its own is the sum of several of them, and 0 means that only the text is stamped. | 
**text** | **str** | The fixed line drawn over the document, printed before the details selected alongside it. Empty when the room  stamps an image instead. | [optional] 
**rotate** | **int** | How far the stamp is turned, in degrees, with negative values turning it anticlockwise and 0 drawing it  horizontally. | 
**image_scale** | **int** | How large the image is drawn, as a percentage of its own size. It is 0 for a text watermark, where nothing is  scaled. | 
**image_url** | **str** | The address the stamped picture is served from, inside the storage of the room. Empty for a text watermark. | [optional] 
**image_height** | **float** | The height the picture is drawn with, in pixels, kept together with the width so that the proportions survive.  It is 0 for a text watermark. | 
**image_width** | **float** | The width the picture is drawn with, in pixels, kept together with the height so that the proportions survive.  It is 0 for a text watermark. | 

## Example

```python
from docspace_api_sdk.models.ai_watermark_dto import AiWatermarkDto

# TODO update the JSON string below
json = "{}"
# create an instance of AiWatermarkDto from a JSON string
ai_watermark_dto_instance = AiWatermarkDto.from_json(json)
# print the JSON string representation of the object
print(AiWatermarkDto.to_json())

# convert the object into a dict
ai_watermark_dto_dict = ai_watermark_dto_instance.to_dict()
# create an instance of AiWatermarkDto from a dict
ai_watermark_dto_from_dict = AiWatermarkDto.from_dict(ai_watermark_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


