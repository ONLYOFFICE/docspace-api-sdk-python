# BackupServiceStateDto
Whether the paid backup service is switched on for a portal.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Specifies whether the paid backup service is switched on for this portal, which is a setting of its  wallet rather than the health of the backup service. While it is true, backups beyond the free  monthly allowance are charged to the wallet. | [optional] 

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


