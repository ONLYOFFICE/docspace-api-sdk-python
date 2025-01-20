from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .batch_request_dto_dest_folder_id import BatchRequestDto_destFolderId

@dataclass
class BatchRequestDto(Parsable):
    """
    Request parameters for copying/moving files
    """
    # [0 - Skip, 1 - Overwrite, 2 - Duplicate]
    conflict_resolve_type: Optional[int] = None
    # Content
    content: Optional[bool] = None
    # Specifies whether to delete a folder after the editing session is finished or not
    delete_after: Optional[bool] = None
    # Destination folder ID
    dest_folder_id: Optional[BatchRequestDto_destFolderId] = None
    # List of file IDs
    file_ids: Optional[List[int]] = None
    # List of folder IDs
    folder_ids: Optional[List[int]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BatchRequestDto:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BatchRequestDto
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return BatchRequestDto()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .batch_request_dto_dest_folder_id import BatchRequestDto_destFolderId

        from .batch_request_dto_dest_folder_id import BatchRequestDto_destFolderId

        fields: Dict[str, Callable[[Any], None]] = {
            "conflictResolveType": lambda n : setattr(self, 'conflict_resolve_type', n.get_int_value()),
            "content": lambda n : setattr(self, 'content', n.get_bool_value()),
            "deleteAfter": lambda n : setattr(self, 'delete_after', n.get_bool_value()),
            "destFolderId": lambda n : setattr(self, 'dest_folder_id', n.get_object_value(BatchRequestDto_destFolderId)),
            "fileIds": lambda n : setattr(self, 'file_ids', n.get_collection_of_primitive_values(int)),
            "folderIds": lambda n : setattr(self, 'folder_ids', n.get_collection_of_primitive_values(int)),
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
        from .batch_request_dto_dest_folder_id import BatchRequestDto_destFolderId

        writer.write_int_value("conflictResolveType", self.conflict_resolve_type)
        writer.write_bool_value("content", self.content)
        writer.write_bool_value("deleteAfter", self.delete_after)
        writer.write_object_value("destFolderId", self.dest_folder_id)
        writer.write_collection_of_primitive_values("fileIds", self.file_ids)
        writer.write_collection_of_primitive_values("folderIds", self.folder_ids)
    

