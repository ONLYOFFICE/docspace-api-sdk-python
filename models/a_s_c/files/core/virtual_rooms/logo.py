from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .logo_cover import LogoCover

@dataclass
class Logo(Parsable):
    # Color
    color: Optional[str] = None
    # The cover property
    cover: Optional[LogoCover] = None
    # Large
    large: Optional[str] = None
    # Medium
    medium: Optional[str] = None
    # Original
    original: Optional[str] = None
    # Small
    small: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Logo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Logo
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Logo()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .logo_cover import LogoCover

        from .logo_cover import LogoCover

        fields: Dict[str, Callable[[Any], None]] = {
            "color": lambda n : setattr(self, 'color', n.get_str_value()),
            "cover": lambda n : setattr(self, 'cover', n.get_object_value(LogoCover)),
            "large": lambda n : setattr(self, 'large', n.get_str_value()),
            "medium": lambda n : setattr(self, 'medium', n.get_str_value()),
            "original": lambda n : setattr(self, 'original', n.get_str_value()),
            "small": lambda n : setattr(self, 'small', n.get_str_value()),
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
        from .logo_cover import LogoCover

        writer.write_str_value("color", self.color)
        writer.write_object_value("cover", self.cover)
        writer.write_str_value("large", self.large)
        writer.write_str_value("medium", self.medium)
        writer.write_str_value("original", self.original)
        writer.write_str_value("small", self.small)
    

