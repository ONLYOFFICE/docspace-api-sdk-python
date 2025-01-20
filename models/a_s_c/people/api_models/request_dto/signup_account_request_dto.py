from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class SignupAccountRequestDto(Parsable):
    """
    Request parameters for creating a third-party account
    """
    # Culture
    culture: Optional[str] = None
    # Email address
    email: Optional[str] = None
    # [0 - All, 1 - Room admin, 2 - Guest, 3 - DocSpace admin, 4 - User]
    employee_type: Optional[int] = None
    # First name
    first_name: Optional[str] = None
    # Link key
    key: Optional[str] = None
    # Last name
    last_name: Optional[str] = None
    # Password hash
    password_hash: Optional[str] = None
    # Third-party profile in the serialized format
    serialized_profile: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SignupAccountRequestDto:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SignupAccountRequestDto
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SignupAccountRequestDto()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "culture": lambda n : setattr(self, 'culture', n.get_str_value()),
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "employeeType": lambda n : setattr(self, 'employee_type', n.get_int_value()),
            "firstName": lambda n : setattr(self, 'first_name', n.get_str_value()),
            "key": lambda n : setattr(self, 'key', n.get_str_value()),
            "lastName": lambda n : setattr(self, 'last_name', n.get_str_value()),
            "passwordHash": lambda n : setattr(self, 'password_hash', n.get_str_value()),
            "serializedProfile": lambda n : setattr(self, 'serialized_profile', n.get_str_value()),
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
        writer.write_str_value("culture", self.culture)
        writer.write_str_value("email", self.email)
        writer.write_int_value("employeeType", self.employee_type)
        writer.write_str_value("firstName", self.first_name)
        writer.write_str_value("key", self.key)
        writer.write_str_value("lastName", self.last_name)
        writer.write_str_value("passwordHash", self.password_hash)
        writer.write_str_value("serializedProfile", self.serialized_profile)
    

