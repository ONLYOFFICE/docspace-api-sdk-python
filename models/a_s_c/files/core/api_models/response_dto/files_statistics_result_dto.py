from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .files_statistics_folder import FilesStatisticsFolder

@dataclass
class FilesStatisticsResultDto(Parsable):
    # The archiveUsedSpace property
    archive_used_space: Optional[FilesStatisticsFolder] = None
    # The myDocumentsUsedSpace property
    my_documents_used_space: Optional[FilesStatisticsFolder] = None
    # The roomsUsedSpace property
    rooms_used_space: Optional[FilesStatisticsFolder] = None
    # The trashUsedSpace property
    trash_used_space: Optional[FilesStatisticsFolder] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> FilesStatisticsResultDto:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FilesStatisticsResultDto
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return FilesStatisticsResultDto()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .files_statistics_folder import FilesStatisticsFolder

        from .files_statistics_folder import FilesStatisticsFolder

        fields: Dict[str, Callable[[Any], None]] = {
            "archiveUsedSpace": lambda n : setattr(self, 'archive_used_space', n.get_object_value(FilesStatisticsFolder)),
            "myDocumentsUsedSpace": lambda n : setattr(self, 'my_documents_used_space', n.get_object_value(FilesStatisticsFolder)),
            "roomsUsedSpace": lambda n : setattr(self, 'rooms_used_space', n.get_object_value(FilesStatisticsFolder)),
            "trashUsedSpace": lambda n : setattr(self, 'trash_used_space', n.get_object_value(FilesStatisticsFolder)),
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
        from .files_statistics_folder import FilesStatisticsFolder

        writer.write_object_value("archiveUsedSpace", self.archive_used_space)
        writer.write_object_value("myDocumentsUsedSpace", self.my_documents_used_space)
        writer.write_object_value("roomsUsedSpace", self.rooms_used_space)
        writer.write_object_value("trashUsedSpace", self.trash_used_space)
    

