from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .room_invitation import RoomInvitation

@dataclass
class RoomInvitationRequest(Parsable):
    """
    Request parameters for inviting users to a room
    """
    # Culture
    culture: Optional[str] = None
    # Collection of invitation parameters
    invitations: Optional[List[RoomInvitation]] = None
    # Message to send when notifying about the shared room
    message: Optional[str] = None
    # Notifies users about the shared room or not
    notify: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RoomInvitationRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RoomInvitationRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RoomInvitationRequest()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .room_invitation import RoomInvitation

        from .room_invitation import RoomInvitation

        fields: Dict[str, Callable[[Any], None]] = {
            "culture": lambda n : setattr(self, 'culture', n.get_str_value()),
            "invitations": lambda n : setattr(self, 'invitations', n.get_collection_of_object_values(RoomInvitation)),
            "message": lambda n : setattr(self, 'message', n.get_str_value()),
            "notify": lambda n : setattr(self, 'notify', n.get_bool_value()),
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
        from .room_invitation import RoomInvitation

        writer.write_str_value("culture", self.culture)
        writer.write_collection_of_object_values("invitations", self.invitations)
        writer.write_str_value("message", self.message)
        writer.write_bool_value("notify", self.notify)
    

