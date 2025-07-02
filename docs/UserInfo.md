# UserInfo
The user information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The user ID. | [optional] 
**first_name** | **str** | The user first name. | [optional] 
**last_name** | **str** | The user last name. | [optional] 
**user_name** | **str** | The user username. | [optional] 
**birth_date** | **datetime** | The user birthday. | [optional] 
**sex** | **bool** | The user sex (male or female). | [optional] 
**status** | [**EmployeeStatus**](EmployeeStatus.md) |  | [optional] 
**activation_status** | [**EmployeeActivationStatus**](EmployeeActivationStatus.md) |  | [optional] 
**terminated_date** | **datetime** | The date and time when the user account was terminated. | [optional] 
**title** | **str** | The user title. | [optional] 
**work_from_date** | **datetime** | The user registration date. | [optional] 
**email** | **str** | The user email address. | [optional] 
**contacts** | **str** | The list of user contacts in the string format. | [optional] 
**contacts_list** | **List[str]** | The list of user contacts. | [optional] 
**location** | **str** | The user location. | [optional] 
**notes** | **str** | The user notes. | [optional] 
**removed** | **bool** | Specifies if the user account was removed or not. | [optional] 
**last_modified** | **datetime** | The date and time when the user account was last modified. | [optional] 
**tenant_id** | **int** | The tenant ID. | [optional] 
**is_active** | **bool** | Specifies if the user is active or not. | [optional] [readonly] 
**culture_name** | **str** | The user culture code. | [optional] 
**mobile_phone** | **str** | The user mobile phone. | [optional] 
**mobile_phone_activation_status** | [**MobilePhoneActivationStatus**](MobilePhoneActivationStatus.md) |  | [optional] 
**sid** | **str** | The LDAP user identificator. | [optional] 
**ldap_qouta** | **int** | The LDAP user quota attribute. | [optional] 
**sso_name_id** | **str** | The SSO SAML user identificator. | [optional] 
**sso_session_id** | **str** | The SSO SAML user session identificator. | [optional] 
**create_date** | **datetime** | The date and time when the user account was created. | [optional] 
**created_by** | **str** | The ID of the user who created the current user account. | [optional] 
**spam** | **bool** | Specifies if tips, updates and offers are allowed to be sent to the user or not. | [optional] 
**check_activation** | **bool** |  | [optional] [readonly] 

## Example

```python
from docspace-api-python.models.user_info import UserInfo

# TODO update the JSON string below
json = "{}"
# create an instance of UserInfo from a JSON string
user_info_instance = UserInfo.from_json(json)
# print the JSON string representation of the object
print(UserInfo.to_json())

# convert the object into a dict
user_info_dict = user_info_instance.to_dict()
# create an instance of UserInfo from a dict
user_info_from_dict = UserInfo.from_dict(user_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


