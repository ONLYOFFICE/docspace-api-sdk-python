# FormsItemDto
The forms item information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from docspace-api-python.models.forms_item_dto import FormsItemDto

# TODO update the JSON string below
json = "{}"
# create an instance of FormsItemDto from a JSON string
forms_item_dto_instance = FormsItemDto.from_json(json)
# print the JSON string representation of the object
print(FormsItemDto.to_json())

# convert the object into a dict
forms_item_dto_dict = forms_item_dto_instance.to_dict()
# create an instance of FormsItemDto from a dict
forms_item_dto_from_dict = FormsItemDto.from_dict(forms_item_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


