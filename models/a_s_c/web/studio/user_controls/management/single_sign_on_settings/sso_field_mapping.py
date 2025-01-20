from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class SsoFieldMapping(Parsable):
    # Email
    email: Optional[str] = None
    # First name
    first_name: Optional[str] = None
    # Last name
    last_name: Optional[str] = None
    # Location
    location: Optional[str] = None
    # Phone
    phone: Optional[str] = None
    # Title
    title: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SsoFieldMapping:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SsoFieldMapping
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SsoFieldMapping()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "firstName": lambda n : setattr(self, 'first_name', n.get_str_value()),
            "lastName": lambda n : setattr(self, 'last_name', n.get_str_value()),
            "location": lambda n : setattr(self, 'location', n.get_str_value()),
            "phone": lambda n : setattr(self, 'phone', n.get_str_value()),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
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
        writer.write_str_value("email", self.email)
        writer.write_str_value("firstName", self.first_name)
        writer.write_str_value("lastName", self.last_name)
        writer.write_str_value("location", self.location)
        writer.write_str_value("phone", self.phone)
        writer.write_str_value("title", self.title)
    

