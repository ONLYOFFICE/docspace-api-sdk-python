from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class ConfirmDto(Parsable):
    # [0 - Ok, 1 - Invalid, 2 - Expired, 3 - Tariff limit, 4 - User existed, 5 - User excluded, 6 - Quota failed]
    result: Optional[int] = None
    # Room id
    room_id: Optional[str] = None
    # Title
    title: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ConfirmDto:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ConfirmDto
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ConfirmDto()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "result": lambda n : setattr(self, 'result', n.get_int_value()),
            "roomId": lambda n : setattr(self, 'room_id', n.get_str_value()),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
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
        writer.write_int_value("result", self.result)
        writer.write_str_value("roomId", self.room_id)
        writer.write_str_value("title", self.title)
    

