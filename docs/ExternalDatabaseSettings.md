# ExternalDatabaseSettings
The connection parameters of an external database.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**database_type** | **str** | The engine of the external database. | [optional] 
**database_type_enum** | [**ExternalDatabaseType**](ExternalDatabaseType.md) | The engine of an external database. | [optional] 
**db_host** | **str** | The host name or the IP address of the database server. | [optional] 
**db_port** | **int** | The port the database server listens on. | [optional] 
**db_name** | **str** | The name of the database to connect to. | [optional] 
**db_user** | **str** | The user name to connect with. | [optional] 
**db_password** | **str** | The password to connect with. | [optional] 
**db_ssl** | **bool** | Specifies whether the connection to the database is secured with SSL. | [optional] 
**sqlite_file_path** | **str** | The path to the database file, used by the SQLite engine only. | [optional] 

## Example

```python
from docspace_api_sdk.models.external_database_settings import ExternalDatabaseSettings

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalDatabaseSettings from a JSON string
external_database_settings_instance = ExternalDatabaseSettings.from_json(json)
# print the JSON string representation of the object
print(ExternalDatabaseSettings.to_json())

# convert the object into a dict
external_database_settings_dict = external_database_settings_instance.to_dict()
# create an instance of ExternalDatabaseSettings from a dict
external_database_settings_from_dict = ExternalDatabaseSettings.from_dict(external_database_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


