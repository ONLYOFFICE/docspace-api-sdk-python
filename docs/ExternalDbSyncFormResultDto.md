# ExternalDbSyncFormResultDto
The result of an external DB synchronization for a single form.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The form file ID. | [optional] 
**title** | **str** | The form file title. | [optional] 
**success** | **bool** | Specifies whether the synchronization succeeded for this form. | [optional] 
**error** | **str** | The error message if the synchronization failed for this form. | [optional] 

## Example

```python
from docspace_api_sdk.models.external_db_sync_form_result_dto import ExternalDbSyncFormResultDto

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalDbSyncFormResultDto from a JSON string
external_db_sync_form_result_dto_instance = ExternalDbSyncFormResultDto.from_json(json)
# print the JSON string representation of the object
print(ExternalDbSyncFormResultDto.to_json())

# convert the object into a dict
external_db_sync_form_result_dto_dict = external_db_sync_form_result_dto_instance.to_dict()
# create an instance of ExternalDbSyncFormResultDto from a dict
external_db_sync_form_result_dto_from_dict = ExternalDbSyncFormResultDto.from_dict(external_db_sync_form_result_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


