# FileDtoAllOfViewAccessibility
Which ways of opening this format the portal supports at all - its own editor, the picture viewer, the media  player and so on. It answers whether the format can be shown, not whether this account may do it; rights are  reported in `security`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image_view** | **bool** |  | [optional] 
**media_view** | **bool** |  | [optional] 
**web_view** | **bool** |  | [optional] 
**web_edit** | **bool** |  | [optional] 
**web_review** | **bool** |  | [optional] 
**web_custom_filter_editing** | **bool** |  | [optional] 
**web_restricted_editing** | **bool** |  | [optional] 
**web_comment** | **bool** |  | [optional] 
**can_convert** | **bool** |  | [optional] 
**must_convert** | **bool** |  | [optional] 

## Example

```python
from docspace_api_sdk.models.file_dto_all_of_view_accessibility import FileDtoAllOfViewAccessibility

# TODO update the JSON string below
json = "{}"
# create an instance of FileDtoAllOfViewAccessibility from a JSON string
file_dto_all_of_view_accessibility_instance = FileDtoAllOfViewAccessibility.from_json(json)
# print the JSON string representation of the object
print(FileDtoAllOfViewAccessibility.to_json())

# convert the object into a dict
file_dto_all_of_view_accessibility_dict = file_dto_all_of_view_accessibility_instance.to_dict()
# create an instance of FileDtoAllOfViewAccessibility from a dict
file_dto_all_of_view_accessibility_from_dict = FileDtoAllOfViewAccessibility.from_dict(file_dto_all_of_view_accessibility_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


