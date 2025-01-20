from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class AutoCleanUpData(Parsable):
    # [1 - One week, 2 - Two weeks, 3 - One month, 4 - Thirty days, 5 - Two months, 6 - Three months]
    gap: Optional[int] = None
    # Specifies if the auto-clearing setting is enabled or not
    is_auto_clean_up: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AutoCleanUpData:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AutoCleanUpData
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AutoCleanUpData()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "gap": lambda n : setattr(self, 'gap', n.get_int_value()),
            "isAutoCleanUp": lambda n : setattr(self, 'is_auto_clean_up', n.get_bool_value()),
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
        writer.write_int_value("gap", self.gap)
        writer.write_bool_value("isAutoCleanUp", self.is_auto_clean_up)
    

