# WhiteLabelItemSizeDto
The pixel box a logo slot is drawn in, in the shape the imaging library reports a geometry.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aspect_ratio** | **bool** | Whether the numbers are to be read as an aspect ratio rather than as pixels. Always `false` on the sizes  this API reports. | [optional] 
**fill_area** | **bool** | Whether an image would be scaled to cover the box rather than to fit inside it. Always `false` here. | [optional] 
**greater** | **bool** | Whether scaling would apply only to an image larger than the box. Always `false` here. | [optional] 
**height** | **int** | The height of the box in pixels - one of the two fields of this object that carry information. | [optional] 
**ignore_aspect_ratio** | **bool** | Whether scaling would be allowed to distort the image. Always `false` here. | [optional] 
**is_percentage** | **bool** | Whether `width` and `height` are to be read as percentages. Always `false` here, so both are pixels. | [optional] 
**less** | **bool** | Whether scaling would apply only to an image smaller than the box. Always `false` here. | [optional] 
**limit_pixels** | **bool** | Whether the box is to be read as a total pixel-area budget instead of as two dimensions. Always `false`  here. | [optional] 
**width** | **int** | The width of the box in pixels - the other field of this object that carries information. | [optional] 
**x** | **int** | The horizontal offset of the box from the origin. Always `0` here. | [optional] 
**y** | **int** | The vertical offset of the box from the origin. Always `0` here. | [optional] 

## Example

```python
from docspace_api_sdk.models.white_label_item_size_dto import WhiteLabelItemSizeDto

# TODO update the JSON string below
json = "{}"
# create an instance of WhiteLabelItemSizeDto from a JSON string
white_label_item_size_dto_instance = WhiteLabelItemSizeDto.from_json(json)
# print the JSON string representation of the object
print(WhiteLabelItemSizeDto.to_json())

# convert the object into a dict
white_label_item_size_dto_dict = white_label_item_size_dto_instance.to_dict()
# create an instance of WhiteLabelItemSizeDto from a dict
white_label_item_size_dto_from_dict = WhiteLabelItemSizeDto.from_dict(white_label_item_size_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


