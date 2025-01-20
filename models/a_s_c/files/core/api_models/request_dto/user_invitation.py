from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

@dataclass
class UserInvitation(Parsable):
    """
    User invitation parameters
    """
    # Resend all
    resend_all: Optional[bool] = None
    # List of user IDs
    users_ids: Optional[List[UUID]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UserInvitation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UserInvitation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UserInvitation()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "resendAll": lambda n : setattr(self, 'resend_all', n.get_bool_value()),
            "usersIds": lambda n : setattr(self, 'users_ids', n.get_collection_of_primitive_values(UUID)),
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
        writer.write_bool_value("resendAll", self.resend_all)
        writer.write_collection_of_primitive_values("usersIds", self.users_ids)
    

