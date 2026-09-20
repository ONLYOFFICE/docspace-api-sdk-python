# DefaultTemplateItemDto
The blank document configured for one extension.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selected_file** | **int** | The copy stored in the portal that serves as the blank for this extension. A null means no custom blank has  been chosen and new documents start from the portal's built-in one; the other fields of the entry are then  empty as well. | [optional] 
**file_extension** | **str** | The extension the entry describes, in lower case with the leading dot. It is the value to send back when this  blank is replaced or reset. | 
**file_title** | **str** | The name the custom blank was copied under, useful for showing which document was chosen. Empty while the  built-in blank is in use. | [optional] 
**last_modified** | **datetime** | When the custom blank was last changed, in the time zone of the portal. Null while the built-in blank is in  use. | [optional] 
**file_size** | **int** | The size of the custom blank in bytes. Null while the built-in blank is in use. | [optional] 
**view_url** | **str** | The address the custom blank can be downloaded from, already carrying the access key of the calling account.  Empty while the built-in blank is in use. | [optional] 

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


