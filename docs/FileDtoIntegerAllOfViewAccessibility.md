# FileDtoIntegerAllOfViewAccessibility
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
from docspace_api_sdk.models.file_dto_integer_all_of_view_accessibility import FileDtoIntegerAllOfViewAccessibility

# TODO update the JSON string below
json = "{}"
# create an instance of FileDtoIntegerAllOfViewAccessibility from a JSON string
file_dto_integer_all_of_view_accessibility_instance = FileDtoIntegerAllOfViewAccessibility.from_json(json)
# print the JSON string representation of the object
print(FileDtoIntegerAllOfViewAccessibility.to_json())

# convert the object into a dict
file_dto_integer_all_of_view_accessibility_dict = file_dto_integer_all_of_view_accessibility_instance.to_dict()
# create an instance of FileDtoIntegerAllOfViewAccessibility from a dict
file_dto_integer_all_of_view_accessibility_from_dict = FileDtoIntegerAllOfViewAccessibility.from_dict(file_dto_integer_all_of_view_accessibility_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


