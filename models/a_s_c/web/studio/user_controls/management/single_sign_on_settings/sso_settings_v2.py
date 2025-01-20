from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .sso_certificate import SsoCertificate
    from .sso_field_mapping import SsoFieldMapping
    from .sso_idp_certificate_advanced import SsoIdpCertificateAdvanced
    from .sso_idp_settings import SsoIdpSettings
    from .sso_sp_certificate_advanced import SsoSpCertificateAdvanced

@dataclass
class SsoSettingsV2(Parsable):
    # Specifies if SSO is enabled or not
    enable_sso: Optional[bool] = None
    # The fieldMapping property
    field_mapping: Optional[SsoFieldMapping] = None
    # Specifies if the authentication page will be hidden or not
    hide_auth_page: Optional[bool] = None
    # The idpCertificateAdvanced property
    idp_certificate_advanced: Optional[SsoIdpCertificateAdvanced] = None
    # List of IDP certificates
    idp_certificates: Optional[List[SsoCertificate]] = None
    # The idpSettings property
    idp_settings: Optional[SsoIdpSettings] = None
    # The spCertificateAdvanced property
    sp_certificate_advanced: Optional[SsoSpCertificateAdvanced] = None
    # List of SP certificates
    sp_certificates: Optional[List[SsoCertificate]] = None
    # SP login label
    sp_login_label: Optional[str] = None
    # Users type (RoomAdmin, User, DocSpaceAdmin)
    users_type: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SsoSettingsV2:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SsoSettingsV2
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SsoSettingsV2()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .sso_certificate import SsoCertificate
        from .sso_field_mapping import SsoFieldMapping
        from .sso_idp_certificate_advanced import SsoIdpCertificateAdvanced
        from .sso_idp_settings import SsoIdpSettings
        from .sso_sp_certificate_advanced import SsoSpCertificateAdvanced

        from .sso_certificate import SsoCertificate
        from .sso_field_mapping import SsoFieldMapping
        from .sso_idp_certificate_advanced import SsoIdpCertificateAdvanced
        from .sso_idp_settings import SsoIdpSettings
        from .sso_sp_certificate_advanced import SsoSpCertificateAdvanced

        fields: Dict[str, Callable[[Any], None]] = {
            "enableSso": lambda n : setattr(self, 'enable_sso', n.get_bool_value()),
            "fieldMapping": lambda n : setattr(self, 'field_mapping', n.get_object_value(SsoFieldMapping)),
            "hideAuthPage": lambda n : setattr(self, 'hide_auth_page', n.get_bool_value()),
            "idpCertificateAdvanced": lambda n : setattr(self, 'idp_certificate_advanced', n.get_object_value(SsoIdpCertificateAdvanced)),
            "idpCertificates": lambda n : setattr(self, 'idp_certificates', n.get_collection_of_object_values(SsoCertificate)),
            "idpSettings": lambda n : setattr(self, 'idp_settings', n.get_object_value(SsoIdpSettings)),
            "spCertificateAdvanced": lambda n : setattr(self, 'sp_certificate_advanced', n.get_object_value(SsoSpCertificateAdvanced)),
            "spCertificates": lambda n : setattr(self, 'sp_certificates', n.get_collection_of_object_values(SsoCertificate)),
            "spLoginLabel": lambda n : setattr(self, 'sp_login_label', n.get_str_value()),
            "usersType": lambda n : setattr(self, 'users_type', n.get_int_value()),
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
        from .sso_certificate import SsoCertificate
        from .sso_field_mapping import SsoFieldMapping
        from .sso_idp_certificate_advanced import SsoIdpCertificateAdvanced
        from .sso_idp_settings import SsoIdpSettings
        from .sso_sp_certificate_advanced import SsoSpCertificateAdvanced

        writer.write_bool_value("enableSso", self.enable_sso)
        writer.write_object_value("fieldMapping", self.field_mapping)
        writer.write_bool_value("hideAuthPage", self.hide_auth_page)
        writer.write_object_value("idpCertificateAdvanced", self.idp_certificate_advanced)
        writer.write_collection_of_object_values("idpCertificates", self.idp_certificates)
        writer.write_object_value("idpSettings", self.idp_settings)
        writer.write_object_value("spCertificateAdvanced", self.sp_certificate_advanced)
        writer.write_collection_of_object_values("spCertificates", self.sp_certificates)
        writer.write_str_value("spLoginLabel", self.sp_login_label)
        writer.write_int_value("usersType", self.users_type)
    

