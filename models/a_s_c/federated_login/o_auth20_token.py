from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class OAuth20Token(Parsable):
    # The access_token property
    access_token: Optional[str] = None
    # The client_id property
    client_id: Optional[str] = None
    # The client_secret property
    client_secret: Optional[str] = None
    # The expires_in property
    expires_in: Optional[int] = None
    # The isExpired property
    is_expired: Optional[bool] = None
    # The redirect_uri property
    redirect_uri: Optional[str] = None
    # The refresh_token property
    refresh_token: Optional[str] = None
    # The timestamp property
    timestamp: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OAuth20Token:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OAuth20Token
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OAuth20Token()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "access_token": lambda n : setattr(self, 'access_token', n.get_str_value()),
            "client_id": lambda n : setattr(self, 'client_id', n.get_str_value()),
            "client_secret": lambda n : setattr(self, 'client_secret', n.get_str_value()),
            "expires_in": lambda n : setattr(self, 'expires_in', n.get_int_value()),
            "isExpired": lambda n : setattr(self, 'is_expired', n.get_bool_value()),
            "redirect_uri": lambda n : setattr(self, 'redirect_uri', n.get_str_value()),
            "refresh_token": lambda n : setattr(self, 'refresh_token', n.get_str_value()),
            "timestamp": lambda n : setattr(self, 'timestamp', n.get_datetime_value()),
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
        writer.write_str_value("access_token", self.access_token)
        writer.write_str_value("client_id", self.client_id)
        writer.write_str_value("client_secret", self.client_secret)
        writer.write_int_value("expires_in", self.expires_in)
        writer.write_str_value("redirect_uri", self.redirect_uri)
        writer.write_str_value("refresh_token", self.refresh_token)
        writer.write_datetime_value("timestamp", self.timestamp)
    

