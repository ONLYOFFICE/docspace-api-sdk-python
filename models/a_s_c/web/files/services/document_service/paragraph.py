from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .run import Run

@dataclass
class Paragraph(Parsable):
    # The align property
    align: Optional[int] = None
    # The runs property
    runs: Optional[List[Run]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Paragraph:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Paragraph
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Paragraph()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .run import Run

        from .run import Run

        fields: Dict[str, Callable[[Any], None]] = {
            "align": lambda n : setattr(self, 'align', n.get_int_value()),
            "runs": lambda n : setattr(self, 'runs', n.get_collection_of_object_values(Run)),
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
        from .run import Run

        writer.write_int_value("align", self.align)
        writer.write_collection_of_object_values("runs", self.runs)
    

