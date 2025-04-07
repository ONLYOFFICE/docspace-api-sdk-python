# HideConfirmConvertRequestDto

Request parameters for hiding the confirmation dialog

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**save** | **bool** | Specifies whether to set the specified settings or not | [optional] 

## Example

```python
from docspace.models.hide_confirm_convert_request_dto import HideConfirmConvertRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of HideConfirmConvertRequestDto from a JSON string
hide_confirm_convert_request_dto_instance = HideConfirmConvertRequestDto.from_json(json)
# print the JSON string representation of the object
print(HideConfirmConvertRequestDto.to_json())

# convert the object into a dict
hide_confirm_convert_request_dto_dict = hide_confirm_convert_request_dto_instance.to_dict()
# create an instance of HideConfirmConvertRequestDto from a dict
hide_confirm_convert_request_dto_from_dict = HideConfirmConvertRequestDto.from_dict(hide_confirm_convert_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


