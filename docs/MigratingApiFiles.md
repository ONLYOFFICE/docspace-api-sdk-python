# MigratingApiFiles

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**folders_count** | **int** |  | [optional] 
**files_count** | **int** |  | [optional] 
**bytes_total** | **int** |  | [optional] 

## Example

```python
from docspace-api-python.models.migrating_api_files import MigratingApiFiles

# TODO update the JSON string below
json = "{}"
# create an instance of MigratingApiFiles from a JSON string
migrating_api_files_instance = MigratingApiFiles.from_json(json)
# print the JSON string representation of the object
print(MigratingApiFiles.to_json())

# convert the object into a dict
migrating_api_files_dict = migrating_api_files_instance.to_dict()
# create an instance of MigratingApiFiles from a dict
migrating_api_files_from_dict = MigratingApiFiles.from_dict(migrating_api_files_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


