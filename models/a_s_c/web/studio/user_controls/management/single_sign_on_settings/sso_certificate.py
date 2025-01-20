from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class SsoCertificate(Parsable):
    # Action
    action: Optional[str] = None
    # Certificate
    crt: Optional[str] = None
    # Domain name
    domain_name: Optional[str] = None
    # Expiration date
    expired_date: Optional[datetime.datetime] = None
    # Key
    key: Optional[str] = None
    # Specifies if a certificate is self-signed or not
    self_signed: Optional[bool] = None
    # Start date
    start_date: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SsoCertificate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SsoCertificate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SsoCertificate()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "action": lambda n : setattr(self, 'action', n.get_str_value()),
            "crt": lambda n : setattr(self, 'crt', n.get_str_value()),
            "domainName": lambda n : setattr(self, 'domain_name', n.get_str_value()),
            "expiredDate": lambda n : setattr(self, 'expired_date', n.get_datetime_value()),
            "key": lambda n : setattr(self, 'key', n.get_str_value()),
            "selfSigned": lambda n : setattr(self, 'self_signed', n.get_bool_value()),
            "startDate": lambda n : setattr(self, 'start_date', n.get_datetime_value()),
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
        writer.write_str_value("action", self.action)
        writer.write_str_value("crt", self.crt)
        writer.write_str_value("domainName", self.domain_name)
        writer.write_datetime_value("expiredDate", self.expired_date)
        writer.write_str_value("key", self.key)
        writer.write_bool_value("selfSigned", self.self_signed)
        writer.write_datetime_value("startDate", self.start_date)
    

