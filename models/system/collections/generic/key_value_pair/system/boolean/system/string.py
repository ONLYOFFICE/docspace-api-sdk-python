from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class String(Parsable):
    # The key property
    key: Optional[bool] = None
    # The value property
    value: Optional[String] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> String:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: String
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return String()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "key": lambda n : setattr(self, 'key', n.get_bool_value()),
            "value": lambda n : setattr(self, 'value', n.get_object_value(String)),
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
        writer.write_bool_value("key", self.key)
        writer.write_str_value("value", self.value)
    

