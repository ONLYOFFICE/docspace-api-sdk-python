# FormRole
The form role.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**room_id** | **int** | The room ID. | [optional] 
**role_name** | **str** | The role name. | [optional] 
**role_color** | **str** | The role color. | [optional] 
**user_id** | **str** | The user ID. | [optional] 
**sequence** | **int** | The role sequence. | [optional] 
**submitted** | **bool** | Specifies if the role was submitted or not. | [optional] 
**opened_at** | **datetime** | The date and time when the role was opened. | [optional] 
**submission_date** | **datetime** | The date and time when the role was submitted. | [optional] 

## Example

```python
from docspace-api-python.models.form_role import FormRole

# TODO update the JSON string below
json = "{}"
# create an instance of FormRole from a JSON string
form_role_instance = FormRole.from_json(json)
# print the JSON string representation of the object
print(FormRole.to_json())

# convert the object into a dict
form_role_dict = form_role_instance.to_dict()
# create an instance of FormRole from a dict
form_role_from_dict = FormRole.from_dict(form_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


