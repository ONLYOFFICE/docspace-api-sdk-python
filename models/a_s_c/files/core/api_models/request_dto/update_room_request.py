from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..room_data_lifetime_dto import RoomDataLifetimeDto
    from .logo_request import LogoRequest
    from .watermark_request_dto import WatermarkRequestDto

@dataclass
class UpdateRoomRequest(Parsable):
    """
    Parameters for updating a room
    """
    # Color
    color: Optional[str] = None
    # Cover
    cover: Optional[str] = None
    # Room quota
    deny_download: Optional[bool] = None
    # Indexing
    indexing: Optional[bool] = None
    # The lifetime property
    lifetime: Optional[RoomDataLifetimeDto] = None
    # Logo request parameters
    logo: Optional[LogoRequest] = None
    # Room quota
    quota: Optional[int] = None
    # List of tags
    tags: Optional[List[str]] = None
    # Room name
    title: Optional[str] = None
    # Request parameters for adding watermarks
    watermark: Optional[WatermarkRequestDto] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UpdateRoomRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UpdateRoomRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UpdateRoomRequest()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ..room_data_lifetime_dto import RoomDataLifetimeDto
        from .logo_request import LogoRequest
        from .watermark_request_dto import WatermarkRequestDto

        from ..room_data_lifetime_dto import RoomDataLifetimeDto
        from .logo_request import LogoRequest
        from .watermark_request_dto import WatermarkRequestDto

        fields: Dict[str, Callable[[Any], None]] = {
            "color": lambda n : setattr(self, 'color', n.get_str_value()),
            "cover": lambda n : setattr(self, 'cover', n.get_str_value()),
            "denyDownload": lambda n : setattr(self, 'deny_download', n.get_bool_value()),
            "indexing": lambda n : setattr(self, 'indexing', n.get_bool_value()),
            "lifetime": lambda n : setattr(self, 'lifetime', n.get_object_value(RoomDataLifetimeDto)),
            "logo": lambda n : setattr(self, 'logo', n.get_object_value(LogoRequest)),
            "quota": lambda n : setattr(self, 'quota', n.get_int_value()),
            "tags": lambda n : setattr(self, 'tags', n.get_collection_of_primitive_values(str)),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
            "watermark": lambda n : setattr(self, 'watermark', n.get_object_value(WatermarkRequestDto)),
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
        from ..room_data_lifetime_dto import RoomDataLifetimeDto
        from .logo_request import LogoRequest
        from .watermark_request_dto import WatermarkRequestDto

        writer.write_str_value("color", self.color)
        writer.write_str_value("cover", self.cover)
        writer.write_bool_value("denyDownload", self.deny_download)
        writer.write_bool_value("indexing", self.indexing)
        writer.write_object_value("lifetime", self.lifetime)
        writer.write_object_value("logo", self.logo)
        writer.write_int_value("quota", self.quota)
        writer.write_collection_of_primitive_values("tags", self.tags)
        writer.write_str_value("title", self.title)
        writer.write_object_value("watermark", self.watermark)
    

