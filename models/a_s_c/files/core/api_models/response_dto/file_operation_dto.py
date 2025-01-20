from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .file_entry_dto import FileEntryDto

@dataclass
class FileOperationDto(Parsable):
    # Error
    error: Optional[str] = None
    # List of files
    files: Optional[List[FileEntryDto]] = None
    # Specifies if the operation is finished or not
    finished: Optional[bool] = None
    # List of folders
    folders: Optional[List[FileEntryDto]] = None
    # Operation ID
    id: Optional[str] = None
    # [0 - Move, 1 - Copy, 2 - Delete, 3 - Download, 4 - MarkAsRead, 5 - Import, 6 - Convert, 7 - Duplicate]
    operation: Optional[int] = None
    # Processing status
    processed: Optional[str] = None
    # Operation progress
    progress: Optional[int] = None
    # URL
    url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> FileOperationDto:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FileOperationDto
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return FileOperationDto()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .file_entry_dto import FileEntryDto

        from .file_entry_dto import FileEntryDto

        fields: Dict[str, Callable[[Any], None]] = {
            "error": lambda n : setattr(self, 'error', n.get_str_value()),
            "files": lambda n : setattr(self, 'files', n.get_collection_of_object_values(FileEntryDto)),
            "finished": lambda n : setattr(self, 'finished', n.get_bool_value()),
            "folders": lambda n : setattr(self, 'folders', n.get_collection_of_object_values(FileEntryDto)),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "Operation": lambda n : setattr(self, 'operation', n.get_int_value()),
            "processed": lambda n : setattr(self, 'processed', n.get_str_value()),
            "progress": lambda n : setattr(self, 'progress', n.get_int_value()),
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
        from .file_entry_dto import FileEntryDto

        writer.write_str_value("error", self.error)
        writer.write_collection_of_object_values("files", self.files)
        writer.write_bool_value("finished", self.finished)
        writer.write_collection_of_object_values("folders", self.folders)
        writer.write_str_value("id", self.id)
        writer.write_int_value("Operation", self.operation)
        writer.write_str_value("processed", self.processed)
        writer.write_int_value("progress", self.progress)
        writer.write_str_value("url", self.url)
    

