# FormResultsDto

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_on** | **datetime** | The date and time when the form was created. | [optional] 
**forms_data** | [**List[FormsItemData]**](FormsItemData.md) | The list of forms data. | [optional] 

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


