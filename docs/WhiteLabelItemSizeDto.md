# WhiteLabelItemSizeDto
The white label logo size parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aspect_ratio** | **bool** | Specifies whether the size is an aspect ratio. | [optional] 
**fill_area** | **bool** | Specifies whether the logo is resized based on the smallest fitting dimension. | [optional] 
**greater** | **bool** | Specifies whether the logo is resized only if it is greater than the size. | [optional] 
**height** | **int** | The logo height, in pixels. | [optional] 
**ignore_aspect_ratio** | **bool** | Specifies whether the logo is resized without preserving the aspect ratio. | [optional] 
**is_percentage** | **bool** | Specifies whether the width and height are expressed as percentages. | [optional] 
**less** | **bool** | Specifies whether the logo is resized only if it is less than the size. | [optional] 
**limit_pixels** | **bool** | Specifies whether the logo is resized using a pixel area count limit. | [optional] 
**width** | **int** | The logo width, in pixels. | [optional] 
**x** | **int** | The X offset from the origin, in pixels. | [optional] 
**y** | **int** | The Y offset from the origin, in pixels. | [optional] 

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


