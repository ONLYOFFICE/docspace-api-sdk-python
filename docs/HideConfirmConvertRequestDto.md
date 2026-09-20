# HideConfirmConvertRequestDto
The body of the conversion prompt switch: which of the two prompts to hide.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**save** | **bool** | Chooses the prompt to hide rather than the state to store: true hides the prompt that offers to keep a copy in  the original format when a document is converted, false hides the prompt that offers to open the conversion  result. Each of the two flags is stored separately for the calling account, and both are one-way - the portal  can hide a prompt but has no way to show it again. | [optional] 

## Example

```python
from docspace_api_sdk.models.hide_confirm_convert_request_dto import HideConfirmConvertRequestDto

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


