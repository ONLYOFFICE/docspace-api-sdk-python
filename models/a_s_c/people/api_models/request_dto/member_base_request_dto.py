from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class MemberBaseRequestDto(Parsable):
    """
    Request parameters for setting new password
    """
    # Email
    email: Optional[str] = None
    # Password
    password: Optional[str] = None
    # Password hash
    password_hash: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MemberBaseRequestDto:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MemberBaseRequestDto
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MemberBaseRequestDto()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "password": lambda n : setattr(self, 'password', n.get_str_value()),
            "passwordHash": lambda n : setattr(self, 'password_hash', n.get_str_value()),
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
        writer.write_str_value("email", self.email)
        writer.write_str_value("password", self.password)
        writer.write_str_value("passwordHash", self.password_hash)
    

