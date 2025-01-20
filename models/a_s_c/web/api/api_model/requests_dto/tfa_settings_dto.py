from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

@dataclass
class TfaSettingsDto(Parsable):
    # Specifies if the TFA settings are available or not
    avaliable: Optional[bool] = None
    # Specifies if the TFA settings are enabled or not
    enabled: Optional[bool] = None
    # ID
    id: Optional[str] = None
    # List of groups who must use the TFA verification
    mandatory_groups: Optional[List[UUID]] = None
    # List of users who must use the TFA verification
    mandatory_users: Optional[List[UUID]] = None
    # Title
    title: Optional[str] = None
    # List of trusted IP addresses
    trusted_ips: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TfaSettingsDto:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TfaSettingsDto
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TfaSettingsDto()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "avaliable": lambda n : setattr(self, 'avaliable', n.get_bool_value()),
            "enabled": lambda n : setattr(self, 'enabled', n.get_bool_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "mandatoryGroups": lambda n : setattr(self, 'mandatory_groups', n.get_collection_of_primitive_values(UUID)),
            "mandatoryUsers": lambda n : setattr(self, 'mandatory_users', n.get_collection_of_primitive_values(UUID)),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
            "trustedIps": lambda n : setattr(self, 'trusted_ips', n.get_collection_of_primitive_values(str)),
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
        writer.write_bool_value("avaliable", self.avaliable)
        writer.write_bool_value("enabled", self.enabled)
        writer.write_str_value("id", self.id)
        writer.write_collection_of_primitive_values("mandatoryGroups", self.mandatory_groups)
        writer.write_collection_of_primitive_values("mandatoryUsers", self.mandatory_users)
        writer.write_str_value("title", self.title)
        writer.write_collection_of_primitive_values("trustedIps", self.trusted_ips)
    

