from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .paragraph import Paragraph

@dataclass
class WatermarkOnDraw(Parsable):
    # The fill property
    fill: Optional[str] = None
    # Defines the watermark height measured in millimeters.
    height: Optional[float] = None
    # The margins property
    margins: Optional[List[int]] = None
    # The paragraphs property
    paragraphs: Optional[List[Paragraph]] = None
    # The rotate property
    rotate: Optional[int] = None
    # The transparent property
    transparent: Optional[float] = None
    # Defines the watermark width measured in millimeters.
    width: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WatermarkOnDraw:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WatermarkOnDraw
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WatermarkOnDraw()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .paragraph import Paragraph

        from .paragraph import Paragraph

        fields: Dict[str, Callable[[Any], None]] = {
            "fill": lambda n : setattr(self, 'fill', n.get_str_value()),
            "height": lambda n : setattr(self, 'height', n.get_float_value()),
            "margins": lambda n : setattr(self, 'margins', n.get_collection_of_primitive_values(int)),
            "paragraphs": lambda n : setattr(self, 'paragraphs', n.get_collection_of_object_values(Paragraph)),
            "rotate": lambda n : setattr(self, 'rotate', n.get_int_value()),
            "transparent": lambda n : setattr(self, 'transparent', n.get_float_value()),
            "width": lambda n : setattr(self, 'width', n.get_float_value()),
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
        from .paragraph import Paragraph

        writer.write_str_value("fill", self.fill)
        writer.write_float_value("height", self.height)
        writer.write_collection_of_primitive_values("margins", self.margins)
        writer.write_collection_of_object_values("paragraphs", self.paragraphs)
        writer.write_int_value("rotate", self.rotate)
        writer.write_float_value("transparent", self.transparent)
        writer.write_float_value("width", self.width)
    

