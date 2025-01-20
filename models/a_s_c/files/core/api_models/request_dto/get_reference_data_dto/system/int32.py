from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class Int32(Parsable):
    """
    Request parameters for getting reference data
    """
    # The unique document identifier used by the service to get a link to the file
    file_key: Optional[int] = None
    # The unique system identifier
    instance_id: Optional[str] = None
    # Link to file
    link: Optional[str] = None
    # The file name or relative path for the formula editor
    path: Optional[str] = None
    # Source file ID
    source_file_id: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Int32:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Int32
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Int32()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "fileKey": lambda n : setattr(self, 'file_key', n.get_int_value()),
            "instanceId": lambda n : setattr(self, 'instance_id', n.get_str_value()),
            "link": lambda n : setattr(self, 'link', n.get_str_value()),
            "path": lambda n : setattr(self, 'path', n.get_str_value()),
            "sourceFileId": lambda n : setattr(self, 'source_file_id', n.get_int_value()),
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
        writer.write_int_value("fileKey", self.file_key)
        writer.write_str_value("instanceId", self.instance_id)
        writer.write_str_value("link", self.link)
        writer.write_str_value("path", self.path)
        writer.write_int_value("sourceFileId", self.source_file_id)
    

