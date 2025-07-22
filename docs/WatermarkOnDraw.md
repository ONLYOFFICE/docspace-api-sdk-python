# WatermarkOnDraw
The document watermark parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**width** | **float** | Defines the watermark width measured in millimeters. | [optional] 
**height** | **float** | Defines the watermark height measured in millimeters. | [optional] 
**margins** | **List[int]** | Defines the watermark margins measured in millimeters. | [optional] 
**fill** | **str** | Defines the watermark fill color. | [optional] 
**rotate** | **int** | Defines the watermark rotation angle. | [optional] 
**transparent** | **float** | Defines the watermark transparency percentage. | [optional] 
**paragraphs** | [**List[Paragraph]**](Paragraph.md) | The list of paragraphs of the watermark. | [optional] 

## Example

```python
from docspace-api-sdk.models.watermark_on_draw import WatermarkOnDraw

# TODO update the JSON string below
json = "{}"
# create an instance of WatermarkOnDraw from a JSON string
watermark_on_draw_instance = WatermarkOnDraw.from_json(json)
# print the JSON string representation of the object
print(WatermarkOnDraw.to_json())

# convert the object into a dict
watermark_on_draw_dict = watermark_on_draw_instance.to_dict()
# create an instance of WatermarkOnDraw from a dict
watermark_on_draw_from_dict = WatermarkOnDraw.from_dict(watermark_on_draw_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


