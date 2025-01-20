from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class AccountInfoDto(Parsable):
    # Class
    class_: Optional[str] = None
    # Specifies if an account is linked or not
    linked: Optional[bool] = None
    # Provider
    provider: Optional[str] = None
    # URL
    url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AccountInfoDto:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AccountInfoDto
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AccountInfoDto()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "class": lambda n : setattr(self, 'class_', n.get_str_value()),
            "linked": lambda n : setattr(self, 'linked', n.get_bool_value()),
            "provider": lambda n : setattr(self, 'provider', n.get_str_value()),
            "url": lambda n : setattr(self, 'url', n.get_str_value()),
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
        writer.write_str_value("class", self.class_)
        writer.write_bool_value("linked", self.linked)
        writer.write_str_value("provider", self.provider)
        writer.write_str_value("url", self.url)
    

