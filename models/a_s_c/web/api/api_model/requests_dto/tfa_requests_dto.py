from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

@dataclass
class TfaRequestsDto(Parsable):
    """
    TFA settings request parameters
    """
    # User ID
    id: Optional[UUID] = None
    # List of groups who must use the TFA verification
    mandatory_groups: Optional[List[UUID]] = None
    # List of users who must use the TFA verification
    mandatory_users: Optional[List[UUID]] = None
    # List of trusted IP addresses
    trusted_ips: Optional[List[str]] = None
    # [0 - None, 1 - Sms, 2 - App]
    type: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TfaRequestsDto:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TfaRequestsDto
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TfaRequestsDto()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "id": lambda n : setattr(self, 'id', n.get_uuid_value()),
            "mandatoryGroups": lambda n : setattr(self, 'mandatory_groups', n.get_collection_of_primitive_values(UUID)),
            "mandatoryUsers": lambda n : setattr(self, 'mandatory_users', n.get_collection_of_primitive_values(UUID)),
            "trustedIps": lambda n : setattr(self, 'trusted_ips', n.get_collection_of_primitive_values(str)),
            "type": lambda n : setattr(self, 'type', n.get_int_value()),
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
        writer.write_uuid_value("id", self.id)
        writer.write_collection_of_primitive_values("mandatoryGroups", self.mandatory_groups)
        writer.write_collection_of_primitive_values("mandatoryUsers", self.mandatory_users)
        writer.write_collection_of_primitive_values("trustedIps", self.trusted_ips)
        writer.write_int_value("type", self.type)
    

