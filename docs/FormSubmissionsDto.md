# FormSubmissionsDto
All completed copies of a form, together with the description of the fields they were filled into.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**List[FormMetadata]**](FormMetadata.md) | Describes the fields of the form version that is being filled - the key each value is stored under, the type  and format of the field and, where the field offers a fixed set of answers, those answers - in the order the  fields are laid out, which is the order to build a results table in. It comes back empty when the portal holds  no indexed description of that version. | [optional] 
**submissions** | [**List[FormResultsDto]**](FormResultsDto.md) | One entry per completed copy, ordered by the copy number that `formsData` carries. An empty list means nothing  has been completed for the version that is currently being filled; the copies of earlier versions of the form  are not reported here. | [optional] 

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


