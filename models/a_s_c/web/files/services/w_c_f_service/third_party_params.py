from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....files.core.auth_data import AuthData

@dataclass
class ThirdPartyParams(Parsable):
    # The auth_data property
    auth_data: Optional[AuthData] = None
    # Specifies if this is a corporate account or not
    corporate: Optional[bool] = None
    # Customer title
    customer_title: Optional[str] = None
    # Provider ID
    provider_id: Optional[int] = None
    # Provider key
    provider_key: Optional[str] = None
    # Specifies if this is a room storage or not
    rooms_storage: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ThirdPartyParams:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ThirdPartyParams
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ThirdPartyParams()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .....files.core.auth_data import AuthData

        from .....files.core.auth_data import AuthData

        fields: Dict[str, Callable[[Any], None]] = {
            "auth_data": lambda n : setattr(self, 'auth_data', n.get_object_value(AuthData)),
            "corporate": lambda n : setattr(self, 'corporate', n.get_bool_value()),
            "customer_title": lambda n : setattr(self, 'customer_title', n.get_str_value()),
            "provider_id": lambda n : setattr(self, 'provider_id', n.get_int_value()),
            "provider_key": lambda n : setattr(self, 'provider_key', n.get_str_value()),
            "roomsStorage": lambda n : setattr(self, 'rooms_storage', n.get_bool_value()),
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
        from .....files.core.auth_data import AuthData

        writer.write_object_value("auth_data", self.auth_data)
        writer.write_bool_value("corporate", self.corporate)
        writer.write_str_value("customer_title", self.customer_title)
        writer.write_int_value("provider_id", self.provider_id)
        writer.write_str_value("provider_key", self.provider_key)
        writer.write_bool_value("roomsStorage", self.rooms_storage)
    

