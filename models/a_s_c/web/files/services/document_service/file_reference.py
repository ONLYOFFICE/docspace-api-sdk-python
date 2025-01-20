from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .file_reference_data import FileReferenceData

@dataclass
class FileReference(Parsable):
    # Error
    error: Optional[str] = None
    # File type
    file_type: Optional[str] = None
    # Key
    key: Optional[str] = None
    # Link
    link: Optional[str] = None
    # Path
    path: Optional[str] = None
    # The referenceData property
    reference_data: Optional[FileReferenceData] = None
    # Token
    token: Optional[str] = None
    # URL
    url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> FileReference:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FileReference
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return FileReference()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .file_reference_data import FileReferenceData

        from .file_reference_data import FileReferenceData

        fields: Dict[str, Callable[[Any], None]] = {
            "error": lambda n : setattr(self, 'error', n.get_str_value()),
            "fileType": lambda n : setattr(self, 'file_type', n.get_str_value()),
            "key": lambda n : setattr(self, 'key', n.get_str_value()),
            "link": lambda n : setattr(self, 'link', n.get_str_value()),
            "path": lambda n : setattr(self, 'path', n.get_str_value()),
            "referenceData": lambda n : setattr(self, 'reference_data', n.get_object_value(FileReferenceData)),
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
        from .file_reference_data import FileReferenceData

        writer.write_str_value("error", self.error)
        writer.write_str_value("fileType", self.file_type)
        writer.write_str_value("key", self.key)
        writer.write_str_value("link", self.link)
        writer.write_str_value("path", self.path)
        writer.write_object_value("referenceData", self.reference_data)
        writer.write_str_value("token", self.token)
        writer.write_str_value("url", self.url)
    

