# SsoSettingsV2
The SSO portal settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_modified** | **datetime** |  | [optional] 
**enable_sso** | **bool** | Specifies if the SSO settings are enabled or not. | [optional] 
**idp_settings** | [**SsoIdpSettings**](SsoIdpSettings.md) |  | [optional] 
**idp_certificates** | [**List[SsoCertificate]**](SsoCertificate.md) | The list of the IdP certificates. | [optional] 
**idp_certificate_advanced** | [**SsoIdpCertificateAdvanced**](SsoIdpCertificateAdvanced.md) |  | [optional] 
**sp_login_label** | **str** | The SP login label. | [optional] 
**sp_certificates** | [**List[SsoCertificate]**](SsoCertificate.md) | The list of the SP certificates. | [optional] 
**sp_certificate_advanced** | [**SsoSpCertificateAdvanced**](SsoSpCertificateAdvanced.md) |  | [optional] 
**field_mapping** | [**SsoFieldMapping**](SsoFieldMapping.md) |  | [optional] 
**hide_auth_page** | **bool** | Specifies if the authentication page will be hidden or not. | [optional] 
**users_type** | **int** | The user type. | [optional] 
**disable_email_verification** | **bool** | Specifies if the email verification is disabled or not. | [optional] 

## Example

```python
from docspace_api_sdk.models.sso_settings_v2 import SsoSettingsV2

# TODO update the JSON string below
json = "{}"
# create an instance of SsoSettingsV2 from a JSON string
sso_settings_v2_instance = SsoSettingsV2.from_json(json)
# print the JSON string representation of the object
print(SsoSettingsV2.to_json())

# convert the object into a dict
sso_settings_v2_dict = sso_settings_v2_instance.to_dict()
# create an instance of SsoSettingsV2 from a dict
sso_settings_v2_from_dict = SsoSettingsV2.from_dict(sso_settings_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


