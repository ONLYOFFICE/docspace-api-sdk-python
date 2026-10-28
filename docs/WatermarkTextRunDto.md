# WatermarkTextRunDto
A run of watermark text with its own colour and size.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fill** | **List[int]** | The fill color of the text run in RGB format. | [optional] 
**text** | **str** | The run text. | [optional] 
**font_size** | **str** | The font size of the text run in points. | [optional] 

## Example

```python
from docspace_api_sdk.models.watermark_text_run_dto import WatermarkTextRunDto

# TODO update the JSON string below
json = "{}"
# create an instance of WatermarkTextRunDto from a JSON string
watermark_text_run_dto_instance = WatermarkTextRunDto.from_json(json)
# print the JSON string representation of the object
print(WatermarkTextRunDto.to_json())

# convert the object into a dict
watermark_text_run_dto_dict = watermark_text_run_dto_instance.to_dict()
# create an instance of WatermarkTextRunDto from a dict
watermark_text_run_dto_from_dict = WatermarkTextRunDto.from_dict(watermark_text_run_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


