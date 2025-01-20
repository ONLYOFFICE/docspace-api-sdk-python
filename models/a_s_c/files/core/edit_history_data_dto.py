from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .edit_history_url import EditHistoryUrl

@dataclass
class EditHistoryDataDto(Parsable):
    # URL to the file changes
    changes_url: Optional[str] = None
    # File type
    file_type: Optional[str] = None
    # Key
    key: Optional[str] = None
    # The previous property
    previous: Optional[EditHistoryUrl] = None
    # Token
    token: Optional[str] = None
    # File URL
    url: Optional[str] = None
    # File version
    version: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EditHistoryDataDto:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EditHistoryDataDto
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EditHistoryDataDto()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .edit_history_url import EditHistoryUrl

        from .edit_history_url import EditHistoryUrl

        fields: Dict[str, Callable[[Any], None]] = {
            "changesUrl": lambda n : setattr(self, 'changes_url', n.get_str_value()),
            "fileType": lambda n : setattr(self, 'file_type', n.get_str_value()),
            "key": lambda n : setattr(self, 'key', n.get_str_value()),
            "previous": lambda n : setattr(self, 'previous', n.get_object_value(EditHistoryUrl)),
            "token": lambda n : setattr(self, 'token', n.get_str_value()),
            "url": lambda n : setattr(self, 'url', n.get_str_value()),
            "version": lambda n : setattr(self, 'version', n.get_int_value()),
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
        from .edit_history_url import EditHistoryUrl

        writer.write_str_value("changesUrl", self.changes_url)
        writer.write_str_value("fileType", self.file_type)
        writer.write_str_value("key", self.key)
        writer.write_object_value("previous", self.previous)
        writer.write_str_value("token", self.token)
        writer.write_str_value("url", self.url)
        writer.write_int_value("version", self.version)
    

