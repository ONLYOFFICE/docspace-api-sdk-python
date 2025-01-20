from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....api.collections.item_key_value_pair.system.string.system.boolean import Boolean

@dataclass
class WebItemsSecurityRequestsDto(Parsable):
    """
    Module request parameters
    """
    # Products with security information
    items: Optional[List[bool]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WebItemsSecurityRequestsDto:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WebItemsSecurityRequestsDto
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WebItemsSecurityRequestsDto()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .....api.collections.item_key_value_pair.system.string.system.boolean import Boolean

        from .....api.collections.item_key_value_pair.system.string.system.boolean import Boolean

        fields: Dict[str, Callable[[Any], None]] = {
            "items": lambda n : setattr(self, 'items', n.get_collection_of_object_values(Bool)),
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
        from .....api.collections.item_key_value_pair.system.string.system.boolean import Boolean

        writer.write_collection_of_object_values("items", self.items)
    

