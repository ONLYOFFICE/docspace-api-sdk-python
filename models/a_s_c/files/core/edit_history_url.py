from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class EditHistoryUrl(Parsable):
    # File type
    file_type: Optional[str] = None
    # Key
    key: Optional[str] = None
    # Url
    url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EditHistoryUrl:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EditHistoryUrl
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EditHistoryUrl()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "fileType": lambda n : setattr(self, 'file_type', n.get_str_value()),
            "key": lambda n : setattr(self, 'key', n.get_str_value()),
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
        writer.write_str_value("fileType", self.file_type)
        writer.write_str_value("key", self.key)
        writer.write_str_value("url", self.url)
    

