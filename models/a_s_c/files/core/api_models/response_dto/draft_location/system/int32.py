from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class Int32(Parsable):
    # Draft ID
    file_id: Optional[int] = None
    # Draft title
    file_title: Optional[str] = None
    # InProcess folder ID
    folder_id: Optional[int] = None
    # InProcess folder title
    folder_title: Optional[str] = None
    
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
            "fileId": lambda n : setattr(self, 'file_id', n.get_int_value()),
            "fileTitle": lambda n : setattr(self, 'file_title', n.get_str_value()),
            "folderId": lambda n : setattr(self, 'folder_id', n.get_int_value()),
            "folderTitle": lambda n : setattr(self, 'folder_title', n.get_str_value()),
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
        writer.write_int_value("fileId", self.file_id)
        writer.write_str_value("fileTitle", self.file_title)
        writer.write_int_value("folderId", self.folder_id)
        writer.write_str_value("folderTitle", self.folder_title)
    

