# SettingsDto
The general configuration of the current portal, as the client shell needs it before and after sign-in.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timezone** | **str** | The portal time zone as an IANA identifier, which is the zone every date this API returns in portal time  is expressed in. Filled in for a signed-in caller only. | [optional] 
**trusted_domains** | **List[str]** | The mail domains a new member may register or be invited from without confirming the address. It is filled  in for a signed-in caller, and for an anonymous one only while `enabledJoin` is `true`; it is empty  whenever `trustedDomainsType` is not `Custom`. | [optional] 
**trusted_domains_type** | [**TenantTrustedDomainsType**](TenantTrustedDomainsType.md) | How the mail domains above are applied: no domain trusted, every domain trusted, or only the listed ones.  Filled in under the same conditions as `trustedDomains`. | [optional] 
**culture** | **str** | The default language of the portal as a culture name, which is what unauthenticated pages are rendered in.  A signed-in member may have a language of their own, and that one is not reported here. | 
**utc_offset** | **str** | The portal's offset from UTC as a time span, positive east of UTC. Filled in for a signed-in caller only,  and taken at the moment of the call, so it already reflects daylight saving time. | [optional] 
**utc_hours_offset** | **float** | The same offset in hours, fractional for a zone that is not on a whole hour. It is there so a client does  not have to parse `utcOffset`. | [optional] 
**greeting_settings** | **str** | The portal title shown on the login page and in letters. It falls back to the product name in the portal  language while the portal has been given no title of its own. | [optional] 
**owner_id** | **UUID** | The portal owner, the one account that cannot be removed or demoted. Filled in for a signed-in caller  only, and the empty GUID for an anonymous one. | [optional] 
**name_schema_id** | **str** | The naming scheme the portal uses for its own vocabulary - what a member, a group or a room is called in  the interface. `GET api/2.0/settings/customschemas/{id}` spells that vocabulary out. Filled in for a  signed-in caller only. | [optional] 
**enabled_join** | **bool** | Whether someone who is not invited may still register, which is the case when the portal trusts every mail  domain or a list of them. It is computed for an anonymous caller only and left out entirely for a  signed-in one, so a missing value is not a `false`. | [optional] 
**enable_adm_mess** | **bool** | Whether the login page may offer the form for writing to the portal administrators. It is also `true`  while the portal's payment has lapsed, whatever the setting says, so it can be set on a portal where an  administrator switched the form off. | [optional] 
**thirdparty_enable** | **bool** | Whether the login page may offer sign-in through an external identity provider. It is computed for an  anonymous caller only; `GET api/2.0/capabilities` reports the same thing with the list of providers. | [optional] 
**doc_space** | **bool** | Always `true` in this product. It exists so a client that also talks to older ONLYOFFICE portals can tell  them apart, and is not a feature switch. | [optional] 
**standalone** | **bool** | Whether this is a server installation someone administers themselves rather than a portal in the cloud.  Several fields below and a number of operations behave differently in the two, so a client that has to  branch on the deployment reads it here. | [optional] 
**is_ami** | **bool** | Whether the installation runs from an Amazon machine image, which is a server installation that can read  its own instance metadata. It is `false` on every cloud portal. | [optional] 
**base_domain** | **str** | The domain new portals of this installation are created under, which is what a portal name is checked  against and appended to. It is empty on an installation that serves a single portal on a fixed address. | 
**wizard_token** | **str** | The token that authorizes the first-run setup wizard. It is handed out to anonymous callers only, and only  while the wizard has not been completed; once it has, the field stays empty for good. | [optional] 
**password_hash** | [**PasswordHasher**](PasswordHasher.md) | The parameters for hashing a password in the client before it is sent - the salt, the iteration count and  the hash size. It is filled in for an anonymous caller and, for a signed-in one, only when  `withPassword=true` is asked for. Hash with exactly these parameters and send the result as  `passwordHash`, since the portal cannot reproduce the hash from a different set. | [optional] 
**firebase** | [**FirebaseDto**](FirebaseDto.md) | The Firebase project a mobile or web client sends push registrations to. Filled in for a signed-in caller  only, and its own fields are empty strings on an installation that configures no Firebase project. | [optional] 
**version** | **str** | The product version of the portal, empty when the installation does not publish one. It is the version of  the server, not of this API, whose own version is fixed at 2.0. | [optional] 
**recaptcha_type** | [**RecaptchaType**](RecaptchaType.md) | Which CAPTCHA the login form has to render, decided by the installation's configuration. Computed for an  anonymous caller only. | [optional] 
**recaptcha_public_key** | **str** | The site key for the CAPTCHA named by `recaptchaType`, safe to embed in a page. It is empty when the  installation configures no CAPTCHA, in which case the login form asks for none. | [optional] 
**debug_info** | **bool** | Whether the client may collect and send diagnostic information. Filled in for a signed-in caller only, and  `false` unless the installation switched it on. | [optional] 
**socket_url** | **str** | The address of the socket service that pushes live updates to a client. It is filled in for a signed-in  caller and for an anonymous one who arrives with an external sharing link, and is empty when the  installation runs no socket service - a client then has to poll. | [optional] 
**tenant_status** | [**TenantStatus**](TenantStatus.md) | The lifecycle state of the portal. Anything other than active means most operations are refused for the  moment, because the portal is being transferred, restored, encrypted or removed. | [optional] 
**tenant_alias** | **str** | The portal's own name within the installation, which together with `baseDomain` forms the address it is  reached at. `PUT api/2.0/portal/portalrename` changes it. | [optional] 
**display_about** | **bool** | Whether the interface may show the About page. A cloud portal always may; a server installation may unless  its plan includes branding and the vendor details hide the page. | [optional] 
**domain_validator** | [**TenantDomainValidator**](TenantDomainValidator.md) | The rules a portal name is checked against - its length limits and the pattern it has to match - so a  client can validate a rename before sending it. Filled in for a signed-in caller only. | [optional] 
**zendesk_key** | **str** | The key that lets the client open the vendor's support chat, empty when the installation configures none.  Filled in for a signed-in caller only. | [optional] 
**tag_manager_id** | **str** | The Google Tag Manager container the client should load, empty when the installation configures none.  Filled in for a signed-in caller only. | [optional] 
**cookie_settings_enabled** | **bool** | Whether the portal limits how long an authentication session stays valid. The limit itself is read with  `GET api/2.0/settings/cookiesettings`; while this is `false` a session is honoured for a year. | 
**limited_access_space** | **bool** | Whether the space-management section is restricted to the portal owner. Filled in for a signed-in caller  only. | [optional] 
**limited_access_dev_tools_for_users** | **bool** | Whether the Developer Tools section is hidden from members who are not administrators. Filled in for a  signed-in caller only. | [optional] 
**display_banners** | **bool** | Whether the interface may show the vendor's promotional banners. A cloud portal always reports `true`; on  a server installation it follows the banner setting. Filled in for a signed-in caller only. | [optional] 
**ai_enabled** | **bool** | Whether the AI features - chat, agents and vectorisation - may be used on this portal. While it is  `false` the AI Agents folder is hidden and the AI operations are refused. Filled in for a signed-in caller  only. | [optional] 
**wallet_low_balance** | **bool** | Whether the portal wallet has already dropped below its low-balance threshold, so a client can warn about  AI operations being cut off. It is reported to DocSpace administrators only and left empty for everyone  else, which is not the same as a healthy balance. | [optional] 
**user_name_regex** | **str** | The pattern a member's first and last name has to match, so a client can validate a name before sending  it. It is a .NET regular expression and is applied to each name part separately. | [optional] 
**invitation_limit** | **int** | How many invitations the portal may still send in the current window. Filled in for a signed-in caller  only, and set to the maximum value of a 32-bit integer on an installation that limits nothing. | [optional] 
**plugins** | [**PluginsDto**](PluginsDto.md) | What the installation allows to be done with web plugins. Filled in for a signed-in caller only, with all  three flags `false` unless the installation switched plugins on. | [optional] 
**deep_link** | [**DeepLinkDto**](DeepLinkDto.md) | What a mobile client needs to hand a document link over to the installed application instead of opening it  in the browser. Its fields are empty strings when the installation configures no application. | 
**form_gallery** | [**FormGalleryDto**](FormGalleryDto.md) | Where the ready-made form templates are served from and which extension they carry. Filled in for a  signed-in caller only. | [optional] 
**max_image_upload_size** | **int** | The largest image the portal accepts as a logo or an avatar, in bytes. Filled in for a signed-in caller  only, and a larger upload is refused rather than resized. | [optional] 
**logo_text** | **str** | The wordmark to print next to the portal logo. It falls back to the built-in one while the portal has  stored no text of its own, so it is never empty. | [optional] 
**external_resources** | [**CultureSpecificExternalResources**](CultureSpecificExternalResources.md) | The addresses of the vendor's help, support, forum and video resources, already picked for the portal  language. An entry is missing when the installation configures no address for it or the resource is  switched off, which `GET api/2.0/settings/rebranding/additional` reports flag by flag. | [optional] 
**default_folder_type** | [**FolderType**](FolderType.md) | The section the client should open after sign-in, which is the caller's own preference rather than a  portal-wide one. Filled in for a signed-in caller only. | [optional] 
**external_db_enabled** | **bool** | Whether the installation has an external database wired up for form results, without which the operations  that write form results there are refused. Filled in for a signed-in caller only. | [optional] 

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


