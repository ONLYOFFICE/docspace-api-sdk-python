from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .watermark_on_draw import WatermarkOnDraw

@dataclass
class Options(Parsable):
    # The watermark_on_draw property
    watermark_on_draw: Optional[WatermarkOnDraw] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Options:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Options
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Options()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .watermark_on_draw import WatermarkOnDraw

        from .watermark_on_draw import WatermarkOnDraw

        fields: Dict[str, Callable[[Any], None]] = {
            "watermark_on_draw": lambda n : setattr(self, 'watermark_on_draw', n.get_object_value(WatermarkOnDraw)),
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
        from .watermark_on_draw import WatermarkOnDraw

        writer.write_object_value("watermark_on_draw", self.watermark_on_draw)
    

