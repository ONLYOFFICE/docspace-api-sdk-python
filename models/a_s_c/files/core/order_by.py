from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class OrderBy(Parsable):
    # Is asc
    is_asc: Optional[bool] = None
    # [0 - Date and time, 1 - AZ, 2 - Size, 3 - Author, 4 - Type, 5 - New, 6 - Date and time creation, 7 - Room type, 8 - Tags, 9 - Room, 10 - Custom order, 11 - Last opened, 12 - Used space]
    property_: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OrderBy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OrderBy
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OrderBy()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "is_asc": lambda n : setattr(self, 'is_asc', n.get_bool_value()),
            "property": lambda n : setattr(self, 'property_', n.get_int_value()),
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
        writer.write_bool_value("is_asc", self.is_asc)
        writer.write_int_value("property", self.property_)
    

