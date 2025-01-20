from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class TaskProgressResponseDto(Parsable):
    # Error
    error: Optional[str] = None
    # ID
    id: Optional[str] = None
    # IsCompleted
    is_completed: Optional[bool] = None
    # Percentage
    percentage: Optional[int] = None
    # [0 - Created, 1 - Running, 2 - Completed, 3 - Canceled, 4 - Failted]
    status: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TaskProgressResponseDto:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TaskProgressResponseDto
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TaskProgressResponseDto()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "error": lambda n : setattr(self, 'error', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "isCompleted": lambda n : setattr(self, 'is_completed', n.get_bool_value()),
            "percentage": lambda n : setattr(self, 'percentage', n.get_int_value()),
            "status": lambda n : setattr(self, 'status', n.get_int_value()),
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
        writer.write_bool_value("isCompleted", self.is_completed)
        writer.write_int_value("percentage", self.percentage)
        writer.write_int_value("status", self.status)
    

