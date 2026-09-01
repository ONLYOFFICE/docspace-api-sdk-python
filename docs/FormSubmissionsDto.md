# FormSubmissionsDto
All submissions of a form, together with the metadata of its fields.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**List[FormMetadata]**](FormMetadata.md) | The form field metadata. | [optional] 
**submissions** | [**List[FormResultsDto]**](FormResultsDto.md) | All submissions. | [optional] 

## Example

```python
from docspace_api_sdk.models.form_submissions_dto import FormSubmissionsDto

# TODO update the JSON string below
json = "{}"
# create an instance of FormSubmissionsDto from a JSON string
form_submissions_dto_instance = FormSubmissionsDto.from_json(json)
# print the JSON string representation of the object
print(FormSubmissionsDto.to_json())

# convert the object into a dict
form_submissions_dto_dict = form_submissions_dto_instance.to_dict()
# create an instance of FormSubmissionsDto from a dict
form_submissions_dto_from_dict = FormSubmissionsDto.from_dict(form_submissions_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


