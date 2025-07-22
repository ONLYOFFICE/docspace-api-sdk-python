# EmployeeFullDto
The full list of user parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The user ID. | [optional] 
**display_name** | **str** | The user display name. | [optional] 
**title** | **str** | The user title. | [optional] 
**avatar** | **str** | The user avatar. | [optional] 
**avatar_original** | **str** | The user original size avatar. | [optional] 
**avatar_max** | **str** | The user maximum size avatar. | [optional] 
**avatar_medium** | **str** | The user medium size avatar. | [optional] 
**avatar_small** | **str** | The user small size avatar. | [optional] 
**profile_url** | **str** | The user profile URL. | [optional] 
**has_avatar** | **bool** | Specifies if the user has an avatar or not. | [optional] 
**is_anonim** | **bool** | Specifies if the user is anonymous or not. | [optional] 
**first_name** | **str** | The user first name. | [optional] 
**last_name** | **str** | The user last name. | [optional] 
**user_name** | **str** | The user username. | [optional] 
**email** | **str** | The user email. | [optional] 
**contacts** | [**List[Contact]**](Contact.md) | The list of user contacts. | [optional] 
**birthday** | [**ApiDateTime**](ApiDateTime.md) |  | [optional] 
**sex** | **str** | The user sex. | [optional] 
**status** | [**EmployeeStatus**](EmployeeStatus.md) |  | [optional] 
**activation_status** | [**EmployeeActivationStatus**](EmployeeActivationStatus.md) |  | [optional] 
**terminated** | [**ApiDateTime**](ApiDateTime.md) |  | [optional] 
**department** | **str** | The user department. | [optional] 
**work_from** | [**ApiDateTime**](ApiDateTime.md) |  | [optional] 
**groups** | [**List[GroupSummaryDto]**](GroupSummaryDto.md) | The list of user groups. | [optional] 
**location** | **str** | The user location. | [optional] 
**notes** | **str** | The user notes. | [optional] 
**is_admin** | **bool** | Specifies if the user is an administrator or not. | [optional] 
**is_room_admin** | **bool** | Specifies if the user is a room administrator or not. | [optional] 
**is_ldap** | **bool** | Specifies if the LDAP settings are enabled for the user or not. | [optional] 
**list_admin_modules** | **List[str]** | The list of the administrator modules. | [optional] 
**is_owner** | **bool** | Specifies if the user is a portal owner or not. | [optional] 
**is_visitor** | **bool** | Specifies if the user is a portal visitor or not. | [optional] 
**is_collaborator** | **bool** | Specifies if the user is a portal collaborator or not. | [optional] 
**culture_name** | **str** | The user culture code. | [optional] 
**mobile_phone** | **str** | The user mobile phone number. | [optional] 
**mobile_phone_activation_status** | [**MobilePhoneActivationStatus**](MobilePhoneActivationStatus.md) |  | [optional] 
**is_sso** | **bool** | Specifies if the SSO settings are enabled for the user or not. | [optional] 
**theme** | [**DarkThemeSettingsType**](DarkThemeSettingsType.md) |  | [optional] 
**quota_limit** | **int** | The user quota limit. | [optional] 
**used_space** | **float** | The portal used space of the user. | [optional] 
**shared** | **bool** | Specifies if the user has access rights. | [optional] 
**is_custom_quota** | **bool** | Specifies if the user has a custom quota or not. | [optional] 
**login_event_id** | **int** | The current login event ID. | [optional] 
**created_by** | [**EmployeeDto**](EmployeeDto.md) |  | [optional] 
**registration_date** | [**ApiDateTime**](ApiDateTime.md) |  | [optional] 
**has_personal_folder** | **bool** | Specifies if the user has a personal folder or not. | [optional] 
**tfa_app_enabled** | **bool** | Indicates whether the user has enabled two-factor authentication (TFA) using an authentication app. | [optional] 

## Example

```python
from docspace-api-sdk.models.employee_full_dto import EmployeeFullDto

# TODO update the JSON string below
json = "{}"
# create an instance of EmployeeFullDto from a JSON string
employee_full_dto_instance = EmployeeFullDto.from_json(json)
# print the JSON string representation of the object
print(EmployeeFullDto.to_json())

# convert the object into a dict
employee_full_dto_dict = employee_full_dto_instance.to_dict()
# create an instance of EmployeeFullDto from a dict
employee_full_dto_from_dict = EmployeeFullDto.from_dict(employee_full_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


