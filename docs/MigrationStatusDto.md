# MigrationStatusDto
The migration status parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**progress** | **float** | The migration progress. | [optional] 
**error** | **str** | The migration error. | [optional] 
**parse_result** | [**MigrationApiInfo**](MigrationApiInfo.md) |  | [optional] 
**is_completed** | **bool** | Specifies whether the migration is completed or not. | [optional] 

## Example

```python
from docspace-api-sdk.models.migration_status_dto import MigrationStatusDto

# TODO update the JSON string below
json = "{}"
# create an instance of MigrationStatusDto from a JSON string
migration_status_dto_instance = MigrationStatusDto.from_json(json)
# print the JSON string representation of the object
print(MigrationStatusDto.to_json())

# convert the object into a dict
migration_status_dto_dict = migration_status_dto_instance.to_dict()
# create an instance of MigrationStatusDto from a dict
migration_status_dto_from_dict = MigrationStatusDto.from_dict(migration_status_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


