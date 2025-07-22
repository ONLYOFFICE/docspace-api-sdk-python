# MigratingApiUser

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**should_import** | **bool** |  | [optional] 
**key** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**user_type** | [**EmployeeType**](EmployeeType.md) |  | [optional] 
**migrating_files** | [**MigratingApiFiles**](MigratingApiFiles.md) |  | [optional] 

## Example

```python
from docspace-api-sdk.models.migrating_api_user import MigratingApiUser

# TODO update the JSON string below
json = "{}"
# create an instance of MigratingApiUser from a JSON string
migrating_api_user_instance = MigratingApiUser.from_json(json)
# print the JSON string representation of the object
print(MigratingApiUser.to_json())

# convert the object into a dict
migrating_api_user_dict = migrating_api_user_instance.to_dict()
# create an instance of MigratingApiUser from a dict
migrating_api_user_from_dict = MigratingApiUser.from_dict(migrating_api_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


