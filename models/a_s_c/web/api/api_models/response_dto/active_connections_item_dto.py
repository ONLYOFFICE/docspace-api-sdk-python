from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .....api.core.api_date_time import ApiDateTime

@dataclass
class ActiveConnectionsItemDto(Parsable):
    # Browser
    browser: Optional[str] = None
    # City
    city: Optional[str] = None
    # Country
    country: Optional[str] = None
    # The date property
    date: Optional[ApiDateTime] = None
    # Id
    id: Optional[int] = None
    # Ip
    ip: Optional[str] = None
    # Mobile
    mobile: Optional[bool] = None
    # Page
    page: Optional[str] = None
    # Platform
    platform: Optional[str] = None
    # Tenant id
    tenant_id: Optional[int] = None
    # User id
    user_id: Optional[UUID] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ActiveConnectionsItemDto:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ActiveConnectionsItemDto
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ActiveConnectionsItemDto()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .....api.core.api_date_time import ApiDateTime

        from .....api.core.api_date_time import ApiDateTime

        fields: Dict[str, Callable[[Any], None]] = {
            "browser": lambda n : setattr(self, 'browser', n.get_str_value()),
            "city": lambda n : setattr(self, 'city', n.get_str_value()),
            "country": lambda n : setattr(self, 'country', n.get_str_value()),
            "date": lambda n : setattr(self, 'date', n.get_object_value(ApiDateTime)),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "ip": lambda n : setattr(self, 'ip', n.get_str_value()),
            "mobile": lambda n : setattr(self, 'mobile', n.get_bool_value()),
            "page": lambda n : setattr(self, 'page', n.get_str_value()),
            "platform": lambda n : setattr(self, 'platform', n.get_str_value()),
            "tenantId": lambda n : setattr(self, 'tenant_id', n.get_int_value()),
            "userId": lambda n : setattr(self, 'user_id', n.get_uuid_value()),
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
        from .....api.core.api_date_time import ApiDateTime

        writer.write_str_value("browser", self.browser)
        writer.write_str_value("city", self.city)
        writer.write_str_value("country", self.country)
        writer.write_object_value("date", self.date)
        writer.write_int_value("id", self.id)
        writer.write_str_value("ip", self.ip)
        writer.write_bool_value("mobile", self.mobile)
        writer.write_str_value("page", self.page)
        writer.write_str_value("platform", self.platform)
        writer.write_int_value("tenantId", self.tenant_id)
        writer.write_uuid_value("userId", self.user_id)
    

