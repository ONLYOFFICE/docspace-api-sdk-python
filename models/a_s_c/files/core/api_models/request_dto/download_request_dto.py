from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .download_request_item_dto import DownloadRequestItemDto

@dataclass
class DownloadRequestDto(Parsable):
    """
    Request parameters for downloading files
    """
    # List of file IDs which will be converted
    file_convert_ids: Optional[List[DownloadRequestItemDto]] = None
    # List of file IDs
    file_ids: Optional[List[int]] = None
    # List of folder IDs
    folder_ids: Optional[List[int]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DownloadRequestDto:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DownloadRequestDto
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DownloadRequestDto()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .download_request_item_dto import DownloadRequestItemDto

        from .download_request_item_dto import DownloadRequestItemDto

        fields: Dict[str, Callable[[Any], None]] = {
            "fileConvertIds": lambda n : setattr(self, 'file_convert_ids', n.get_collection_of_object_values(DownloadRequestItemDto)),
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
        from .download_request_item_dto import DownloadRequestItemDto

        writer.write_collection_of_object_values("fileConvertIds", self.file_convert_ids)
        writer.write_collection_of_primitive_values("fileIds", self.file_ids)
        writer.write_collection_of_primitive_values("folderIds", self.folder_ids)
    

