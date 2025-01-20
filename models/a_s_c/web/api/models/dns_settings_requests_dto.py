from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class DnsSettingsRequestsDto(Parsable):
    """
    DNS settings request parameters
    """
    # DNS
    dns_name: Optional[str] = None
    # Enabled or not
    enable: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DnsSettingsRequestsDto:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DnsSettingsRequestsDto
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DnsSettingsRequestsDto()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "dnsName": lambda n : setattr(self, 'dns_name', n.get_str_value()),
            "enable": lambda n : setattr(self, 'enable', n.get_bool_value()),
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
        writer.write_str_value("dnsName", self.dns_name)
        writer.write_bool_value("enable", self.enable)
    

