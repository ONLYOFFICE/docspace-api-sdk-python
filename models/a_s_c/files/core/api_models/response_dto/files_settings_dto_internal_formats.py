from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class FilesSettingsDto_internalFormats(Parsable):
    """
    Internal formats
    """
    # The Archive property
    archive: Optional[str] = None
    # The Audio property
    audio: Optional[str] = None
    # The Document property
    document: Optional[str] = None
    # The Image property
    image: Optional[str] = None
    # The Pdf property
    pdf: Optional[str] = None
    # The Presentation property
    presentation: Optional[str] = None
    # The Spreadsheet property
    spreadsheet: Optional[str] = None
    # The Unknown property
    unknown: Optional[str] = None
    # The Video property
    video: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> FilesSettingsDto_internalFormats:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FilesSettingsDto_internalFormats
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return FilesSettingsDto_internalFormats()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "Archive": lambda n : setattr(self, 'archive', n.get_str_value()),
            "Audio": lambda n : setattr(self, 'audio', n.get_str_value()),
            "Document": lambda n : setattr(self, 'document', n.get_str_value()),
            "Image": lambda n : setattr(self, 'image', n.get_str_value()),
            "Pdf": lambda n : setattr(self, 'pdf', n.get_str_value()),
            "Presentation": lambda n : setattr(self, 'presentation', n.get_str_value()),
            "Spreadsheet": lambda n : setattr(self, 'spreadsheet', n.get_str_value()),
            "Unknown": lambda n : setattr(self, 'unknown', n.get_str_value()),
            "Video": lambda n : setattr(self, 'video', n.get_str_value()),
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
        writer.write_str_value("Archive", self.archive)
        writer.write_str_value("Audio", self.audio)
        writer.write_str_value("Document", self.document)
        writer.write_str_value("Image", self.image)
        writer.write_str_value("Pdf", self.pdf)
        writer.write_str_value("Presentation", self.presentation)
        writer.write_str_value("Spreadsheet", self.spreadsheet)
        writer.write_str_value("Unknown", self.unknown)
        writer.write_str_value("Video", self.video)
    

