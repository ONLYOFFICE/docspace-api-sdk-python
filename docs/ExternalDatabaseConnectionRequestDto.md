# ExternalDatabaseConnectionRequestDto
The connection parameters of an external database to test.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**database_type** | **str** | The engine of the external database: `mysql`, or `sqlite` on a Standalone installation. | [optional] 
**database_type_enum** | [**ExternalDatabaseType**](ExternalDatabaseType.md) | The engine named by `databaseType`, as the server reads it. A value sent here is ignored. | [optional] 
**db_host** | **str** | The host name or the IP address of the database server. | [optional] 
**db_port** | **int** | The port the database server listens on. | [optional] 
**db_name** | **str** | The name of the database to connect to. | [optional] 
**db_user** | **str** | The user name to connect with. | [optional] 
**db_password** | **str** | The password to connect with. | [optional] 
**db_ssl** | **bool** | Whether the connection is secured with SSL. | [optional] 
**sqlite_file_path** | **str** | The path to the database file, used by the SQLite engine only. | [optional] 

## Example

```python
from docspace_api_sdk.models.external_database_connection_request_dto import ExternalDatabaseConnectionRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalDatabaseConnectionRequestDto from a JSON string
external_database_connection_request_dto_instance = ExternalDatabaseConnectionRequestDto.from_json(json)
# print the JSON string representation of the object
print(ExternalDatabaseConnectionRequestDto.to_json())

# convert the object into a dict
external_database_connection_request_dto_dict = external_database_connection_request_dto_instance.to_dict()
# create an instance of ExternalDatabaseConnectionRequestDto from a dict
external_database_connection_request_dto_from_dict = ExternalDatabaseConnectionRequestDto.from_dict(external_database_connection_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


