from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ...orders_item_request_dto.system.int32 import Int32

@dataclass
class Int32(Parsable):
    # The items property
    items: Optional[List[Int32]] = None
    
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
        from ...orders_item_request_dto.system.int32 import Int32

        from ...orders_item_request_dto.system.int32 import Int32

        fields: Dict[str, Callable[[Any], None]] = {
            "items": lambda n : setattr(self, 'items', n.get_collection_of_object_values(Int32)),
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
        from ...orders_item_request_dto.system.int32 import Int32

        writer.write_collection_of_object_values("items", self.items)
    

