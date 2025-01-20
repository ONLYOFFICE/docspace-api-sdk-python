from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .....core.tenants.tenant_domain_validator import TenantDomainValidator
    from .....security.cryptography.password_hasher import PasswordHasher
    from .deep_link_dto import DeepLinkDto
    from .firebase_dto import FirebaseDto
    from .form_gallery_dto import FormGalleryDto
    from .plugins_dto import PluginsDto

@dataclass
class SettingsDto(Parsable):
    # API documentation link
    api_docs_link: Optional[str] = None
    # Base domain
    base_domain: Optional[str] = None
    # Email for training booking
    book_training_email: Optional[str] = None
    # Specifies whether the cookie settings are enabled
    cookie_settings_enabled: Optional[bool] = None
    # Language
    culture: Optional[str] = None
    # Specifies if the debug information will be sent or not
    debug_info: Optional[bool] = None
    # The deepLink property
    deep_link: Optional[DeepLinkDto] = None
    # Specifies whether to display the About section
    display_about: Optional[bool] = None
    # Specifies if this is a DocSpace portal or not
    doc_space: Optional[bool] = None
    # Documentation email
    documentation_email: Optional[str] = None
    # The domainValidator property
    domain_validator: Optional[TenantDomainValidator] = None
    # Specifies if a user can send a message to the administrator or not
    enable_adm_mess: Optional[bool] = None
    # Specifies if a user can join to the portal or not
    enabled_join: Optional[bool] = None
    # The firebase property
    firebase: Optional[FirebaseDto] = None
    # The formGallery property
    form_gallery: Optional[FormGalleryDto] = None
    # Link to the forum
    forum_link: Optional[str] = None
    # Greeting settings
    greeting_settings: Optional[str] = None
    # Link to the help
    help_link: Optional[str] = None
    # Invitation limit
    invitation_limit: Optional[int] = None
    # Specifies if this is a AMI instance or not
    is_ami: Optional[bool] = None
    # Legal terms
    legal_terms: Optional[str] = None
    # License url
    license_url: Optional[str] = None
    # Limited access space
    limited_access_space: Optional[bool] = None
    # Max image upload size
    max_image_upload_size: Optional[int] = None
    # Team template ID
    name_schema_id: Optional[str] = None
    # Owner ID
    owner_id: Optional[UUID] = None
    # The passwordHash property
    password_hash: Optional[PasswordHasher] = None
    # The plugins property
    plugins: Optional[PluginsDto] = None
    # ReCAPTCHA public key
    recaptcha_public_key: Optional[str] = None
    # [0 - Default, 1 - AndroidV2, 2 - iOSV2, 3 - hCaptcha]
    recaptcha_type: Optional[int] = None
    # Socket URL
    socket_url: Optional[str] = None
    # Specifies if this is a standalone portal or not
    standalone: Optional[bool] = None
    # Tag manager ID
    tag_manager_id: Optional[str] = None
    # Tenant alias
    tenant_alias: Optional[str] = None
    # [0 - Active, 1 - Suspended, 2 - Remove pending, 3 - Transfering, 4 - Restoring, 5 - Migrating, 6 - Encryption]
    tenant_status: Optional[int] = None
    # Specifies if a user can connect third-party providers or not
    thirdparty_enable: Optional[bool] = None
    # Time zone
    timezone: Optional[str] = None
    # List of trusted domains
    trusted_domains: Optional[List[str]] = None
    # [0 - None, 1 - Custom, 2 - All]
    trusted_domains_type: Optional[int] = None
    # User name validation regex
    user_name_regex: Optional[str] = None
    # UTC hours offset
    utc_hours_offset: Optional[float] = None
    # UTC offset
    utc_offset: Optional[str] = None
    # Version
    version: Optional[str] = None
    # Wizard token
    wizard_token: Optional[str] = None
    # Zendesk key
    zendesk_key: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SettingsDto:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SettingsDto
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SettingsDto()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .....core.tenants.tenant_domain_validator import TenantDomainValidator
        from .....security.cryptography.password_hasher import PasswordHasher
        from .deep_link_dto import DeepLinkDto
        from .firebase_dto import FirebaseDto
        from .form_gallery_dto import FormGalleryDto
        from .plugins_dto import PluginsDto

        from .....core.tenants.tenant_domain_validator import TenantDomainValidator
        from .....security.cryptography.password_hasher import PasswordHasher
        from .deep_link_dto import DeepLinkDto
        from .firebase_dto import FirebaseDto
        from .form_gallery_dto import FormGalleryDto
        from .plugins_dto import PluginsDto

        fields: Dict[str, Callable[[Any], None]] = {
            "apiDocsLink": lambda n : setattr(self, 'api_docs_link', n.get_str_value()),
            "baseDomain": lambda n : setattr(self, 'base_domain', n.get_str_value()),
            "bookTrainingEmail": lambda n : setattr(self, 'book_training_email', n.get_str_value()),
            "cookieSettingsEnabled": lambda n : setattr(self, 'cookie_settings_enabled', n.get_bool_value()),
            "culture": lambda n : setattr(self, 'culture', n.get_str_value()),
            "debugInfo": lambda n : setattr(self, 'debug_info', n.get_bool_value()),
            "deepLink": lambda n : setattr(self, 'deep_link', n.get_object_value(DeepLinkDto)),
            "displayAbout": lambda n : setattr(self, 'display_about', n.get_bool_value()),
            "docSpace": lambda n : setattr(self, 'doc_space', n.get_bool_value()),
            "documentationEmail": lambda n : setattr(self, 'documentation_email', n.get_str_value()),
            "domainValidator": lambda n : setattr(self, 'domain_validator', n.get_object_value(TenantDomainValidator)),
            "enableAdmMess": lambda n : setattr(self, 'enable_adm_mess', n.get_bool_value()),
            "enabledJoin": lambda n : setattr(self, 'enabled_join', n.get_bool_value()),
            "firebase": lambda n : setattr(self, 'firebase', n.get_object_value(FirebaseDto)),
            "formGallery": lambda n : setattr(self, 'form_gallery', n.get_object_value(FormGalleryDto)),
            "forumLink": lambda n : setattr(self, 'forum_link', n.get_str_value()),
            "greetingSettings": lambda n : setattr(self, 'greeting_settings', n.get_str_value()),
            "helpLink": lambda n : setattr(self, 'help_link', n.get_str_value()),
            "invitationLimit": lambda n : setattr(self, 'invitation_limit', n.get_int_value()),
            "isAmi": lambda n : setattr(self, 'is_ami', n.get_bool_value()),
            "legalTerms": lambda n : setattr(self, 'legal_terms', n.get_str_value()),
            "licenseUrl": lambda n : setattr(self, 'license_url', n.get_str_value()),
            "limitedAccessSpace": lambda n : setattr(self, 'limited_access_space', n.get_bool_value()),
            "maxImageUploadSize": lambda n : setattr(self, 'max_image_upload_size', n.get_int_value()),
            "nameSchemaId": lambda n : setattr(self, 'name_schema_id', n.get_str_value()),
            "ownerId": lambda n : setattr(self, 'owner_id', n.get_uuid_value()),
            "passwordHash": lambda n : setattr(self, 'password_hash', n.get_object_value(PasswordHasher)),
            "plugins": lambda n : setattr(self, 'plugins', n.get_object_value(PluginsDto)),
            "recaptchaPublicKey": lambda n : setattr(self, 'recaptcha_public_key', n.get_str_value()),
            "recaptchaType": lambda n : setattr(self, 'recaptcha_type', n.get_int_value()),
            "socketUrl": lambda n : setattr(self, 'socket_url', n.get_str_value()),
            "standalone": lambda n : setattr(self, 'standalone', n.get_bool_value()),
            "tagManagerId": lambda n : setattr(self, 'tag_manager_id', n.get_str_value()),
            "tenantAlias": lambda n : setattr(self, 'tenant_alias', n.get_str_value()),
            "tenantStatus": lambda n : setattr(self, 'tenant_status', n.get_int_value()),
            "thirdpartyEnable": lambda n : setattr(self, 'thirdparty_enable', n.get_bool_value()),
            "timezone": lambda n : setattr(self, 'timezone', n.get_str_value()),
            "trustedDomains": lambda n : setattr(self, 'trusted_domains', n.get_collection_of_primitive_values(str)),
            "trustedDomainsType": lambda n : setattr(self, 'trusted_domains_type', n.get_int_value()),
            "userNameRegex": lambda n : setattr(self, 'user_name_regex', n.get_str_value()),
            "utcHoursOffset": lambda n : setattr(self, 'utc_hours_offset', n.get_float_value()),
            "utcOffset": lambda n : setattr(self, 'utc_offset', n.get_str_value()),
            "version": lambda n : setattr(self, 'version', n.get_str_value()),
            "wizardToken": lambda n : setattr(self, 'wizard_token', n.get_str_value()),
            "zendeskKey": lambda n : setattr(self, 'zendesk_key', n.get_str_value()),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        from .....core.tenants.tenant_domain_validator import TenantDomainValidator
        from .....security.cryptography.password_hasher import PasswordHasher
        from .deep_link_dto import DeepLinkDto
        from .firebase_dto import FirebaseDto
        from .form_gallery_dto import FormGalleryDto
        from .plugins_dto import PluginsDto

        writer.write_str_value("apiDocsLink", self.api_docs_link)
        writer.write_str_value("baseDomain", self.base_domain)
        writer.write_str_value("bookTrainingEmail", self.book_training_email)
        writer.write_bool_value("cookieSettingsEnabled", self.cookie_settings_enabled)
        writer.write_str_value("culture", self.culture)
        writer.write_bool_value("debugInfo", self.debug_info)
        writer.write_object_value("deepLink", self.deep_link)
        writer.write_bool_value("displayAbout", self.display_about)
        writer.write_bool_value("docSpace", self.doc_space)
        writer.write_str_value("documentationEmail", self.documentation_email)
        writer.write_object_value("domainValidator", self.domain_validator)
        writer.write_bool_value("enableAdmMess", self.enable_adm_mess)
        writer.write_bool_value("enabledJoin", self.enabled_join)
        writer.write_object_value("firebase", self.firebase)
        writer.write_object_value("formGallery", self.form_gallery)
        writer.write_str_value("forumLink", self.forum_link)
        writer.write_str_value("greetingSettings", self.greeting_settings)
        writer.write_str_value("helpLink", self.help_link)
        writer.write_int_value("invitationLimit", self.invitation_limit)
        writer.write_bool_value("isAmi", self.is_ami)
        writer.write_str_value("legalTerms", self.legal_terms)
        writer.write_str_value("licenseUrl", self.license_url)
        writer.write_bool_value("limitedAccessSpace", self.limited_access_space)
        writer.write_int_value("maxImageUploadSize", self.max_image_upload_size)
        writer.write_str_value("nameSchemaId", self.name_schema_id)
        writer.write_uuid_value("ownerId", self.owner_id)
        writer.write_object_value("passwordHash", self.password_hash)
        writer.write_object_value("plugins", self.plugins)
        writer.write_str_value("recaptchaPublicKey", self.recaptcha_public_key)
        writer.write_int_value("recaptchaType", self.recaptcha_type)
        writer.write_str_value("socketUrl", self.socket_url)
        writer.write_bool_value("standalone", self.standalone)
        writer.write_str_value("tagManagerId", self.tag_manager_id)
        writer.write_str_value("tenantAlias", self.tenant_alias)
        writer.write_int_value("tenantStatus", self.tenant_status)
        writer.write_bool_value("thirdpartyEnable", self.thirdparty_enable)
        writer.write_str_value("timezone", self.timezone)
        writer.write_collection_of_primitive_values("trustedDomains", self.trusted_domains)
        writer.write_int_value("trustedDomainsType", self.trusted_domains_type)
        writer.write_str_value("userNameRegex", self.user_name_regex)
        writer.write_float_value("utcHoursOffset", self.utc_hours_offset)
        writer.write_str_value("utcOffset", self.utc_offset)
        writer.write_str_value("version", self.version)
        writer.write_str_value("wizardToken", self.wizard_token)
        writer.write_str_value("zendeskKey", self.zendesk_key)
    

