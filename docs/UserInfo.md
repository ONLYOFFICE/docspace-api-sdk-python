# UserInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID | [optional] 
**first_name** | **str** | First name | [optional] 
**last_name** | **str** | Last name | [optional] 
**user_name** | **str** | Username | [optional] 
**birth_date** | **datetime** | Birthday | [optional] 
**sex** | **bool** | Sex (male or female) | [optional] 
**status** | [**EmployeeStatus**](EmployeeStatus.md) |  | [optional] 
**activation_status** | [**EmployeeActivationStatus**](EmployeeActivationStatus.md) |  | [optional] 
**terminated_date** | **datetime** | The date and time when the user account was terminated | [optional] 
**title** | **str** | Title | [optional] 
**work_from_date** | **datetime** | Registration date | [optional] 
**email** | **str** | Email | [optional] 
**contacts** | **str** | List of contacts in the string format | [optional] 
**contacts_list** | **List[str]** | List of contacts | [optional] 
**location** | **str** | Location | [optional] 
**notes** | **str** | Notes | [optional] 
**removed** | **bool** | Specifies if the user account was removed or not | [optional] 
**last_modified** | **datetime** | Last modified date | [optional] 
**tenant_id** | **int** | Tenant ID | [optional] 
**is_active** | **bool** | Spceifies if the user is active or not | [optional] [readonly] 
**culture_name** | **str** | Language | [optional] 
**mobile_phone** | **str** | Mobile phone | [optional] 
**mobile_phone_activation_status** | [**MobilePhoneActivationStatus**](MobilePhoneActivationStatus.md) |  | [optional] 
**sid** | **str** | LDAP user identificator | [optional] 
**ldap_qouta** | **int** | LDAP user quota attribute | [optional] 
**sso_name_id** | **str** | SSO SAML user identificator | [optional] 
**sso_session_id** | **str** | SSO SAML user session identificator | [optional] 
**create_date** | **datetime** | Creation date | [optional] 
**created_by** | **str** |  | [optional] 
**spam** | **bool** |  | [optional] 
**check_activation** | **bool** |  | [optional] [readonly] 

## Example

```python
from docspace.models.user_info import UserInfo

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


