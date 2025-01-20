from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class SsoIdpSettings(Parsable):
    # Entity ID
    entity_id: Optional[str] = None
    # Name ID format
    name_id_format: Optional[str] = None
    # SLO binding
    slo_binding: Optional[str] = None
    # SLO URL
    slo_url: Optional[str] = None
    # SSO binding
    sso_binding: Optional[str] = None
    # SSO URL
    sso_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SsoIdpSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SsoIdpSettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SsoIdpSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "entityId": lambda n : setattr(self, 'entity_id', n.get_str_value()),
            "nameIdFormat": lambda n : setattr(self, 'name_id_format', n.get_str_value()),
            "sloBinding": lambda n : setattr(self, 'slo_binding', n.get_str_value()),
            "sloUrl": lambda n : setattr(self, 'slo_url', n.get_str_value()),
            "ssoBinding": lambda n : setattr(self, 'sso_binding', n.get_str_value()),
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
        writer.write_str_value("entityId", self.entity_id)
        writer.write_str_value("nameIdFormat", self.name_id_format)
        writer.write_str_value("sloBinding", self.slo_binding)
        writer.write_str_value("sloUrl", self.slo_url)
        writer.write_str_value("ssoBinding", self.sso_binding)
        writer.write_str_value("ssoUrl", self.sso_url)
    

