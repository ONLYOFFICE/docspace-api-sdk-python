from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ...federated_login.o_auth20_token import OAuth20Token

@dataclass
class AuthData(Parsable):
    # Login
    login: Optional[str] = None
    # Password
    password: Optional[str] = None
    # Provider
    provider: Optional[str] = None
    # Raw token
    raw_token: Optional[str] = None
    # The token property
    token: Optional[OAuth20Token] = None
    # Url
    url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AuthData:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AuthData
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AuthData()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ...federated_login.o_auth20_token import OAuth20Token

        from ...federated_login.o_auth20_token import OAuth20Token

        fields: Dict[str, Callable[[Any], None]] = {
            "login": lambda n : setattr(self, 'login', n.get_str_value()),
            "password": lambda n : setattr(self, 'password', n.get_str_value()),
            "provider": lambda n : setattr(self, 'provider', n.get_str_value()),
            "rawToken": lambda n : setattr(self, 'raw_token', n.get_str_value()),
            "token": lambda n : setattr(self, 'token', n.get_object_value(OAuth20Token)),
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
        from ...federated_login.o_auth20_token import OAuth20Token

        writer.write_str_value("login", self.login)
        writer.write_str_value("password", self.password)
        writer.write_str_value("provider", self.provider)
        writer.write_str_value("rawToken", self.raw_token)
        writer.write_object_value("token", self.token)
        writer.write_str_value("url", self.url)
    

