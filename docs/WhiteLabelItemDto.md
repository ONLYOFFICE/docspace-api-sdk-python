# WhiteLabelItemDto
The white label item parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**WhiteLabelLogoType**](WhiteLabelLogoType.md) | The white label logo type. | [optional] 
**name** | **str** | The white label file name. | [optional] 
**size** | [**WhiteLabelItemSizeDto**](WhiteLabelItemSizeDto.md) | The white label file size. | [optional] 
**path** | [**WhiteLabelItemPathDto**](WhiteLabelItemPathDto.md) | The white label file path. | [optional] 

## Example

```python
from docspace_api_sdk.models.white_label_item_dto import WhiteLabelItemDto

# TODO update the JSON string below
json = "{}"
# create an instance of WhiteLabelItemDto from a JSON string
white_label_item_dto_instance = WhiteLabelItemDto.from_json(json)
# print the JSON string representation of the object
print(WhiteLabelItemDto.to_json())

# convert the object into a dict
white_label_item_dto_dict = white_label_item_dto_instance.to_dict()
# create an instance of WhiteLabelItemDto from a dict
white_label_item_dto_from_dict = WhiteLabelItemDto.from_dict(white_label_item_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


