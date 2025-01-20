from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class LogoRequest(Parsable):
    """
    Logo request parameters
    """
    # The rectangle height
    height: Optional[int] = None
    # The path to the temporary image file
    tmp_file: Optional[str] = None
    # The rectangle width
    width: Optional[int] = None
    # The X coordinate of the rectangle starting point
    x: Optional[int] = None
    # The Y coordinate of the rectangle starting point
    y: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LogoRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LogoRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LogoRequest()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "height": lambda n : setattr(self, 'height', n.get_int_value()),
            "tmpFile": lambda n : setattr(self, 'tmp_file', n.get_str_value()),
            "width": lambda n : setattr(self, 'width', n.get_int_value()),
            "x": lambda n : setattr(self, 'x', n.get_int_value()),
            "y": lambda n : setattr(self, 'y', n.get_int_value()),
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
        writer.write_int_value("height", self.height)
        writer.write_str_value("tmpFile", self.tmp_file)
        writer.write_int_value("width", self.width)
        writer.write_int_value("x", self.x)
        writer.write_int_value("y", self.y)
    

