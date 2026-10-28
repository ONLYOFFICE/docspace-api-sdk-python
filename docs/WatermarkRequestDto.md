# WatermarkRequestDto
The watermark drawn over the documents of a room.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Whether the room draws a watermark at all. Sending the object with this turned off removes the watermark the  room has, and the rest of the fields are then irrelevant. | [optional] 
**additions** | [**WatermarkAdditions**](WatermarkAdditions.md) | Which details of the reader and of the room are stamped into the watermark alongside the text. The values  combine, so several of them can be added together to stamp more than one. | [optional] 
**text** | **str** | The fixed line drawn over the document, shown before the details selected alongside it. It is the whole  watermark when no details are added. | [optional] 
**rotate** | **int** | How far the watermark is turned, in degrees, with negative values turning it anticlockwise. Zero draws it  horizontally across the page. | [optional] 
**image_scale** | **int** | How large the watermark image is drawn, as a percentage of its own size. It applies to the image form of the  watermark only. | [optional] 
**image_url** | **str** | The picture to use instead of a text watermark, named by the path that `POST api/2.0/files/logos` returned for  an image uploaded beforehand. The portal copies it into the room when the setting is saved. | [optional] 
**image_height** | **float** | The height the watermark image is drawn with, in pixels, used together with the width to keep its proportions. | [optional] 
**image_width** | **float** | The width the watermark image is drawn with, in pixels, used together with the height to keep its proportions. | [optional] 

## Example

```python
from docspace_api_sdk.models.watermark_request_dto import WatermarkRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of WatermarkRequestDto from a JSON string
watermark_request_dto_instance = WatermarkRequestDto.from_json(json)
# print the JSON string representation of the object
print(WatermarkRequestDto.to_json())

# convert the object into a dict
watermark_request_dto_dict = watermark_request_dto_instance.to_dict()
# create an instance of WatermarkRequestDto from a dict
watermark_request_dto_from_dict = WatermarkRequestDto.from_dict(watermark_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


