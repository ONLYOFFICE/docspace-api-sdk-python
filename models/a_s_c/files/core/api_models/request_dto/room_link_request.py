from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .....api.core.api_date_time import ApiDateTime

@dataclass
class RoomLinkRequest(Parsable):
    """
    Link parameters
    """
    # [0 - None, 1 - Read and write, 2 - Read, 3 - Restrict, 4 - Varies, 5 - Review, 6 - Comment, 7 - Fill forms, 8 - Custom filter, 9 - Room manager, 10 - Editing, 11 - Content creator]
    access: Optional[int] = None
    # Specifies whether downloading a file from a link is disabled or not
    deny_download: Optional[bool] = None
    # The expirationDate property
    expiration_date: Optional[ApiDateTime] = None
    # Link ID
    link_id: Optional[UUID] = None
    # [0 - Invitation, 1 - External]
    link_type: Optional[int] = None
    # Link password
    password: Optional[str] = None
    # Link name
    title: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RoomLinkRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RoomLinkRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RoomLinkRequest()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .....api.core.api_date_time import ApiDateTime

        from .....api.core.api_date_time import ApiDateTime

        fields: Dict[str, Callable[[Any], None]] = {
            "access": lambda n : setattr(self, 'access', n.get_int_value()),
            "denyDownload": lambda n : setattr(self, 'deny_download', n.get_bool_value()),
            "expirationDate": lambda n : setattr(self, 'expiration_date', n.get_object_value(ApiDateTime)),
            "linkId": lambda n : setattr(self, 'link_id', n.get_uuid_value()),
            "linkType": lambda n : setattr(self, 'link_type', n.get_int_value()),
            "password": lambda n : setattr(self, 'password', n.get_str_value()),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
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

        writer.write_int_value("access", self.access)
        writer.write_bool_value("denyDownload", self.deny_download)
        writer.write_object_value("expirationDate", self.expiration_date)
        writer.write_uuid_value("linkId", self.link_id)
        writer.write_int_value("linkType", self.link_type)
        writer.write_str_value("password", self.password)
        writer.write_str_value("title", self.title)
    

