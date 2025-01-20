from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class ThumbnailsDataDto(Parsable):
    # Big
    big: Optional[str] = None
    # Maximum size
    max: Optional[str] = None
    # Medium
    medium: Optional[str] = None
    # Original photo
    original: Optional[str] = None
    # Retina
    retina: Optional[str] = None
    # Small
    small: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ThumbnailsDataDto:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ThumbnailsDataDto
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ThumbnailsDataDto()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "big": lambda n : setattr(self, 'big', n.get_str_value()),
            "max": lambda n : setattr(self, 'max', n.get_str_value()),
            "medium": lambda n : setattr(self, 'medium', n.get_str_value()),
            "original": lambda n : setattr(self, 'original', n.get_str_value()),
            "retina": lambda n : setattr(self, 'retina', n.get_str_value()),
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
        writer.write_str_value("big", self.big)
        writer.write_str_value("max", self.max)
        writer.write_str_value("medium", self.medium)
        writer.write_str_value("original", self.original)
        writer.write_str_value("retina", self.retina)
        writer.write_str_value("small", self.small)
    

