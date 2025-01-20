from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class TenantDomainValidator(Parsable):
    # Max length
    max_length: Optional[int] = None
    # Min length
    min_length: Optional[int] = None
    # Regex
    regex: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TenantDomainValidator:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TenantDomainValidator
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TenantDomainValidator()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "maxLength": lambda n : setattr(self, 'max_length', n.get_int_value()),
            "minLength": lambda n : setattr(self, 'min_length', n.get_int_value()),
            "regex": lambda n : setattr(self, 'regex', n.get_str_value()),
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
    

