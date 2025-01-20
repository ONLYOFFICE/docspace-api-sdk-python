from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ...file_entry_dto import FileEntryDto
    from ...folder_dto.system.int32 import Int32

@dataclass
class Int32(Parsable):
    # Number of folder elements
    count: Optional[int] = None
    # The current property
    current: Optional[Int32] = None
    # List of files
    files: Optional[List[FileEntryDto]] = None
    # List of folders
    folders: Optional[List[FileEntryDto]] = None
    # New element index
    new: Optional[int] = None
    # Folder start index
    start_index: Optional[int] = None
    # Total number of elements in the folder
    total: Optional[int] = None
    
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
        from ...file_entry_dto import FileEntryDto
        from ...folder_dto.system.int32 import Int32

        from ...file_entry_dto import FileEntryDto
        from ...folder_dto.system.int32 import Int32

        fields: Dict[str, Callable[[Any], None]] = {
            "count": lambda n : setattr(self, 'count', n.get_int_value()),
            "current": lambda n : setattr(self, 'current', n.get_object_value(Int32)),
            "files": lambda n : setattr(self, 'files', n.get_collection_of_object_values(FileEntryDto)),
            "folders": lambda n : setattr(self, 'folders', n.get_collection_of_object_values(FileEntryDto)),
            "new": lambda n : setattr(self, 'new', n.get_int_value()),
            "startIndex": lambda n : setattr(self, 'start_index', n.get_int_value()),
            "total": lambda n : setattr(self, 'total', n.get_int_value()),
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
        from ...file_entry_dto import FileEntryDto
        from ...folder_dto.system.int32 import Int32

        writer.write_int_value("count", self.count)
        writer.write_int_value("current", self.current)
        writer.write_collection_of_object_values("files", self.files)
        writer.write_collection_of_object_values("folders", self.folders)
        writer.write_int_value("new", self.new)
        writer.write_int_value("startIndex", self.start_index)
        writer.write_int_value("total", self.total)
    

