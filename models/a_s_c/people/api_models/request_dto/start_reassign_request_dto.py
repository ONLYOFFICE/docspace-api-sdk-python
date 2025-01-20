from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

@dataclass
class StartReassignRequestDto(Parsable):
    """
    Request parameters for starting the reassignment process
    """
    # Specifies whether to delete a profile when the data reassignment will be finished or not
    delete_profile: Optional[bool] = None
    # User ID whose data will be reassigned to another user
    from_user_id: Optional[UUID] = None
    # User ID to whom all the data will be reassigned
    to_user_id: Optional[UUID] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> StartReassignRequestDto:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: StartReassignRequestDto
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return StartReassignRequestDto()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "deleteProfile": lambda n : setattr(self, 'delete_profile', n.get_bool_value()),
            "fromUserId": lambda n : setattr(self, 'from_user_id', n.get_uuid_value()),
            "toUserId": lambda n : setattr(self, 'to_user_id', n.get_uuid_value()),
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
        writer.write_bool_value("deleteProfile", self.delete_profile)
        writer.write_uuid_value("fromUserId", self.from_user_id)
        writer.write_uuid_value("toUserId", self.to_user_id)
    

