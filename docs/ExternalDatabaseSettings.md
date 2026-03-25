# ExternalDatabaseSettings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**database_type** | **str** |  | [optional] 
**database_type_enum** | [**ExternalDatabaseType**](ExternalDatabaseType.md) |  | [optional] 
**db_host** | **str** |  | [optional] 
**db_port** | **int** |  | [optional] 
**db_name** | **str** |  | [optional] 
**db_user** | **str** |  | [optional] 
**db_password** | **str** |  | [optional] 
**db_ssl** | **bool** |  | [optional] 
**sqlite_file_path** | **str** |  | [optional] 

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


