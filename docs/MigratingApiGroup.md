# MigratingApiGroup

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**should_import** | **bool** |  | [optional] 
**group_name** | **str** |  | [optional] 
**module_name** | **str** |  | [optional] 
**user_uid_list** | **List[str]** |  | [optional] 

## Example

```python
from docspace-api-python.models.migrating_api_group import MigratingApiGroup

# TODO update the JSON string below
json = "{}"
# create an instance of MigratingApiGroup from a JSON string
migrating_api_group_instance = MigratingApiGroup.from_json(json)
# print the JSON string representation of the object
print(MigratingApiGroup.to_json())

# convert the object into a dict
migrating_api_group_dict = migrating_api_group_instance.to_dict()
# create an instance of MigratingApiGroup from a dict
migrating_api_group_from_dict = MigratingApiGroup.from_dict(migrating_api_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


