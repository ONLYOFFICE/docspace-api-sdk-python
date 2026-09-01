# BackupsCountResultDto
The number of backups.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**free** | **int** | The number of free backups. | [optional] 
**paid** | **int** | The number of paid backups. | [optional] 

## Example

```python
from docspace_api_sdk.models.backups_count_result_dto import BackupsCountResultDto

# TODO update the JSON string below
json = "{}"
# create an instance of BackupsCountResultDto from a JSON string
backups_count_result_dto_instance = BackupsCountResultDto.from_json(json)
# print the JSON string representation of the object
print(BackupsCountResultDto.to_json())

# convert the object into a dict
backups_count_result_dto_dict = backups_count_result_dto_instance.to_dict()
# create an instance of BackupsCountResultDto from a dict
backups_count_result_dto_from_dict = BackupsCountResultDto.from_dict(backups_count_result_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


