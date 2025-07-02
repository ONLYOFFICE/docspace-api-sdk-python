# WatermarkRequestDto
The request parameters for adding watermarks.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Specifies whether watermarks are on or off. | [optional] 
**additions** | [**WatermarkAdditions**](WatermarkAdditions.md) |  | [optional] 
**text** | **str** | The watermark text. | [optional] 
**rotate** | **int** | The watermark text and image rotate angle. | [optional] 
**image_scale** | **int** | The watermark image scale. | [optional] 
**image_url** | **str** | The path to the temporary image file. | [optional] 
**image_height** | **float** | The watermark image height. | [optional] 
**image_width** | **float** | The watermark image width. | [optional] 

## Example

```python
from docspace-api-python.models.watermark_request_dto import WatermarkRequestDto

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


