# FormsItemDataDto
The data of the separate form item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The form data key. | [optional] 
**tag** | **str** | The form data tag. | [optional] 
**value** | **str** | The form data value. | [optional] 
**type** | **str** | The form data type. | [optional] 

## Example

```python
from docspace_api_sdk.models.forms_item_data_dto import FormsItemDataDto

# TODO update the JSON string below
json = "{}"
# create an instance of FormsItemDataDto from a JSON string
forms_item_data_dto_instance = FormsItemDataDto.from_json(json)
# print the JSON string representation of the object
print(FormsItemDataDto.to_json())

# convert the object into a dict
forms_item_data_dto_dict = forms_item_data_dto_instance.to_dict()
# create an instance of FormsItemDataDto from a dict
forms_item_data_dto_from_dict = FormsItemDataDto.from_dict(forms_item_data_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


