from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class WebhooksLogDto(Parsable):
    # Config name
    config_name: Optional[str] = None
    # Creation time
    creation_time: Optional[datetime.datetime] = None
    # Delivery time
    delivery: Optional[datetime.datetime] = None
    # ID
    id: Optional[int] = None
    # Method
    method: Optional[str] = None
    # Request headers
    request_headers: Optional[str] = None
    # Request payload
    request_payload: Optional[str] = None
    # Response headers
    response_headers: Optional[str] = None
    # Response payload
    response_payload: Optional[str] = None
    # Route
    route: Optional[str] = None
    # Status
    status: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WebhooksLogDto:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WebhooksLogDto
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WebhooksLogDto()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "configName": lambda n : setattr(self, 'config_name', n.get_str_value()),
            "creationTime": lambda n : setattr(self, 'creation_time', n.get_datetime_value()),
            "delivery": lambda n : setattr(self, 'delivery', n.get_datetime_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "method": lambda n : setattr(self, 'method', n.get_str_value()),
            "requestHeaders": lambda n : setattr(self, 'request_headers', n.get_str_value()),
            "requestPayload": lambda n : setattr(self, 'request_payload', n.get_str_value()),
            "responseHeaders": lambda n : setattr(self, 'response_headers', n.get_str_value()),
            "responsePayload": lambda n : setattr(self, 'response_payload', n.get_str_value()),
            "route": lambda n : setattr(self, 'route', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_int_value()),
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
        writer.write_str_value("configName", self.config_name)
        writer.write_datetime_value("creationTime", self.creation_time)
        writer.write_datetime_value("delivery", self.delivery)
        writer.write_int_value("id", self.id)
        writer.write_str_value("method", self.method)
        writer.write_str_value("requestHeaders", self.request_headers)
        writer.write_str_value("requestPayload", self.request_payload)
        writer.write_str_value("responseHeaders", self.response_headers)
        writer.write_str_value("responsePayload", self.response_payload)
        writer.write_str_value("route", self.route)
        writer.write_int_value("status", self.status)
    

