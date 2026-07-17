# DefaultTemplateItemDto
Default template setting

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selected_file** | **int** | File id to use as a default template | [optional] 
**file_extension** | **str** | Extension of a default template | 
**file_title** | **str** | Title of a default template | [optional] 
**last_modified** | **datetime** | Last modified date of a default template | [optional] 
**file_size** | **int** | Filesize (in bytes) of a default template | [optional] 
**view_url** | **str** | View url of a default template | [optional] 

## Example

```python
from docspace_api_sdk.models.default_template_item_dto import DefaultTemplateItemDto

# TODO update the JSON string below
json = "{}"
# create an instance of DefaultTemplateItemDto from a JSON string
default_template_item_dto_instance = DefaultTemplateItemDto.from_json(json)
# print the JSON string representation of the object
print(DefaultTemplateItemDto.to_json())

# convert the object into a dict
default_template_item_dto_dict = default_template_item_dto_instance.to_dict()
# create an instance of DefaultTemplateItemDto from a dict
default_template_item_dto_from_dict = DefaultTemplateItemDto.from_dict(default_template_item_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


