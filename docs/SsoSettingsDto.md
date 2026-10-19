# SsoSettingsDto
The SAML single sign-on configuration of the portal.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_modified** | **datetime** | The timestamp indicating when the settings were last modified. | [optional] 
**enable_sso** | **bool** | Specifies if the SSO settings are enabled or not. | [optional] 
**idp_settings** | [**SsoIdpSettingsDto**](SsoIdpSettingsDto.md) | The SSO IdP settings. | [optional] 
**idp_certificates** | [**List[SsoCertificateDto]**](SsoCertificateDto.md) | The list of the IdP certificates. | [optional] 
**idp_certificate_advanced** | [**SsoIdpCertificateAdvancedDto**](SsoIdpCertificateAdvancedDto.md) | The IdP advanced certificate. | [optional] 
**sp_login_label** | **str** | The SP login label. | [optional] 
**sp_certificates** | [**List[SsoCertificateDto]**](SsoCertificateDto.md) | The list of the SP certificates. | [optional] 
**sp_certificate_advanced** | [**SsoSpCertificateAdvancedDto**](SsoSpCertificateAdvancedDto.md) | The SP advanced certificate. | [optional] 
**field_mapping** | [**SsoFieldMappingDto**](SsoFieldMappingDto.md) | The SSO field mapping. | [optional] 
**hide_auth_page** | **bool** | Specifies if the authentication page will be hidden or not. | [optional] 
**users_type** | **int** | The user type. | [optional] 
**disable_email_verification** | **bool** | Specifies if the email verification is disabled or not. | [optional] 

## Example

```python
from docspace_api_sdk.models.sso_settings_dto import SsoSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of SsoSettingsDto from a JSON string
sso_settings_dto_instance = SsoSettingsDto.from_json(json)
# print the JSON string representation of the object
print(SsoSettingsDto.to_json())

# convert the object into a dict
sso_settings_dto_dict = sso_settings_dto_instance.to_dict()
# create an instance of SsoSettingsDto from a dict
sso_settings_dto_from_dict = SsoSettingsDto.from_dict(sso_settings_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


