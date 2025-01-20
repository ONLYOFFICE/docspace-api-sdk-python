from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class WatermarkRequestDto(Parsable):
    """
    Request parameters for adding watermarks
    """
    # [1 - User name, 2 - User email, 4 - User ip adress, 8 - Current date, 16 - Room name]
    additions: Optional[int] = None
    # Specifies whether watermarks are on or off
    enabled: Optional[bool] = None
    # Watermark image height
    image_height: Optional[float] = None
    # Watermark image scale
    image_scale: Optional[int] = None
    # The path to the temporary image file
    image_url: Optional[str] = None
    # Watermark image width
    image_width: Optional[float] = None
    # Watermark text and image rotate
    rotate: Optional[int] = None
    # Watermark Text
    text: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WatermarkRequestDto:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WatermarkRequestDto
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WatermarkRequestDto()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "additions": lambda n : setattr(self, 'additions', n.get_int_value()),
            "enabled": lambda n : setattr(self, 'enabled', n.get_bool_value()),
            "imageHeight": lambda n : setattr(self, 'image_height', n.get_float_value()),
            "imageScale": lambda n : setattr(self, 'image_scale', n.get_int_value()),
            "imageUrl": lambda n : setattr(self, 'image_url', n.get_str_value()),
            "imageWidth": lambda n : setattr(self, 'image_width', n.get_float_value()),
            "rotate": lambda n : setattr(self, 'rotate', n.get_int_value()),
            "text": lambda n : setattr(self, 'text', n.get_str_value()),
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
        writer.write_int_value("additions", self.additions)
        writer.write_bool_value("enabled", self.enabled)
        writer.write_float_value("imageHeight", self.image_height)
        writer.write_int_value("imageScale", self.image_scale)
        writer.write_str_value("imageUrl", self.image_url)
        writer.write_float_value("imageWidth", self.image_width)
        writer.write_int_value("rotate", self.rotate)
        writer.write_str_value("text", self.text)
    

