from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class Boolean(Parsable):
    # The key property
    key: Optional[str] = None
    # The value property
    value: Optional[Boolean] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Boolean:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Boolean
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Boolean()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "key": lambda n : setattr(self, 'key', n.get_str_value()),
            "value": lambda n : setattr(self, 'value', n.get_object_value(Boolean)),
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
        writer.write_str_value("key", self.key)
        writer.write_bool_value("value", self.value)
    

