from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class WebhooksConfigRequestsDto(Parsable):
    """
    Webhook request parameters
    """
    # Enabled or not
    enabled: Optional[bool] = None
    # ID
    id: Optional[int] = None
    # Name
    name: Optional[str] = None
    # Secret key
    secret_key: Optional[str] = None
    # SSL
    ssl: Optional[bool] = None
    # URI
    uri: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WebhooksConfigRequestsDto:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WebhooksConfigRequestsDto
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WebhooksConfigRequestsDto()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "enabled": lambda n : setattr(self, 'enabled', n.get_bool_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "secretKey": lambda n : setattr(self, 'secret_key', n.get_str_value()),
            "ssl": lambda n : setattr(self, 'ssl', n.get_bool_value()),
            "uri": lambda n : setattr(self, 'uri', n.get_str_value()),
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
        writer.write_bool_value("enabled", self.enabled)
        writer.write_int_value("id", self.id)
        writer.write_str_value("name", self.name)
        writer.write_str_value("secretKey", self.secret_key)
        writer.write_bool_value("ssl", self.ssl)
        writer.write_str_value("uri", self.uri)
    

