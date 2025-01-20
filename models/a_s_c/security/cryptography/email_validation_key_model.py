from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

@dataclass
class EmailValidationKeyModel(Parsable):
    """
    Confirmation email parameters
    """
    # Email
    email: Optional[str] = None
    # [0 - All, 1 - Room admin, 2 - Guest, 3 - DocSpace admin, 4 - User]
    empl_type: Optional[int] = None
    # Access an account for the first time or not
    first: Optional[str] = None
    # Key
    key: Optional[str] = None
    # Room ID
    room_id: Optional[str] = None
    # [0 - Emp invite, 1 - Link invite, 2 - Portal suspend, 3 - Portal continue, 4 - Portal remove, 5 - Dns change, 6 - Portal owner change, 7 - Activation, 8 - Email change, 9 - Email activation, 10 - Password change, 11 - Profile remove, 12 - Phone activation, 13 - Phone auth, 14 - Auth, 15 - Tfa activation, 16 - Tfa auth, 17 - Wizard]
    type: Optional[int] = None
    # User ID
    ui_d: Optional[UUID] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EmailValidationKeyModel:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EmailValidationKeyModel
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EmailValidationKeyModel()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "emplType": lambda n : setattr(self, 'empl_type', n.get_int_value()),
            "first": lambda n : setattr(self, 'first', n.get_str_value()),
            "key": lambda n : setattr(self, 'key', n.get_str_value()),
            "roomId": lambda n : setattr(self, 'room_id', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_int_value()),
            "uiD": lambda n : setattr(self, 'ui_d', n.get_uuid_value()),
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
        writer.write_int_value("emplType", self.empl_type)
        writer.write_str_value("first", self.first)
        writer.write_str_value("key", self.key)
        writer.write_str_value("roomId", self.room_id)
        writer.write_int_value("type", self.type)
        writer.write_uuid_value("uiD", self.ui_d)
    

