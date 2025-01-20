from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class ConversationResultDto(Parsable):
    """
    Result of file conversation operation.
    """
    # Error
    error: Optional[str] = None
    # Operation ID
    id: Optional[str] = None
    # [0 - Move, 1 - Copy, 2 - Delete, 3 - Download, 4 - MarkAsRead, 5 - Import, 6 - Convert, 7 - Duplicate]
    operation: Optional[int] = None
    # Specifies if the operation is processed or not
    processed: Optional[str] = None
    # Operation progress
    progress: Optional[int] = None
    # Source file
    source: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ConversationResultDto:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ConversationResultDto
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ConversationResultDto()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "error": lambda n : setattr(self, 'error', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "Operation": lambda n : setattr(self, 'operation', n.get_int_value()),
            "processed": lambda n : setattr(self, 'processed', n.get_str_value()),
            "progress": lambda n : setattr(self, 'progress', n.get_int_value()),
            "source": lambda n : setattr(self, 'source', n.get_str_value()),
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
        writer.write_str_value("error", self.error)
        writer.write_str_value("id", self.id)
        writer.write_int_value("Operation", self.operation)
        writer.write_str_value("processed", self.processed)
        writer.write_int_value("progress", self.progress)
        writer.write_str_value("source", self.source)
    

