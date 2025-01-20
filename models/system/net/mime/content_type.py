from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class ContentType(Parsable):
    # The boundary property
    boundary: Optional[str] = None
    # The charSet property
    char_set: Optional[str] = None
    # The mediaType property
    media_type: Optional[str] = None
    # The name property
    name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ContentType:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ContentType
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ContentType()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "boundary": lambda n : setattr(self, 'boundary', n.get_str_value()),
            "charSet": lambda n : setattr(self, 'char_set', n.get_str_value()),
            "mediaType": lambda n : setattr(self, 'media_type', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
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
        writer.write_str_value("boundary", self.boundary)
        writer.write_str_value("charSet", self.char_set)
        writer.write_str_value("mediaType", self.media_type)
        writer.write_str_value("name", self.name)
    

