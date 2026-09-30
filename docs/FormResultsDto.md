# FormResultsDto
One completed copy of a form, with the values that were entered into it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_on** | **datetime** | When the portal recorded this copy, in UTC: the moment the filled copy was completed and its data indexed, not  the moment the form itself was made. | [optional] 
**forms_data** | [**List[FormsItemData]**](FormsItemData.md) | The values that were entered into this copy, one entry per field, preceded by an entry keyed `FormNumber` that  carries the number of the copy and is what the submissions are ordered by. Fields holding a picture or a  signature are left out of the record, so a field missing here was not necessarily left blank. | [optional] 

## Example

```python
from docspace_api_sdk.models.form_results_dto import FormResultsDto

# TODO update the JSON string below
json = "{}"
# create an instance of FormResultsDto from a JSON string
form_results_dto_instance = FormResultsDto.from_json(json)
# print the JSON string representation of the object
print(FormResultsDto.to_json())

# convert the object into a dict
form_results_dto_dict = form_results_dto_instance.to_dict()
# create an instance of FormResultsDto from a dict
form_results_dto_from_dict = FormResultsDto.from_dict(form_results_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


