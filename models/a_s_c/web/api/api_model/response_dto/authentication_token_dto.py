from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class AuthenticationTokenDto(Parsable):
    # Confirmation email URL
    confirm_url: Optional[str] = None
    # Token expiration time
    expires: Optional[datetime.datetime] = None
    # Phone number
    phone_noise: Optional[str] = None
    # Specifies if the authentication code is sent by SMS or not
    sms: Optional[bool] = None
    # Specifies if the two-factor application is used or not
    tfa: Optional[bool] = None
    # Two-factor authentication key
    tfa_key: Optional[str] = None
    # Authentication token
    token: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AuthenticationTokenDto:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AuthenticationTokenDto
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AuthenticationTokenDto()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "confirmUrl": lambda n : setattr(self, 'confirm_url', n.get_str_value()),
            "expires": lambda n : setattr(self, 'expires', n.get_datetime_value()),
            "phoneNoise": lambda n : setattr(self, 'phone_noise', n.get_str_value()),
            "sms": lambda n : setattr(self, 'sms', n.get_bool_value()),
            "tfa": lambda n : setattr(self, 'tfa', n.get_bool_value()),
            "tfaKey": lambda n : setattr(self, 'tfa_key', n.get_str_value()),
            "token": lambda n : setattr(self, 'token', n.get_str_value()),
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
        writer.write_str_value("confirmUrl", self.confirm_url)
        writer.write_datetime_value("expires", self.expires)
        writer.write_str_value("phoneNoise", self.phone_noise)
        writer.write_bool_value("sms", self.sms)
        writer.write_bool_value("tfa", self.tfa)
        writer.write_str_value("tfaKey", self.tfa_key)
        writer.write_str_value("token", self.token)
    

