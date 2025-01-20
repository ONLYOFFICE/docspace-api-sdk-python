from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class CheckFillFormDraft(Parsable):
    """
    Parameters for checking a form draft
    """
    # Action with a form
    action: Optional[str] = None
    # Specifies whether to request an embedded form or not
    request_embedded: Optional[bool] = None
    # Specifies whether to request a form for viewing or not
    request_view: Optional[bool] = None
    # File version
    version: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CheckFillFormDraft:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CheckFillFormDraft
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CheckFillFormDraft()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "action": lambda n : setattr(self, 'action', n.get_str_value()),
            "requestEmbedded": lambda n : setattr(self, 'request_embedded', n.get_bool_value()),
            "requestView": lambda n : setattr(self, 'request_view', n.get_bool_value()),
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
        writer.write_str_value("action", self.action)
        writer.write_int_value("version", self.version)
    

