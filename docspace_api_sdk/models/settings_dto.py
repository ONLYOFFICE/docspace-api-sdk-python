#
# (c) Copyright Ascensio System SIA 2026
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#



from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from uuid import UUID
from docspace_api_sdk.models.culture_specific_external_resources import CultureSpecificExternalResources
from docspace_api_sdk.models.deep_link_dto import DeepLinkDto
from docspace_api_sdk.models.firebase_dto import FirebaseDto
from docspace_api_sdk.models.folder_type import FolderType
from docspace_api_sdk.models.form_gallery_dto import FormGalleryDto
from docspace_api_sdk.models.password_hasher import PasswordHasher
from docspace_api_sdk.models.plugins_dto import PluginsDto
from docspace_api_sdk.models.recaptcha_type import RecaptchaType
from docspace_api_sdk.models.tenant_domain_validator import TenantDomainValidator
from docspace_api_sdk.models.tenant_status import TenantStatus
from docspace_api_sdk.models.tenant_trusted_domains_type import TenantTrustedDomainsType
from typing import Optional, Set
from typing_extensions import Self

class SettingsDto(BaseModel):
    """
    The general configuration of the current portal, as the client shell needs it before and after sign-in.
    """ # noqa: E501
    timezone: Optional[StrictStr] = Field(default=None, description="The portal time zone as an IANA identifier, which is the zone every date this API returns in portal time  is expressed in. Filled in for a signed-in caller only.", json_schema_extra={"examples": ["UTC"]})
    trusted_domains: Optional[List[StrictStr]] = Field(default=None, description="The mail domains a new member may register or be invited from without confirming the address. It is filled  in for a signed-in caller, and for an anonymous one only while `enabledJoin` is `true`; it is empty  whenever `trustedDomainsType` is not `Custom`.", alias="trustedDomains", json_schema_extra={"examples": [["mydomain.com", "mydomain1.com"]]})
    trusted_domains_type: Optional[TenantTrustedDomainsType] = Field(default=None, description="How the mail domains above are applied: no domain trusted, every domain trusted, or only the listed ones.  Filled in under the same conditions as `trustedDomains`.", alias="trustedDomainsType")
    culture: Optional[StrictStr] = Field(description="The default language of the portal as a culture name, which is what unauthenticated pages are rendered in.  A signed-in member may have a language of their own, and that one is not reported here.", json_schema_extra={"examples": ["en-US"]})
    utc_offset: Optional[StrictStr] = Field(default=None, description="The portal's offset from UTC as a time span, positive east of UTC. Filled in for a signed-in caller only,  and taken at the moment of the call, so it already reflects daylight saving time.", alias="utcOffset", json_schema_extra={"examples": ["-08:30:00"]})
    utc_hours_offset: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The same offset in hours, fractional for a zone that is not on a whole hour. It is there so a client does  not have to parse `utcOffset`.", alias="utcHoursOffset", json_schema_extra={"examples": [-8.5]})
    greeting_settings: Optional[StrictStr] = Field(default=None, description="The portal title shown on the login page and in letters. It falls back to the product name in the portal  language while the portal has been given no title of its own.", alias="greetingSettings", json_schema_extra={"examples": ["Web Office Applications"]})
    owner_id: Optional[UUID] = Field(default=None, description="The portal owner, the one account that cannot be removed or demoted. Filled in for a signed-in caller  only, and the empty GUID for an anonymous one.", alias="ownerId", json_schema_extra={"examples": ["00000000-0000-0000-0000-000000000000"]})
    name_schema_id: Optional[StrictStr] = Field(default=None, description="The naming scheme the portal uses for its own vocabulary - what a member, a group or a room is called in  the interface. `GET api/2.0/settings/customschemas/{id}` spells that vocabulary out. Filled in for a  signed-in caller only.", alias="nameSchemaId", json_schema_extra={"examples": ["default"]})
    enabled_join: Optional[StrictBool] = Field(default=None, description="Whether someone who is not invited may still register, which is the case when the portal trusts every mail  domain or a list of them. It is computed for an anonymous caller only and left out entirely for a  signed-in one, so a missing value is not a `false`.", alias="enabledJoin", json_schema_extra={"examples": [True]})
    enable_adm_mess: Optional[StrictBool] = Field(default=None, description="Whether the login page may offer the form for writing to the portal administrators. It is also `true`  while the portal's payment has lapsed, whatever the setting says, so it can be set on a portal where an  administrator switched the form off.", alias="enableAdmMess", json_schema_extra={"examples": [True]})
    thirdparty_enable: Optional[StrictBool] = Field(default=None, description="Whether the login page may offer sign-in through an external identity provider. It is computed for an  anonymous caller only; `GET api/2.0/capabilities` reports the same thing with the list of providers.", alias="thirdpartyEnable", json_schema_extra={"examples": [True]})
    doc_space: Optional[StrictBool] = Field(default=None, description="Always `true` in this product. It exists so a client that also talks to older ONLYOFFICE portals can tell  them apart, and is not a feature switch.", alias="docSpace", json_schema_extra={"examples": [True]})
    standalone: Optional[StrictBool] = Field(default=None, description="Whether this is a server installation someone administers themselves rather than a portal in the cloud.  Several fields below and a number of operations behave differently in the two, so a client that has to  branch on the deployment reads it here.", json_schema_extra={"examples": [True]})
    is_ami: Optional[StrictBool] = Field(default=None, description="Whether the installation runs from an Amazon machine image, which is a server installation that can read  its own instance metadata. It is `false` on every cloud portal.", alias="isAmi", json_schema_extra={"examples": [True]})
    base_domain: Optional[StrictStr] = Field(description="The domain new portals of this installation are created under, which is what a portal name is checked  against and appended to. It is empty on an installation that serves a single portal on a fixed address.", alias="baseDomain", json_schema_extra={"examples": ["example.com"]})
    wizard_token: Optional[StrictStr] = Field(default=None, description="The token that authorizes the first-run setup wizard. It is handed out to anonymous callers only, and only  while the wizard has not been completed; once it has, the field stays empty for good.", alias="wizardToken", json_schema_extra={"examples": ["dGhpc2lzYXRva2Vu..."]})
    password_hash: Optional[PasswordHasher] = Field(default=None, description="The parameters for hashing a password in the client before it is sent - the salt, the iteration count and  the hash size. It is filled in for an anonymous caller and, for a signed-in one, only when  `withPassword=true` is asked for. Hash with exactly these parameters and send the result as  `passwordHash`, since the portal cannot reproduce the hash from a different set.", alias="passwordHash")
    firebase: Optional[FirebaseDto] = Field(default=None, description="The Firebase project a mobile or web client sends push registrations to. Filled in for a signed-in caller  only, and its own fields are empty strings on an installation that configures no Firebase project.")
    version: Optional[StrictStr] = Field(default=None, description="The product version of the portal, empty when the installation does not publish one. It is the version of  the server, not of this API, whose own version is fixed at 2.0.", json_schema_extra={"examples": ["12.5.0"]})
    recaptcha_type: Optional[RecaptchaType] = Field(default=None, description="Which CAPTCHA the login form has to render, decided by the installation's configuration. Computed for an  anonymous caller only.", alias="recaptchaType")
    recaptcha_public_key: Optional[StrictStr] = Field(default=None, description="The site key for the CAPTCHA named by `recaptchaType`, safe to embed in a page. It is empty when the  installation configures no CAPTCHA, in which case the login form asks for none.", alias="recaptchaPublicKey", json_schema_extra={"examples": ["abc123def456"]})
    debug_info: Optional[StrictBool] = Field(default=None, description="Whether the client may collect and send diagnostic information. Filled in for a signed-in caller only, and  `false` unless the installation switched it on.", alias="debugInfo", json_schema_extra={"examples": [True]})
    socket_url: Optional[StrictStr] = Field(default=None, description="The address of the socket service that pushes live updates to a client. It is filled in for a signed-in  caller and for an anonymous one who arrives with an external sharing link, and is empty when the  installation runs no socket service - a client then has to poll.", alias="socketUrl", json_schema_extra={"examples": ["https://example.com"]})
    tenant_status: Optional[TenantStatus] = Field(default=None, description="The lifecycle state of the portal. Anything other than active means most operations are refused for the  moment, because the portal is being transferred, restored, encrypted or removed.", alias="tenantStatus")
    tenant_alias: Optional[StrictStr] = Field(default=None, description="The portal's own name within the installation, which together with `baseDomain` forms the address it is  reached at. `PUT api/2.0/portal/portalrename` changes it.", alias="tenantAlias", json_schema_extra={"examples": ["mycompany"]})
    display_about: Optional[StrictBool] = Field(default=None, description="Whether the interface may show the About page. A cloud portal always may; a server installation may unless  its plan includes branding and the vendor details hide the page.", alias="displayAbout", json_schema_extra={"examples": [True]})
    domain_validator: Optional[TenantDomainValidator] = Field(default=None, description="The rules a portal name is checked against - its length limits and the pattern it has to match - so a  client can validate a rename before sending it. Filled in for a signed-in caller only.", alias="domainValidator")
    zendesk_key: Optional[StrictStr] = Field(default=None, description="The key that lets the client open the vendor's support chat, empty when the installation configures none.  Filled in for a signed-in caller only.", alias="zendeskKey", json_schema_extra={"examples": ["abc123def456"]})
    tag_manager_id: Optional[StrictStr] = Field(default=None, description="The Google Tag Manager container the client should load, empty when the installation configures none.  Filled in for a signed-in caller only.", alias="tagManagerId", json_schema_extra={"examples": ["GTM-XXXXXX"]})
    cookie_settings_enabled: StrictBool = Field(description="Whether the portal limits how long an authentication session stays valid. The limit itself is read with  `GET api/2.0/settings/cookiesettings`; while this is `false` a session is honoured for a year.", alias="cookieSettingsEnabled", json_schema_extra={"examples": [True]})
    limited_access_space: Optional[StrictBool] = Field(default=None, description="Whether the space-management section is restricted to the portal owner. Filled in for a signed-in caller  only.", alias="limitedAccessSpace", json_schema_extra={"examples": [True]})
    limited_access_dev_tools_for_users: Optional[StrictBool] = Field(default=None, description="Whether the Developer Tools section is hidden from members who are not administrators. Filled in for a  signed-in caller only.", alias="limitedAccessDevToolsForUsers", json_schema_extra={"examples": [True]})
    display_banners: Optional[StrictBool] = Field(default=None, description="Whether the interface may show the vendor's promotional banners. A cloud portal always reports `true`; on  a server installation it follows the banner setting. Filled in for a signed-in caller only.", alias="displayBanners", json_schema_extra={"examples": [True]})
    ai_enabled: Optional[StrictBool] = Field(default=None, description="Whether the AI features - chat, agents and vectorisation - may be used on this portal. While it is  `false` the AI Agents folder is hidden and the AI operations are refused. Filled in for a signed-in caller  only.", alias="aiEnabled", json_schema_extra={"examples": [True]})
    wallet_low_balance: Optional[StrictBool] = Field(default=None, description="Whether the portal wallet has already dropped below its low-balance threshold, so a client can warn about  AI operations being cut off. It is reported to DocSpace administrators only and left empty for everyone  else, which is not the same as a healthy balance.", alias="walletLowBalance", json_schema_extra={"examples": [False]})
    user_name_regex: Optional[StrictStr] = Field(default=None, description="The pattern a member's first and last name has to match, so a client can validate a name before sending  it. It is a .NET regular expression and is applied to each name part separately.", alias="userNameRegex", json_schema_extra={"examples": ["^[a-zA-Z0-9_]{3,20}$"]})
    invitation_limit: Optional[StrictInt] = Field(default=None, description="How many invitations the portal may still send in the current window. Filled in for a signed-in caller  only, and set to the maximum value of a 32-bit integer on an installation that limits nothing.", alias="invitationLimit", json_schema_extra={"examples": [10]})
    plugins: Optional[PluginsDto] = Field(default=None, description="What the installation allows to be done with web plugins. Filled in for a signed-in caller only, with all  three flags `false` unless the installation switched plugins on.")
    deep_link: DeepLinkDto = Field(description="What a mobile client needs to hand a document link over to the installed application instead of opening it  in the browser. Its fields are empty strings when the installation configures no application.", alias="deepLink")
    form_gallery: Optional[FormGalleryDto] = Field(default=None, description="Where the ready-made form templates are served from and which extension they carry. Filled in for a  signed-in caller only.", alias="formGallery")
    max_image_upload_size: Optional[StrictInt] = Field(default=None, description="The largest image the portal accepts as a logo or an avatar, in bytes. Filled in for a signed-in caller  only, and a larger upload is refused rather than resized.", alias="maxImageUploadSize", json_schema_extra={"examples": [10485760]})
    logo_text: Optional[StrictStr] = Field(default=None, description="The wordmark to print next to the portal logo. It falls back to the built-in one while the portal has  stored no text of its own, so it is never empty.", alias="logoText", json_schema_extra={"examples": ["Company Name"]})
    external_resources: Optional[CultureSpecificExternalResources] = Field(default=None, description="The addresses of the vendor's help, support, forum and video resources, already picked for the portal  language. An entry is missing when the installation configures no address for it or the resource is  switched off, which `GET api/2.0/settings/rebranding/additional` reports flag by flag.", alias="externalResources")
    default_folder_type: Optional[FolderType] = Field(default=None, description="The section the client should open after sign-in, which is the caller's own preference rather than a  portal-wide one. Filled in for a signed-in caller only.", alias="defaultFolderType")
    external_db_enabled: Optional[StrictBool] = Field(default=None, description="Whether the installation has an external database wired up for form results, without which the operations  that write form results there are refused. Filled in for a signed-in caller only.", alias="externalDbEnabled", json_schema_extra={"examples": [True]})
    __properties: ClassVar[List[str]] = ["timezone", "trustedDomains", "trustedDomainsType", "culture", "utcOffset", "utcHoursOffset", "greetingSettings", "ownerId", "nameSchemaId", "enabledJoin", "enableAdmMess", "thirdpartyEnable", "docSpace", "standalone", "isAmi", "baseDomain", "wizardToken", "passwordHash", "firebase", "version", "recaptchaType", "recaptchaPublicKey", "debugInfo", "socketUrl", "tenantStatus", "tenantAlias", "displayAbout", "domainValidator", "zendeskKey", "tagManagerId", "cookieSettingsEnabled", "limitedAccessSpace", "limitedAccessDevToolsForUsers", "displayBanners", "aiEnabled", "walletLowBalance", "userNameRegex", "invitationLimit", "plugins", "deepLink", "formGallery", "maxImageUploadSize", "logoText", "externalResources", "defaultFolderType", "externalDbEnabled"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of SettingsDto from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of password_hash
        if self.password_hash:
            _dict['passwordHash'] = self.password_hash.to_dict()
        # override the default output from pydantic by calling `to_dict()` of firebase
        if self.firebase:
            _dict['firebase'] = self.firebase.to_dict()
        # override the default output from pydantic by calling `to_dict()` of domain_validator
        if self.domain_validator:
            _dict['domainValidator'] = self.domain_validator.to_dict()
        # override the default output from pydantic by calling `to_dict()` of plugins
        if self.plugins:
            _dict['plugins'] = self.plugins.to_dict()
        # override the default output from pydantic by calling `to_dict()` of deep_link
        if self.deep_link:
            _dict['deepLink'] = self.deep_link.to_dict()
        # override the default output from pydantic by calling `to_dict()` of form_gallery
        if self.form_gallery:
            _dict['formGallery'] = self.form_gallery.to_dict()
        # override the default output from pydantic by calling `to_dict()` of external_resources
        if self.external_resources:
            _dict['externalResources'] = self.external_resources.to_dict()
        # set to None if timezone (nullable) is None
        # and model_fields_set contains the field
        if self.timezone is None and "timezone" in self.model_fields_set:
            _dict['timezone'] = None

        # set to None if trusted_domains (nullable) is None
        # and model_fields_set contains the field
        if self.trusted_domains is None and "trusted_domains" in self.model_fields_set:
            _dict['trustedDomains'] = None

        # set to None if culture (nullable) is None
        # and model_fields_set contains the field
        if self.culture is None and "culture" in self.model_fields_set:
            _dict['culture'] = None

        # set to None if greeting_settings (nullable) is None
        # and model_fields_set contains the field
        if self.greeting_settings is None and "greeting_settings" in self.model_fields_set:
            _dict['greetingSettings'] = None

        # set to None if name_schema_id (nullable) is None
        # and model_fields_set contains the field
        if self.name_schema_id is None and "name_schema_id" in self.model_fields_set:
            _dict['nameSchemaId'] = None

        # set to None if enabled_join (nullable) is None
        # and model_fields_set contains the field
        if self.enabled_join is None and "enabled_join" in self.model_fields_set:
            _dict['enabledJoin'] = None

        # set to None if enable_adm_mess (nullable) is None
        # and model_fields_set contains the field
        if self.enable_adm_mess is None and "enable_adm_mess" in self.model_fields_set:
            _dict['enableAdmMess'] = None

        # set to None if thirdparty_enable (nullable) is None
        # and model_fields_set contains the field
        if self.thirdparty_enable is None and "thirdparty_enable" in self.model_fields_set:
            _dict['thirdpartyEnable'] = None

        # set to None if base_domain (nullable) is None
        # and model_fields_set contains the field
        if self.base_domain is None and "base_domain" in self.model_fields_set:
            _dict['baseDomain'] = None

        # set to None if wizard_token (nullable) is None
        # and model_fields_set contains the field
        if self.wizard_token is None and "wizard_token" in self.model_fields_set:
            _dict['wizardToken'] = None

        # set to None if version (nullable) is None
        # and model_fields_set contains the field
        if self.version is None and "version" in self.model_fields_set:
            _dict['version'] = None

        # set to None if recaptcha_public_key (nullable) is None
        # and model_fields_set contains the field
        if self.recaptcha_public_key is None and "recaptcha_public_key" in self.model_fields_set:
            _dict['recaptchaPublicKey'] = None

        # set to None if socket_url (nullable) is None
        # and model_fields_set contains the field
        if self.socket_url is None and "socket_url" in self.model_fields_set:
            _dict['socketUrl'] = None

        # set to None if tenant_alias (nullable) is None
        # and model_fields_set contains the field
        if self.tenant_alias is None and "tenant_alias" in self.model_fields_set:
            _dict['tenantAlias'] = None

        # set to None if zendesk_key (nullable) is None
        # and model_fields_set contains the field
        if self.zendesk_key is None and "zendesk_key" in self.model_fields_set:
            _dict['zendeskKey'] = None

        # set to None if tag_manager_id (nullable) is None
        # and model_fields_set contains the field
        if self.tag_manager_id is None and "tag_manager_id" in self.model_fields_set:
            _dict['tagManagerId'] = None

        # set to None if wallet_low_balance (nullable) is None
        # and model_fields_set contains the field
        if self.wallet_low_balance is None and "wallet_low_balance" in self.model_fields_set:
            _dict['walletLowBalance'] = None

        # set to None if user_name_regex (nullable) is None
        # and model_fields_set contains the field
        if self.user_name_regex is None and "user_name_regex" in self.model_fields_set:
            _dict['userNameRegex'] = None

        # set to None if invitation_limit (nullable) is None
        # and model_fields_set contains the field
        if self.invitation_limit is None and "invitation_limit" in self.model_fields_set:
            _dict['invitationLimit'] = None

        # set to None if logo_text (nullable) is None
        # and model_fields_set contains the field
        if self.logo_text is None and "logo_text" in self.model_fields_set:
            _dict['logoText'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SettingsDto from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "timezone": obj.get("timezone"),
            "trustedDomains": obj.get("trustedDomains"),
            "trustedDomainsType": obj.get("trustedDomainsType"),
            "culture": obj.get("culture"),
            "utcOffset": obj.get("utcOffset"),
            "utcHoursOffset": obj.get("utcHoursOffset"),
            "greetingSettings": obj.get("greetingSettings"),
            "ownerId": obj.get("ownerId"),
            "nameSchemaId": obj.get("nameSchemaId"),
            "enabledJoin": obj.get("enabledJoin"),
            "enableAdmMess": obj.get("enableAdmMess"),
            "thirdpartyEnable": obj.get("thirdpartyEnable"),
            "docSpace": obj.get("docSpace"),
            "standalone": obj.get("standalone"),
            "isAmi": obj.get("isAmi"),
            "baseDomain": obj.get("baseDomain"),
            "wizardToken": obj.get("wizardToken"),
            "passwordHash": PasswordHasher.from_dict(obj["passwordHash"]) if obj.get("passwordHash") is not None else None,
            "firebase": FirebaseDto.from_dict(obj["firebase"]) if obj.get("firebase") is not None else None,
            "version": obj.get("version"),
            "recaptchaType": obj.get("recaptchaType"),
            "recaptchaPublicKey": obj.get("recaptchaPublicKey"),
            "debugInfo": obj.get("debugInfo"),
            "socketUrl": obj.get("socketUrl"),
            "tenantStatus": obj.get("tenantStatus"),
            "tenantAlias": obj.get("tenantAlias"),
            "displayAbout": obj.get("displayAbout"),
            "domainValidator": TenantDomainValidator.from_dict(obj["domainValidator"]) if obj.get("domainValidator") is not None else None,
            "zendeskKey": obj.get("zendeskKey"),
            "tagManagerId": obj.get("tagManagerId"),
            "cookieSettingsEnabled": obj.get("cookieSettingsEnabled"),
            "limitedAccessSpace": obj.get("limitedAccessSpace"),
            "limitedAccessDevToolsForUsers": obj.get("limitedAccessDevToolsForUsers"),
            "displayBanners": obj.get("displayBanners"),
            "aiEnabled": obj.get("aiEnabled"),
            "walletLowBalance": obj.get("walletLowBalance"),
            "userNameRegex": obj.get("userNameRegex"),
            "invitationLimit": obj.get("invitationLimit"),
            "plugins": PluginsDto.from_dict(obj["plugins"]) if obj.get("plugins") is not None else None,
            "deepLink": DeepLinkDto.from_dict(obj["deepLink"]) if obj.get("deepLink") is not None else None,
            "formGallery": FormGalleryDto.from_dict(obj["formGallery"]) if obj.get("formGallery") is not None else None,
            "maxImageUploadSize": obj.get("maxImageUploadSize"),
            "logoText": obj.get("logoText"),
            "externalResources": CultureSpecificExternalResources.from_dict(obj["externalResources"]) if obj.get("externalResources") is not None else None,
            "defaultFolderType": obj.get("defaultFolderType"),
            "externalDbEnabled": obj.get("externalDbEnabled")
        })
        return _obj


