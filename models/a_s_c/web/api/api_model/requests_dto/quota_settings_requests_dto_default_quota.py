from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import ComposedTypeWrapper, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class QuotaSettingsRequestsDto_defaultQuota(ComposedTypeWrapper, Parsable):
    """
    Composed type wrapper for classes int, str
    """
    # Composed type representation for type int
    integer: Optional[int] = None
    # Composed type representation for type str
    string: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> QuotaSettingsRequestsDto_defaultQuota:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: QuotaSettingsRequestsDto_defaultQuota
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        result = QuotaSettingsRequestsDto_defaultQuota()
        if integer_value := parse_node.get_int_value():
            result.integer = integer_value
        elif string_value := parse_node.get_str_value():
            result.string = string_value
        return result
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        return {}
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        if self.integer:
            writer.write_int_value(None, self.integer)
        elif self.string:
            writer.write_str_value(None, self.string)
    

