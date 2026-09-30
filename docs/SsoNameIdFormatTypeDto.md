# SsoNameIdFormatTypeDto
The SAML name ID formats the SSO settings accept.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**saml11_unspecified** | **str** | The SAML 1.1 unspecified name ID format. | [optional] [readonly] 
**saml11_email_address** | **str** | The SAML 1.1 email address name ID format. | [optional] [readonly] 
**saml20_entity** | **str** | The SAML 2.0 entity name ID format. | [optional] [readonly] 
**saml20_transient** | **str** | The SAML 2.0 transient name ID format, whose identifier differs from one session to the next. It is what  the built-in configuration uses. | [optional] [readonly] 
**saml20_persistent** | **str** | The SAML 2.0 persistent name ID format, whose identifier stays the same for one person across sessions. | [optional] [readonly] 
**saml20_encrypted** | **str** | The SAML 2.0 encrypted name ID format. | [optional] [readonly] 
**saml20_unspecified** | **str** | The SAML 2.0 unspecified name ID format. | [optional] [readonly] 
**saml11_x509_subject_name** | **str** | The SAML 1.1 X.509 subject name name ID format. | [optional] [readonly] 
**saml11_windows_domain_qualified_name** | **str** | The SAML 1.1 Windows domain qualified name name ID format. | [optional] [readonly] 
**saml20_kerberos** | **str** | The SAML 2.0 Kerberos name ID format. | [optional] [readonly] 

## Example

```python
from docspace_api_sdk.models.sso_name_id_format_type_dto import SsoNameIdFormatTypeDto

# TODO update the JSON string below
json = "{}"
# create an instance of SsoNameIdFormatTypeDto from a JSON string
sso_name_id_format_type_dto_instance = SsoNameIdFormatTypeDto.from_json(json)
# print the JSON string representation of the object
print(SsoNameIdFormatTypeDto.to_json())

# convert the object into a dict
sso_name_id_format_type_dto_dict = sso_name_id_format_type_dto_instance.to_dict()
# create an instance of SsoNameIdFormatTypeDto from a dict
sso_name_id_format_type_dto_from_dict = SsoNameIdFormatTypeDto.from_dict(sso_name_id_format_type_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


