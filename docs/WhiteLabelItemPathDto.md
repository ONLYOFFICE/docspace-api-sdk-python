# WhiteLabelItemPathDto
The image URLs of one logo slot, per interface theme.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**light** | **str** | The absolute URL of the image to render on a light background. It is filled in unless the request asked  for the dark theme alone with `isDark=true`, in which case only `dark` comes back. | [optional] 
**dark** | **str** | The absolute URL of the image to render on a dark background. When both themes are asked for it comes back  empty for a slot that has no separate dark image, meaning the light one is to be used for both; when  `isDark=false` was passed it is left out entirely. | [optional] 

## Example

```python
from docspace_api_sdk.models.white_label_item_path_dto import WhiteLabelItemPathDto

# TODO update the JSON string below
json = "{}"
# create an instance of WhiteLabelItemPathDto from a JSON string
white_label_item_path_dto_instance = WhiteLabelItemPathDto.from_json(json)
# print the JSON string representation of the object
print(WhiteLabelItemPathDto.to_json())

# convert the object into a dict
white_label_item_path_dto_dict = white_label_item_path_dto_instance.to_dict()
# create an instance of WhiteLabelItemPathDto from a dict
white_label_item_path_dto_from_dict = WhiteLabelItemPathDto.from_dict(white_label_item_path_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


