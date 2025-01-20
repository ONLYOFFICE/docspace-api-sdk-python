from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class CoEditingConfig(Parsable):
    # Change
    change: Optional[bool] = None
    # Fast
    fast: Optional[bool] = None
    # The mode property
    mode: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CoEditingConfig:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CoEditingConfig
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CoEditingConfig()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "change": lambda n : setattr(self, 'change', n.get_bool_value()),
            "fast": lambda n : setattr(self, 'fast', n.get_bool_value()),
            "mode": lambda n : setattr(self, 'mode', n.get_int_value()),
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
        writer.write_bool_value("change", self.change)
        writer.write_bool_value("fast", self.fast)
        writer.write_int_value("mode", self.mode)
    

