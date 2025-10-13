# BackupServiceStateDto
Backup service state.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Specifies if the backup service is enabled or not. | [optional] 

## Example

```python
from docspace_api_sdk.models.backup_service_state_dto import BackupServiceStateDto

# TODO update the JSON string below
json = "{}"
# create an instance of BackupServiceStateDto from a JSON string
backup_service_state_dto_instance = BackupServiceStateDto.from_json(json)
# print the JSON string representation of the object
print(BackupServiceStateDto.to_json())

# convert the object into a dict
backup_service_state_dto_dict = backup_service_state_dto_instance.to_dict()
# create an instance of BackupServiceStateDto from a dict
backup_service_state_dto_from_dict = BackupServiceStateDto.from_dict(backup_service_state_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


