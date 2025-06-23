# FileDtoIntegerSecurity

The actions that can be perforrmed with the file entry.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**read** | **bool** |  | [optional] 
**comment** | **bool** |  | [optional] 
**fill_forms** | **bool** |  | [optional] 
**review** | **bool** |  | [optional] 
**create** | **bool** |  | [optional] 
**create_from** | **bool** |  | [optional] 
**edit** | **bool** |  | [optional] 
**delete** | **bool** |  | [optional] 
**custom_filter** | **bool** |  | [optional] 
**edit_room** | **bool** |  | [optional] 
**rename** | **bool** |  | [optional] 
**read_history** | **bool** |  | [optional] 
**lock** | **bool** |  | [optional] 
**edit_history** | **bool** |  | [optional] 
**copy_to** | **bool** |  | [optional] 
**copy** | **bool** |  | [optional] 
**move_to** | **bool** |  | [optional] 
**move** | **bool** |  | [optional] 
**pin** | **bool** |  | [optional] 
**mute** | **bool** |  | [optional] 
**edit_access** | **bool** |  | [optional] 
**duplicate** | **bool** |  | [optional] 
**submit_to_form_gallery** | **bool** |  | [optional] 
**download** | **bool** |  | [optional] 
**convert** | **bool** |  | [optional] 
**copy_shared_link** | **bool** |  | [optional] 
**read_links** | **bool** |  | [optional] 
**reconnect** | **bool** |  | [optional] 
**create_room_from** | **bool** |  | [optional] 
**copy_link** | **bool** |  | [optional] 
**embed** | **bool** |  | [optional] 
**change_owner** | **bool** |  | [optional] 
**index_export** | **bool** |  | [optional] 
**start_filling** | **bool** |  | [optional] 
**filling_status** | **bool** |  | [optional] 
**reset_filling** | **bool** |  | [optional] 
**stop_filling** | **bool** |  | [optional] 
**open_form** | **bool** |  | [optional] 

## Example

```python
from docspace.models.file_dto_integer_security import FileDtoIntegerSecurity

# TODO update the JSON string below
json = "{}"
# create an instance of FileDtoIntegerSecurity from a JSON string
file_dto_integer_security_instance = FileDtoIntegerSecurity.from_json(json)
# print the JSON string representation of the object
print(FileDtoIntegerSecurity.to_json())

# convert the object into a dict
file_dto_integer_security_dict = file_dto_integer_security_instance.to_dict()
# create an instance of FileDtoIntegerSecurity from a dict
file_dto_integer_security_from_dict = FileDtoIntegerSecurity.from_dict(file_dto_integer_security_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


