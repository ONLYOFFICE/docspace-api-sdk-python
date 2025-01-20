from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

@dataclass
class SecurityRequestsDto(Parsable):
    """
    Security request parameters
    """
    # Administrator or not
    administrator: Optional[bool] = None
    # Product ID
    product_id: Optional[UUID] = None
    # User ID
    user_id: Optional[UUID] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SecurityRequestsDto:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SecurityRequestsDto
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SecurityRequestsDto()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "administrator": lambda n : setattr(self, 'administrator', n.get_bool_value()),
            "productId": lambda n : setattr(self, 'product_id', n.get_uuid_value()),
            "userId": lambda n : setattr(self, 'user_id', n.get_uuid_value()),
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
        writer.write_bool_value("administrator", self.administrator)
        writer.write_uuid_value("productId", self.product_id)
        writer.write_uuid_value("userId", self.user_id)
    

