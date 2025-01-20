from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class ChangeHistory(Parsable):
    """
    Parameters for changing version history
    """
    # Marks as a version or revision
    continue_version: Optional[bool] = None
    # File version
    version: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ChangeHistory:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ChangeHistory
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ChangeHistory()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "continueVersion": lambda n : setattr(self, 'continue_version', n.get_bool_value()),
            "version": lambda n : setattr(self, 'version', n.get_int_value()),
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
        writer.write_bool_value("continueVersion", self.continue_version)
        writer.write_int_value("version", self.version)
    

