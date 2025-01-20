from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

@dataclass
class EmployeeDto(Parsable):
    # Avatar
    avatar: Optional[str] = None
    # Maximum size avatar
    avatar_max: Optional[str] = None
    # Medium size avatar
    avatar_medium: Optional[str] = None
    # Original size avatar
    avatar_original: Optional[str] = None
    # Small avatar
    avatar_small: Optional[str] = None
    # Display name
    display_name: Optional[str] = None
    # Specifies if the user has an avatar or not
    has_avatar: Optional[bool] = None
    # ID
    id: Optional[UUID] = None
    # Specifies if the user is an anonim or not
    is_anonim: Optional[bool] = None
    # Profile URL
    profile_url: Optional[str] = None
    # Title
    title: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EmployeeDto:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EmployeeDto
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EmployeeDto()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "avatar": lambda n : setattr(self, 'avatar', n.get_str_value()),
            "avatarMax": lambda n : setattr(self, 'avatar_max', n.get_str_value()),
            "avatarMedium": lambda n : setattr(self, 'avatar_medium', n.get_str_value()),
            "avatarOriginal": lambda n : setattr(self, 'avatar_original', n.get_str_value()),
            "avatarSmall": lambda n : setattr(self, 'avatar_small', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "hasAvatar": lambda n : setattr(self, 'has_avatar', n.get_bool_value()),
            "id": lambda n : setattr(self, 'id', n.get_uuid_value()),
            "isAnonim": lambda n : setattr(self, 'is_anonim', n.get_bool_value()),
            "profileUrl": lambda n : setattr(self, 'profile_url', n.get_str_value()),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
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
        writer.write_str_value("avatar", self.avatar)
        writer.write_str_value("avatarMax", self.avatar_max)
        writer.write_str_value("avatarMedium", self.avatar_medium)
        writer.write_str_value("avatarOriginal", self.avatar_original)
        writer.write_str_value("avatarSmall", self.avatar_small)
        writer.write_str_value("displayName", self.display_name)
        writer.write_bool_value("hasAvatar", self.has_avatar)
        writer.write_uuid_value("id", self.id)
        writer.write_bool_value("isAnonim", self.is_anonim)
        writer.write_str_value("profileUrl", self.profile_url)
        writer.write_str_value("title", self.title)
    

