from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....i_p_security.ip_restriction_base import IpRestrictionBase

@dataclass
class IpRestrictionsDto(Parsable):
    """
    New IP restriction settings
    """
    # Enables IP restrictions or not
    enable: Optional[bool] = None
    # List of IP addresses
    ip_restrictions: Optional[List[IpRestrictionBase]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> IpRestrictionsDto:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: IpRestrictionsDto
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return IpRestrictionsDto()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .....i_p_security.ip_restriction_base import IpRestrictionBase

        from .....i_p_security.ip_restriction_base import IpRestrictionBase

        fields: Dict[str, Callable[[Any], None]] = {
            "enable": lambda n : setattr(self, 'enable', n.get_bool_value()),
            "ipRestrictions": lambda n : setattr(self, 'ip_restrictions', n.get_collection_of_object_values(IpRestrictionBase)),
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
        from .....i_p_security.ip_restriction_base import IpRestrictionBase

        writer.write_bool_value("enable", self.enable)
        writer.write_collection_of_object_values("ipRestrictions", self.ip_restrictions)
    

