# WatermarkParagraphDto
One paragraph of the watermark text.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**align** | **int** | The paragraph align. | [optional] 
**runs** | [**List[WatermarkTextRunDto]**](WatermarkTextRunDto.md) | The list of text runs from the paragraph. | [optional] 

## Example

```python
from docspace_api_sdk.models.watermark_paragraph_dto import WatermarkParagraphDto

# TODO update the JSON string below
json = "{}"
# create an instance of WatermarkParagraphDto from a JSON string
watermark_paragraph_dto_instance = WatermarkParagraphDto.from_json(json)
# print the JSON string representation of the object
print(WatermarkParagraphDto.to_json())

# convert the object into a dict
watermark_paragraph_dto_dict = watermark_paragraph_dto_instance.to_dict()
# create an instance of WatermarkParagraphDto from a dict
watermark_paragraph_dto_from_dict = WatermarkParagraphDto.from_dict(watermark_paragraph_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


