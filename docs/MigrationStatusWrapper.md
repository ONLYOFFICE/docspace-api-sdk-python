# MigrationStatusWrapper


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**MigrationStatusDto**](MigrationStatusDto.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace.models.migration_status_wrapper import MigrationStatusWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of MigrationStatusWrapper from a JSON string
migration_status_wrapper_instance = MigrationStatusWrapper.from_json(json)
# print the JSON string representation of the object
print(MigrationStatusWrapper.to_json())

# convert the object into a dict
migration_status_wrapper_dict = migration_status_wrapper_instance.to_dict()
# create an instance of MigrationStatusWrapper from a dict
migration_status_wrapper_from_dict = MigrationStatusWrapper.from_dict(migration_status_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


