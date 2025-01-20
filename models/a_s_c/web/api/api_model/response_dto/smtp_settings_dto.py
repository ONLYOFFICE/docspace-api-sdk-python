from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class SmtpSettingsDto(Parsable):
    """
    SMTP settings
    """
    # Credentials username
    credentials_user_name: Optional[str] = None
    # Credentials user password
    credentials_user_password: Optional[str] = None
    # Enables authentication or not
    enable_auth: Optional[bool] = None
    # Enables SSL or not
    enable_s_s_l: Optional[bool] = None
    # Host
    host: Optional[str] = None
    # Specifies if the current settings are default or not
    is_default_settings: Optional[bool] = None
    # Port
    port: Optional[int] = None
    # Sender address
    sender_address: Optional[str] = None
    # Sender display name
    sender_display_name: Optional[str] = None
    # Specifies whether to use NTLM or not
    use_ntlm: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SmtpSettingsDto:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SmtpSettingsDto
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SmtpSettingsDto()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "credentialsUserName": lambda n : setattr(self, 'credentials_user_name', n.get_str_value()),
            "credentialsUserPassword": lambda n : setattr(self, 'credentials_user_password', n.get_str_value()),
            "enableAuth": lambda n : setattr(self, 'enable_auth', n.get_bool_value()),
            "enableSSL": lambda n : setattr(self, 'enable_s_s_l', n.get_bool_value()),
            "host": lambda n : setattr(self, 'host', n.get_str_value()),
            "isDefaultSettings": lambda n : setattr(self, 'is_default_settings', n.get_bool_value()),
            "port": lambda n : setattr(self, 'port', n.get_int_value()),
            "senderAddress": lambda n : setattr(self, 'sender_address', n.get_str_value()),
            "senderDisplayName": lambda n : setattr(self, 'sender_display_name', n.get_str_value()),
            "useNtlm": lambda n : setattr(self, 'use_ntlm', n.get_bool_value()),
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
        writer.write_str_value("credentialsUserName", self.credentials_user_name)
        writer.write_str_value("credentialsUserPassword", self.credentials_user_password)
        writer.write_bool_value("enableAuth", self.enable_auth)
        writer.write_bool_value("enableSSL", self.enable_s_s_l)
        writer.write_str_value("host", self.host)
        writer.write_bool_value("isDefaultSettings", self.is_default_settings)
        writer.write_int_value("port", self.port)
        writer.write_str_value("senderAddress", self.sender_address)
        writer.write_str_value("senderDisplayName", self.sender_display_name)
        writer.write_bool_value("useNtlm", self.use_ntlm)
    

