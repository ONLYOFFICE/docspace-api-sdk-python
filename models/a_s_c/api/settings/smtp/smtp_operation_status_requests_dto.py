from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class SmtpOperationStatusRequestsDto(Parsable):
    # Specifies if the SMTP operation is completed or not
    completed: Optional[bool] = None
    # SMTP operation error
    error: Optional[str] = None
    # SMTP operation ID
    id: Optional[str] = None
    # Percentage of SMTP operation completion
    percents: Optional[int] = None
    # SMTP operation status
    status: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SmtpOperationStatusRequestsDto:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SmtpOperationStatusRequestsDto
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SmtpOperationStatusRequestsDto()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "completed": lambda n : setattr(self, 'completed', n.get_bool_value()),
            "error": lambda n : setattr(self, 'error', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "percents": lambda n : setattr(self, 'percents', n.get_int_value()),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
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
        writer.write_bool_value("completed", self.completed)
        writer.write_str_value("error", self.error)
        writer.write_str_value("id", self.id)
        writer.write_int_value("percents", self.percents)
        writer.write_str_value("status", self.status)
    

