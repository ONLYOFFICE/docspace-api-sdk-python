# WatermarkDto



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additions** | [**WatermarkAdditions**](WatermarkAdditions.md) |  | [optional] 
**text** | **str** | Watermark Text | [optional] 
**rotate** | **int** | Watermark text and image rotate | [optional] 
**image_scale** | **int** | Watermark image scale | [optional] 
**image_url** | **str** | Watermark image url | [optional] 
**image_height** | **float** | Watermark image height | [optional] 
**image_width** | **float** | Watermark image width | [optional] 

## Example

```python
from docspace.models.watermark_dto import WatermarkDto

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


