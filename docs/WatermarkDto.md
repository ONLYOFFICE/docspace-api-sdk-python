# WatermarkDto
The watermark settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additions** | [**WatermarkAdditions**](WatermarkAdditions.md) |  | [optional] 
**text** | **str** | The watermark text. | [optional] 
**rotate** | **int** | The watermark text and image rotate. | [optional] 
**image_scale** | **int** | The watermark image scale. | [optional] 
**image_url** | **str** | The watermark image url. | [optional] 
**image_height** | **float** | The watermark image height. | [optional] 
**image_width** | **float** | The watermark image width. | [optional] 

## Example

```python
from docspace-api-sdk.models.watermark_dto import WatermarkDto

# TODO update the JSON string below
json = "{}"
# create an instance of WatermarkDto from a JSON string
watermark_dto_instance = WatermarkDto.from_json(json)
# print the JSON string representation of the object
print(WatermarkDto.to_json())

# convert the object into a dict
watermark_dto_dict = watermark_dto_instance.to_dict()
# create an instance of WatermarkDto from a dict
watermark_dto_from_dict = WatermarkDto.from_dict(watermark_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


