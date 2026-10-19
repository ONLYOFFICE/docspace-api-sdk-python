# FormRoleRequest
One role of a form and the account that fills it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**room_id** | **int** | The ID of the room the form is in. It is stored with the role as sent, so pass the room the form lives in. | [optional] 
**role_name** | **str** | The name of a role the form defines, such as the one the form author gave a group of fields. | [optional] 
**role_color** | **str** | The color the editor marks the fields of this role with, as a hex code. | [optional] 
**user_id** | **UUID** | The account that fills this role. It is notified once filling starts, unless it is the caller. | [optional] 
**sequence** | **int** | Accepted for compatibility and ignored: the position of the role in the list sets the filling order. | [optional] 
**submitted** | **bool** | Whether this role counts as already submitted. It is stored as sent; send false when filling starts. | [optional] 
**opened_at** | **datetime** | Accepted for compatibility and ignored: the portal records when the role is opened. | [optional] 
**submission_date** | **datetime** | Accepted for compatibility and ignored: the portal records when the role is submitted. | [optional] 

## Example

```python
from docspace_api_sdk.models.form_role_request import FormRoleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FormRoleRequest from a JSON string
form_role_request_instance = FormRoleRequest.from_json(json)
# print the JSON string representation of the object
print(FormRoleRequest.to_json())

# convert the object into a dict
form_role_request_dict = form_role_request_instance.to_dict()
# create an instance of FormRoleRequest from a dict
form_role_request_from_dict = FormRoleRequest.from_dict(form_role_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


