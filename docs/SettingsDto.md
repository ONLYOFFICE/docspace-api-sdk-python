# SettingsDto
The settings information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timezone** | **str** | The time zone. | [optional] 
**trusted_domains** | **List[str]** | The list of the trusted domains. | [optional] 
**trusted_domains_type** | [**TenantTrustedDomainsType**](TenantTrustedDomainsType.md) |  | [optional] 
**culture** | **str** | The language. | [optional] 
**utc_offset** | **str** | The UTC offset in the TimeSpan format. | [optional] 
**utc_hours_offset** | **float** | The UTC offset in hours. | [optional] 
**greeting_settings** | **str** | The greeting settings. | [optional] 
**owner_id** | **str** | The owner ID. | [optional] 
**name_schema_id** | **str** | The team template ID. | [optional] 
**enabled_join** | **bool** | Specifies if a user can join the portal or not. | [optional] 
**enable_adm_mess** | **bool** | Specifies if a user can send a message to the administrator when accessing the DocSpace portal or not. | [optional] 
**thirdparty_enable** | **bool** | Specifies if a user can connect third-party providers to the portal or not. | [optional] 
**doc_space** | **bool** | Specifies if this portal is a DocSpace portal or not. | [optional] 
**standalone** | **bool** | Indicates whether the system is running in standalone mode. | [optional] 
**is_ami** | **bool** | Specifies if this portal is the AMI instance or not. | [optional] 
**base_domain** | **str** | The base domain. | [optional] 
**wizard_token** | **str** | The wizard token. | [optional] 
**password_hash** | [**PasswordHasher**](PasswordHasher.md) |  | [optional] 
**firebase** | [**FirebaseDto**](FirebaseDto.md) |  | [optional] 
**version** | **str** | The portal version. | [optional] 
**recaptcha_type** | [**RecaptchaType**](RecaptchaType.md) |  | [optional] 
**recaptcha_public_key** | **str** | The ReCAPTCHA public key. | [optional] 
**debug_info** | **bool** | Specifies if the debug information will be sent or not. | [optional] 
**socket_url** | **str** | The socket URL. | [optional] 
**tenant_status** | [**TenantStatus**](TenantStatus.md) |  | [optional] 
**tenant_alias** | **str** | The tenant alias. | [optional] 
**display_about** | **bool** | Specifies whether to display the \&quot;About\&quot; portal section. | [optional] 
**domain_validator** | [**TenantDomainValidator**](TenantDomainValidator.md) |  | [optional] 
**zendesk_key** | **str** | The Zendesk key. | [optional] 
**tag_manager_id** | **str** | The tag manager ID. | [optional] 
**cookie_settings_enabled** | **bool** | Specifies whether the cookie settings are enabled. | [optional] 
**limited_access_space** | **bool** | Specifies whether the access to the space management is limited or not. | [optional] 
**limited_access_dev_tools_for_users** | **bool** | Specifies whether the access to the Developer Tools is limited for users or not. | [optional] 
**display_banners** | **bool** | Specifies whether to display the promotional banners. | [optional] 
**user_name_regex** | **str** | The user name validation regex. | [optional] 
**invitation_limit** | **int** | The maximum number of invitations to the portal. | [optional] 
**plugins** | [**PluginsDto**](PluginsDto.md) |  | [optional] 
**deep_link** | [**DeepLinkDto**](DeepLinkDto.md) |  | [optional] 
**form_gallery** | [**FormGalleryDto**](FormGalleryDto.md) |  | [optional] 
**max_image_upload_size** | **int** | The maximum image upload size. | [optional] 
**logo_text** | **str** | The white label logo text. | [optional] 
**external_resources** | [**CultureSpecificExternalResources**](CultureSpecificExternalResources.md) |  | [optional] 

## Example

```python
from docspace_api_sdk.models.settings_dto import SettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of SettingsDto from a JSON string
settings_dto_instance = SettingsDto.from_json(json)
# print the JSON string representation of the object
print(SettingsDto.to_json())

# convert the object into a dict
settings_dto_dict = settings_dto_instance.to_dict()
# create an instance of SettingsDto from a dict
settings_dto_from_dict = SettingsDto.from_dict(settings_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


