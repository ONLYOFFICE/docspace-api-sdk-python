# MigrationApiInfo
The migration API information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**migrator_name** | **str** | The migrator name. | [optional] 
**operation** | **str** | The migration operation. | [optional] 
**failed_archives** | **List[str]** | The list of failed archives. | [optional] 
**users** | [**List[MigratingApiUser]**](MigratingApiUser.md) | The list of migrating users. | [optional] 
**without_email_users** | [**List[MigratingApiUser]**](MigratingApiUser.md) | The list of migrating users without email. | [optional] 
**exist_users** | [**List[MigratingApiUser]**](MigratingApiUser.md) | The list of existing migrating users. | [optional] 
**groups** | [**List[MigratingApiGroup]**](MigratingApiGroup.md) | The list of migrating groups. | [optional] 
**import_personal_files** | **bool** | Specifies whether to import personal files or not. | [optional] 
**import_shared_files** | **bool** | Specifies whether to import shared files or not. | [optional] 
**import_shared_folders** | **bool** | Specifies whether to import shared folders or not. | [optional] 
**import_common_files** | **bool** | Specifies whether to import common files or not. | [optional] 
**import_project_files** | **bool** | Specifies whether to import project files or not. | [optional] 
**import_groups** | **bool** | Specifies whether to import groups or not. | [optional] 
**successed_users** | **int** | The number of successfully migrated users. | [optional] 
**failed_users** | **int** | The number of unsuccessfully migrated users. | [optional] 
**files** | **List[str]** | The list of migrated files. | [optional] 
**errors** | **List[str]** | The list of migration errors. | [optional] 

## Example

```python
from docspace_api_sdk.models.migration_api_info import MigrationApiInfo

# TODO update the JSON string below
json = "{}"
# create an instance of MigrationApiInfo from a JSON string
migration_api_info_instance = MigrationApiInfo.from_json(json)
# print the JSON string representation of the object
print(MigrationApiInfo.to_json())

# convert the object into a dict
migration_api_info_dict = migration_api_info_instance.to_dict()
# create an instance of MigrationApiInfo from a dict
migration_api_info_from_dict = MigrationApiInfo.from_dict(migration_api_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


