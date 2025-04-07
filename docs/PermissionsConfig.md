# PermissionsConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**change_history** | **bool** | Change history | [optional] 
**comment** | **bool** | Comment | [optional] 
**chat** | **bool** | Chat | [optional] 
**download** | **bool** | Download | [optional] 
**edit** | **bool** | Edit | [optional] 
**fill_forms** | **bool** | FillForms | [optional] 
**modify_filter** | **bool** | ModifyFilter | [optional] 
**protect** | **bool** | Protect | [optional] 
**var_print** | **bool** | Print | [optional] 
**rename** | **bool** | Rename | [optional] 
**review** | **bool** | Review | [optional] 
**copy** | **bool** | Copy | [optional] 

## Example

```python
from docspace.models.permissions_config import PermissionsConfig

# TODO update the JSON string below
json = "{}"
# create an instance of PermissionsConfig from a JSON string
permissions_config_instance = PermissionsConfig.from_json(json)
# print the JSON string representation of the object
print(PermissionsConfig.to_json())

# convert the object into a dict
permissions_config_dict = permissions_config_instance.to_dict()
# create an instance of PermissionsConfig from a dict
permissions_config_from_dict = PermissionsConfig.from_dict(permissions_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


