from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class PasswordHasher(Parsable):
    # The iterations property
    iterations: Optional[int] = None
    # The salt property
    salt: Optional[str] = None
    # The size property
    size: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PasswordHasher:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PasswordHasher
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PasswordHasher()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "iterations": lambda n : setattr(self, 'iterations', n.get_int_value()),
            "salt": lambda n : setattr(self, 'salt', n.get_str_value()),
            "size": lambda n : setattr(self, 'size', n.get_int_value()),
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
    

