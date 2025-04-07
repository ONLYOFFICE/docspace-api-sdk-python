# EmployeeFullDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID | [optional] 
**display_name** | **str** | Display name | [optional] 
**title** | **str** | Title | [optional] 
**avatar** | **str** | Avatar | [optional] 
**avatar_original** | **str** | Original size avatar | [optional] 
**avatar_max** | **str** | Maximum size avatar | [optional] 
**avatar_medium** | **str** | Medium size avatar | [optional] 
**avatar_small** | **str** | Small avatar | [optional] 
**profile_url** | **str** | Profile URL | [optional] 
**has_avatar** | **bool** | Specifies if the user has an avatar or not | [optional] 
**is_anonim** | **bool** | Specifies if the user is an anonim or not | [optional] 
**first_name** | **str** | First name | [optional] 
**last_name** | **str** | Last name | [optional] 
**user_name** | **str** | Username | [optional] 
**email** | **str** | Email | [optional] 
**contacts** | [**List[Contact]**](Contact.md) | List of contacts | [optional] 
**birthday** | [**ApiDateTime**](ApiDateTime.md) |  | [optional] 
**sex** | **str** | Sex | [optional] 
**status** | [**EmployeeStatus**](EmployeeStatus.md) |  | [optional] 
**activation_status** | [**EmployeeActivationStatus**](EmployeeActivationStatus.md) |  | [optional] 
**terminated** | [**ApiDateTime**](ApiDateTime.md) |  | [optional] 
**department** | **str** | Department | [optional] 
**work_from** | [**ApiDateTime**](ApiDateTime.md) |  | [optional] 
**groups** | [**List[GroupSummaryDto]**](GroupSummaryDto.md) | List of groups | [optional] 
**location** | **str** | Location | [optional] 
**notes** | **str** | Notes | [optional] 
**is_admin** | **bool** | Specifies if the user is an administrator or not | [optional] 
**is_room_admin** | **bool** | Specifies if the user is a room administrator or not | [optional] 
**is_ldap** | **bool** | Specifies if the LDAP settings are enabled for the user or not | [optional] 
**list_admin_modules** | **List[str]** | List of administrator modules | [optional] 
**is_owner** | **bool** | Specifies if the user is a portal owner or not | [optional] 
**is_visitor** | **bool** | Specifies if the user is a portal visitor or not | [optional] 
**is_collaborator** | **bool** | Specifies if the user is a portal collaborator or not | [optional] 
**culture_name** | **str** | Language | [optional] 
**mobile_phone** | **str** | Mobile phone number | [optional] 
**mobile_phone_activation_status** | [**MobilePhoneActivationStatus**](MobilePhoneActivationStatus.md) |  | [optional] 
**is_sso** | **bool** | Specifies if the SSO settings are enabled for the user or not | [optional] 
**theme** | [**DarkThemeSettingsType**](DarkThemeSettingsType.md) |  | [optional] 
**quota_limit** | **int** | Quota limit | [optional] 
**used_space** | **float** | Portal used space | [optional] 
**shared** | **bool** | Shared | [optional] 
**is_custom_quota** | **bool** | Specifies if the user has a custom quota or not | [optional] 
**login_event_id** | **int** | Current login event ID | [optional] 
**created_by** | [**EmployeeDto**](EmployeeDto.md) |  | [optional] 
**registration_date** | [**ApiDateTime**](ApiDateTime.md) |  | [optional] 

## Example

```python
from docspace.models.employee_full_dto import EmployeeFullDto

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


