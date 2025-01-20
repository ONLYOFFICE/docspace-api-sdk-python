from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class ThirdPartyBackupRequestDto(Parsable):
    """
    Third-party backup request parameters
    """
    # Customer title
    customer_title: Optional[str] = None
    # Login
    login: Optional[str] = None
    # Password
    password: Optional[str] = None
    # Provider key
    provider_key: Optional[str] = None
    # Authentication token
    token: Optional[str] = None
    # Connection URL for the sharepoint
    url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ThirdPartyBackupRequestDto:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ThirdPartyBackupRequestDto
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ThirdPartyBackupRequestDto()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "customerTitle": lambda n : setattr(self, 'customer_title', n.get_str_value()),
            "login": lambda n : setattr(self, 'login', n.get_str_value()),
            "password": lambda n : setattr(self, 'password', n.get_str_value()),
            "providerKey": lambda n : setattr(self, 'provider_key', n.get_str_value()),
            "token": lambda n : setattr(self, 'token', n.get_str_value()),
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
        writer.write_str_value("customerTitle", self.customer_title)
        writer.write_str_value("login", self.login)
        writer.write_str_value("password", self.password)
        writer.write_str_value("providerKey", self.provider_key)
        writer.write_str_value("token", self.token)
        writer.write_str_value("url", self.url)
    

