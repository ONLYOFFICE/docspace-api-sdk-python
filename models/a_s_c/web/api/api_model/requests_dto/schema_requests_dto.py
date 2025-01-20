from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class SchemaRequestsDto(Parsable):
    """
    Team template parameters
    """
    # Group caption
    group_caption: Optional[str] = None
    # Group lead caption
    group_head_caption: Optional[str] = None
    # Groups caption
    groups_caption: Optional[str] = None
    # Guest caption
    guest_caption: Optional[str] = None
    # Guests caption
    guests_caption: Optional[str] = None
    # Team template ID
    id: Optional[str] = None
    # Team template name
    name: Optional[str] = None
    # Registration date caption
    reg_date_caption: Optional[str] = None
    # User caption
    user_caption: Optional[str] = None
    # User status caption
    user_post_caption: Optional[str] = None
    # Users caption
    users_caption: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SchemaRequestsDto:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SchemaRequestsDto
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SchemaRequestsDto()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "groupCaption": lambda n : setattr(self, 'group_caption', n.get_str_value()),
            "groupHeadCaption": lambda n : setattr(self, 'group_head_caption', n.get_str_value()),
            "groupsCaption": lambda n : setattr(self, 'groups_caption', n.get_str_value()),
            "guestCaption": lambda n : setattr(self, 'guest_caption', n.get_str_value()),
            "guestsCaption": lambda n : setattr(self, 'guests_caption', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "regDateCaption": lambda n : setattr(self, 'reg_date_caption', n.get_str_value()),
            "userCaption": lambda n : setattr(self, 'user_caption', n.get_str_value()),
            "userPostCaption": lambda n : setattr(self, 'user_post_caption', n.get_str_value()),
            "usersCaption": lambda n : setattr(self, 'users_caption', n.get_str_value()),
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
        writer.write_str_value("groupCaption", self.group_caption)
        writer.write_str_value("groupHeadCaption", self.group_head_caption)
        writer.write_str_value("groupsCaption", self.groups_caption)
        writer.write_str_value("guestCaption", self.guest_caption)
        writer.write_str_value("guestsCaption", self.guests_caption)
        writer.write_str_value("id", self.id)
        writer.write_str_value("name", self.name)
        writer.write_str_value("regDateCaption", self.reg_date_caption)
        writer.write_str_value("userCaption", self.user_caption)
        writer.write_str_value("userPostCaption", self.user_post_caption)
        writer.write_str_value("usersCaption", self.users_caption)
    

