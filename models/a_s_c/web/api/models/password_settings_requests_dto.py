from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class PasswordSettingsRequestsDto(Parsable):
    """
    Password settings
    """
    # Specifies if the password must include the digits or not
    digits: Optional[bool] = None
    # Minimum password length
    min_length: Optional[int] = None
    # Specifies if the password must include the special symbols or not
    spec_symbols: Optional[bool] = None
    # Specifies if the password must include the uppercase letters or not
    upper_case: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PasswordSettingsRequestsDto:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PasswordSettingsRequestsDto
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PasswordSettingsRequestsDto()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "digits": lambda n : setattr(self, 'digits', n.get_bool_value()),
            "minLength": lambda n : setattr(self, 'min_length', n.get_int_value()),
            "specSymbols": lambda n : setattr(self, 'spec_symbols', n.get_bool_value()),
            "upperCase": lambda n : setattr(self, 'upper_case', n.get_bool_value()),
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
        writer.write_bool_value("digits", self.digits)
        writer.write_int_value("minLength", self.min_length)
        writer.write_bool_value("specSymbols", self.spec_symbols)
        writer.write_bool_value("upperCase", self.upper_case)
    

