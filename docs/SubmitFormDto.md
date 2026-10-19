# SubmitFormDto
The Complete & Submit button settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**visible** | **bool** | Specifies whether the Complete  & Submit button will be displayed or hidden on the top toolbar. | [optional] 
**result_message** | **str** | A message displayed after forms are submitted. | [optional] 

## Example

```python
from docspace_api_sdk.models.submit_form_dto import SubmitFormDto

# TODO update the JSON string below
json = "{}"
# create an instance of SubmitFormDto from a JSON string
submit_form_dto_instance = SubmitFormDto.from_json(json)
# print the JSON string representation of the object
print(SubmitFormDto.to_json())

# convert the object into a dict
submit_form_dto_dict = submit_form_dto_instance.to_dict()
# create an instance of SubmitFormDto from a dict
submit_form_dto_from_dict = SubmitFormDto.from_dict(submit_form_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


