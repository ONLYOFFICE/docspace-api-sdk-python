from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class BatchTagsRequestDto(Parsable):
    """
    Request parameters for adding tags
    """
    # Tag names
    names: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BatchTagsRequestDto:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BatchTagsRequestDto
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return BatchTagsRequestDto()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "names": lambda n : setattr(self, 'names', n.get_collection_of_primitive_values(str)),
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
        writer.write_collection_of_primitive_values("names", self.names)
    

