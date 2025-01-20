from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class CapabilitiesDto(Parsable):
    # The identityServerEnabled property
    identity_server_enabled: Optional[bool] = None
    # Ldap domain
    ldap_domain: Optional[str] = None
    # Specifies if the LDAP settings are enabled or not
    ldap_enabled: Optional[bool] = None
    # Specifies if OAuth is enabled or not
    oauth_enabled: Optional[bool] = None
    # List of providers
    providers: Optional[List[str]] = None
    # SP login label
    sso_label: Optional[str] = None
    # SSO URL. If this parameter is empty, then the SSO settings are disabled
    sso_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CapabilitiesDto:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CapabilitiesDto
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CapabilitiesDto()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "identityServerEnabled": lambda n : setattr(self, 'identity_server_enabled', n.get_bool_value()),
            "ldapDomain": lambda n : setattr(self, 'ldap_domain', n.get_str_value()),
            "ldapEnabled": lambda n : setattr(self, 'ldap_enabled', n.get_bool_value()),
            "oauthEnabled": lambda n : setattr(self, 'oauth_enabled', n.get_bool_value()),
            "providers": lambda n : setattr(self, 'providers', n.get_collection_of_primitive_values(str)),
            "ssoLabel": lambda n : setattr(self, 'sso_label', n.get_str_value()),
            "ssoUrl": lambda n : setattr(self, 'sso_url', n.get_str_value()),
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
        writer.write_bool_value("identityServerEnabled", self.identity_server_enabled)
        writer.write_str_value("ldapDomain", self.ldap_domain)
        writer.write_bool_value("ldapEnabled", self.ldap_enabled)
        writer.write_bool_value("oauthEnabled", self.oauth_enabled)
        writer.write_collection_of_primitive_values("providers", self.providers)
        writer.write_str_value("ssoLabel", self.sso_label)
        writer.write_str_value("ssoUrl", self.sso_url)
    

