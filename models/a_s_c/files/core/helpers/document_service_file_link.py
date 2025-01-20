from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class DocumentService_FileLink(Parsable):
    # File type
    filetype: Optional[str] = None
    # Token
    token: Optional[str] = None
    # Url
    url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DocumentService_FileLink:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DocumentService_FileLink
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DocumentService_FileLink()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "filetype": lambda n : setattr(self, 'filetype', n.get_str_value()),
            "token": lambda n : setattr(self, 'token', n.get_str_value()),
            "url": lambda n : setattr(self, 'url', n.get_str_value()),
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
        writer.write_str_value("filetype", self.filetype)
        writer.write_str_value("token", self.token)
        writer.write_str_value("url", self.url)
    

