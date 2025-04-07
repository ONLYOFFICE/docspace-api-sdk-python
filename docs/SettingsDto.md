# SettingsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timezone** | **str** | Time zone | [optional] 
**trusted_domains** | **List[str]** | List of trusted domains | [optional] 
**trusted_domains_type** | [**TenantTrustedDomainsType**](TenantTrustedDomainsType.md) |  | [optional] 
**culture** | **str** | Language | [optional] 
**utc_offset** | **str** | UTC offset | [optional] 
**utc_hours_offset** | **float** | UTC hours offset | [optional] 
**greeting_settings** | **str** | Greeting settings | [optional] 
**owner_id** | **str** | Owner ID | [optional] 
**name_schema_id** | **str** | Team template ID | [optional] 
**enabled_join** | **bool** | Specifies if a user can join to the portal or not | [optional] 
**enable_adm_mess** | **bool** | Specifies if a user can send a message to the administrator or not | [optional] 
**thirdparty_enable** | **bool** | Specifies if a user can connect third-party providers or not | [optional] 
**doc_space** | **bool** | Specifies if this is a DocSpace portal or not | [optional] 
**standalone** | **bool** | Specifies if this is a standalone portal or not | [optional] 
**is_ami** | **bool** | Specifies if this is a AMI instance or not | [optional] 
**base_domain** | **str** | Base domain | [optional] 
**wizard_token** | **str** | Wizard token | [optional] 
**password_hash** | [**PasswordHasher**](PasswordHasher.md) |  | [optional] 
**firebase** | [**FirebaseDto**](FirebaseDto.md) |  | [optional] 
**version** | **str** | Version | [optional] 
**recaptcha_type** | [**RecaptchaType**](RecaptchaType.md) |  | [optional] 
**recaptcha_public_key** | **str** | ReCAPTCHA public key | [optional] 
**debug_info** | **bool** | Specifies if the debug information will be sent or not | [optional] 
**socket_url** | **str** | Socket URL | [optional] 
**tenant_status** | [**TenantStatus**](TenantStatus.md) |  | [optional] 
**tenant_alias** | **str** | Tenant alias | [optional] 
**display_about** | **bool** | Specifies whether to display the About section | [optional] 
**domain_validator** | [**TenantDomainValidator**](TenantDomainValidator.md) |  | [optional] 
**zendesk_key** | **str** | Zendesk key | [optional] 
**tag_manager_id** | **str** | Tag manager ID | [optional] 
**cookie_settings_enabled** | **bool** | Specifies whether the cookie settings are enabled | [optional] 
**limited_access_space** | **bool** | Limited access space | [optional] 
**user_name_regex** | **str** | User name validation regex | [optional] 
**invitation_limit** | **int** | Invitation limit | [optional] 
**plugins** | [**PluginsDto**](PluginsDto.md) |  | [optional] 
**deep_link** | [**DeepLinkDto**](DeepLinkDto.md) |  | [optional] 
**form_gallery** | [**FormGalleryDto**](FormGalleryDto.md) |  | [optional] 
**max_image_upload_size** | **int** | Max image upload size | [optional] 
**logo_text** | **str** | White label logo text | [optional] 
**external_resources** | [**CultureSpecificExternalResources**](CultureSpecificExternalResources.md) |  | [optional] 

## Example

```python
from docspace.models.settings_dto import SettingsDto

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


