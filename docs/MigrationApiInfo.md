# MigrationApiInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**migrator_name** | **str** |  | [optional] 
**operation** | **str** |  | [optional] 
**failed_archives** | **List[str]** |  | [optional] 
**users** | [**List[MigratingApiUser]**](MigratingApiUser.md) |  | [optional] 
**without_email_users** | [**List[MigratingApiUser]**](MigratingApiUser.md) |  | [optional] 
**exist_users** | [**List[MigratingApiUser]**](MigratingApiUser.md) |  | [optional] 
**groups** | [**List[MigratingApiGroup]**](MigratingApiGroup.md) |  | [optional] 
**import_personal_files** | **bool** |  | [optional] 
**import_shared_files** | **bool** |  | [optional] 
**import_shared_folders** | **bool** |  | [optional] 
**import_common_files** | **bool** |  | [optional] 
**import_project_files** | **bool** |  | [optional] 
**import_groups** | **bool** |  | [optional] 
**successed_users** | **int** |  | [optional] 
**failed_users** | **int** |  | [optional] 
**files** | **List[str]** |  | [optional] 
**errors** | **List[str]** |  | [optional] 

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


