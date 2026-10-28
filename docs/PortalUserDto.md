# PortalUserDto
A portal account in the format the portal stores it. Returned where the API has always handed out the  stored record; new endpoints return ASC.Web.Api.Models.EmployeeDto instead.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | The user ID. | [optional] 
**first_name** | **str** | The user's first name. | [optional] 
**last_name** | **str** | The user's last name. | [optional] 
**user_name** | **str** | The user username. | [optional] 
**birth_date** | **datetime** | The user birthday. | [optional] 
**sex** | **bool** | The user sex (male or female). | [optional] 
**status** | [**EmployeeStatus**](EmployeeStatus.md) | The user status. | [optional] 
**activation_status** | [**EmployeeActivationStatus**](EmployeeActivationStatus.md) | The user activation status. | [optional] 
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
**is_active** | **bool** | Specifies if the user is active or not. | [optional] 
**culture_name** | **str** | The user culture code. | [optional] 
**mobile_phone** | **str** | The user mobile phone. | [optional] 
**mobile_phone_activation_status** | [**MobilePhoneActivationStatus**](MobilePhoneActivationStatus.md) | The user mobile phone activation status. | [optional] 
**sid** | **str** | The LDAP user identifier. | [optional] 
**ldap_qouta** | **int** | The LDAP user quota attribute. | [optional] 
**sso_name_id** | **str** | The SSO SAML user identifier. | [optional] 
**sso_session_id** | **str** | The SSO SAML user session identifier. | [optional] 
**create_date** | **datetime** | The date and time when the user account was created. | [optional] 
**created_by** | **UUID** | The ID of the user who created the current user account. | [optional] 
**spam** | **bool** | Specifies if tips, updates and offers are allowed to be sent to the user or not. | [optional] 
**check_activation** | **bool** | Specifies whether the account still has to be activated: the opposite of `isActive`. | [optional] 

## Example

```python
from docspace_api_sdk.models.portal_user_dto import PortalUserDto

# TODO update the JSON string below
json = "{}"
# create an instance of PortalUserDto from a JSON string
portal_user_dto_instance = PortalUserDto.from_json(json)
# print the JSON string representation of the object
print(PortalUserDto.to_json())

# convert the object into a dict
portal_user_dto_dict = portal_user_dto_instance.to_dict()
# create an instance of PortalUserDto from a dict
portal_user_dto_from_dict = PortalUserDto.from_dict(portal_user_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


