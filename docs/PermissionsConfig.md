# PermissionsConfig
The permissions configuration parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **bool** | Defines if the document can be commented or not. | [optional] 
**chat** | **bool** | Defines if the chat functionality is enabled in the document or not. | [optional] 
**download** | **bool** | Defines if the document can be downloaded or only viewed or edited online. | [optional] 
**edit** | **bool** | Defines if the document can be edited or only viewed. | [optional] 
**fill_forms** | **bool** | Defines if the forms can be filled. | [optional] 
**modify_filter** | **bool** | Defines if the filter can be applied globally (true) affecting all the other users,  or locally (false), i.e. for the current user only. | [optional] 
**protect** | **bool** | Defines if the \&quot;Protection\&quot; tab on the toolbar and the \&quot;Protect\&quot; button in the left menu are displayedor hidden. | [optional] 
**var_print** | **bool** | Defines if the document can be printed or not. | [optional] 
**rename** | **bool** | Specifies whether to display the \&quot;Rename...\&quot; button when using the \&quot;onRequestRename\&quot; event. | [optional] 
**review** | **bool** | Defines if the document can be reviewed or not. | [optional] 
**copy** | **bool** | Defines if the content can be copied to the clipboard or not. | [optional] 

## Example

```python
from docspace-api-python.models.permissions_config import PermissionsConfig

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


