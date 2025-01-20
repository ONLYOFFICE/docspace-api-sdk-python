from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .logo_request import LogoRequest

@dataclass
class CreateThirdPartyRoom(Parsable):
    """
    Parameters for creating a room
    """
    # Color
    color: Optional[str] = None
    # Cover
    cover: Optional[str] = None
    # Create as new folder
    create_as_new_folder: Optional[bool] = None
    # Deny download
    deny_download: Optional[bool] = None
    # Indexing
    indexing: Optional[bool] = None
    # Logo request parameters
    logo: Optional[LogoRequest] = None
    # Private
    private: Optional[bool] = None
    # [1 - Form filling room, 2 - Collaboration room, 5 - Custom room, 6 - Public room, 8 - Virtual data room]
    room_type: Optional[int] = None
    # Tags
    tags: Optional[List[str]] = None
    # Room name
    title: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CreateThirdPartyRoom:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CreateThirdPartyRoom
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CreateThirdPartyRoom()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .logo_request import LogoRequest

        from .logo_request import LogoRequest

        fields: Dict[str, Callable[[Any], None]] = {
            "color": lambda n : setattr(self, 'color', n.get_str_value()),
            "cover": lambda n : setattr(self, 'cover', n.get_str_value()),
            "createAsNewFolder": lambda n : setattr(self, 'create_as_new_folder', n.get_bool_value()),
            "denyDownload": lambda n : setattr(self, 'deny_download', n.get_bool_value()),
            "indexing": lambda n : setattr(self, 'indexing', n.get_bool_value()),
            "logo": lambda n : setattr(self, 'logo', n.get_object_value(LogoRequest)),
            "private": lambda n : setattr(self, 'private', n.get_bool_value()),
            "roomType": lambda n : setattr(self, 'room_type', n.get_int_value()),
            "tags": lambda n : setattr(self, 'tags', n.get_collection_of_primitive_values(str)),
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
        from .logo_request import LogoRequest

        writer.write_str_value("color", self.color)
        writer.write_str_value("cover", self.cover)
        writer.write_bool_value("createAsNewFolder", self.create_as_new_folder)
        writer.write_bool_value("denyDownload", self.deny_download)
        writer.write_bool_value("indexing", self.indexing)
        writer.write_object_value("logo", self.logo)
        writer.write_bool_value("private", self.private)
        writer.write_int_value("roomType", self.room_type)
        writer.write_collection_of_primitive_values("tags", self.tags)
        writer.write_str_value("title", self.title)
    

