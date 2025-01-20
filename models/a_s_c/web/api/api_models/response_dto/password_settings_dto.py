from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class PasswordSettingsDto(Parsable):
    # Allowed characters regex str
    allowed_characters_regex_str: Optional[str] = None
    # Digits
    digits: Optional[bool] = None
    # Digits regex str
    digits_regex_str: Optional[str] = None
    # Min length
    min_length: Optional[int] = None
    # Spec symbols
    spec_symbols: Optional[bool] = None
    # Spec symbols regex str
    spec_symbols_regex_str: Optional[str] = None
    # Upper case
    upper_case: Optional[bool] = None
    # Upper case regex str
    upper_case_regex_str: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PasswordSettingsDto:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PasswordSettingsDto
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PasswordSettingsDto()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "allowedCharactersRegexStr": lambda n : setattr(self, 'allowed_characters_regex_str', n.get_str_value()),
            "digits": lambda n : setattr(self, 'digits', n.get_bool_value()),
            "digitsRegexStr": lambda n : setattr(self, 'digits_regex_str', n.get_str_value()),
            "minLength": lambda n : setattr(self, 'min_length', n.get_int_value()),
            "specSymbols": lambda n : setattr(self, 'spec_symbols', n.get_bool_value()),
            "specSymbolsRegexStr": lambda n : setattr(self, 'spec_symbols_regex_str', n.get_str_value()),
            "upperCase": lambda n : setattr(self, 'upper_case', n.get_bool_value()),
            "upperCaseRegexStr": lambda n : setattr(self, 'upper_case_regex_str', n.get_str_value()),
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
        writer.write_str_value("allowedCharactersRegexStr", self.allowed_characters_regex_str)
        writer.write_bool_value("digits", self.digits)
        writer.write_str_value("digitsRegexStr", self.digits_regex_str)
        writer.write_int_value("minLength", self.min_length)
        writer.write_bool_value("specSymbols", self.spec_symbols)
        writer.write_str_value("specSymbolsRegexStr", self.spec_symbols_regex_str)
        writer.write_bool_value("upperCase", self.upper_case)
        writer.write_str_value("upperCaseRegexStr", self.upper_case_regex_str)
    

