# FormsItemDto
One field of a form, offered as a filter over the copies gathered in a form-filling room.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The name of the field as it is written in the form; send it back as `formsItemKey` to keep only              the completed copies whose field of that name holds a value.              <example>first_name</example> | [optional] 
**type** | **str** | The kind of value the field holds, a text box or a checkbox for instance; send it back as              `formsItemType` beside the key.              <example>text</example> | [optional] 

## Example

```python
from docspace_api_sdk.models.forms_item_dto import FormsItemDto

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


