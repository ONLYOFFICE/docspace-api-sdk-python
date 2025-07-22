# FileDtoIntegerViewAccessibility
The file accessibility.

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
**co_auhtoring** | **bool** |  | [optional] 
**can_convert** | **bool** |  | [optional] 
**must_convert** | **bool** |  | [optional] 

## Example

```python
from docspace-api-sdk.models.file_dto_integer_view_accessibility import FileDtoIntegerViewAccessibility

# TODO update the JSON string below
json = "{}"
# create an instance of FileDtoIntegerViewAccessibility from a JSON string
file_dto_integer_view_accessibility_instance = FileDtoIntegerViewAccessibility.from_json(json)
# print the JSON string representation of the object
print(FileDtoIntegerViewAccessibility.to_json())

# convert the object into a dict
file_dto_integer_view_accessibility_dict = file_dto_integer_view_accessibility_instance.to_dict()
# create an instance of FileDtoIntegerViewAccessibility from a dict
file_dto_integer_view_accessibility_from_dict = FileDtoIntegerViewAccessibility.from_dict(file_dto_integer_view_accessibility_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


