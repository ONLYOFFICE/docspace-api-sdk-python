from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .....api.core.api_date_time import ApiDateTime

@dataclass
class FileLinkRequest(Parsable):
    """
    External link parameters
    """
    # [0 - None, 1 - Read and write, 2 - Read, 3 - Restrict, 4 - Varies, 5 - Review, 6 - Comment, 7 - Fill forms, 8 - Custom filter, 9 - Room manager, 10 - Editing, 11 - Content creator]
    access: Optional[int] = None
    # The expirationDate property
    expiration_date: Optional[ApiDateTime] = None
    # Link scope
    internal: Optional[bool] = None
    # Link ID
    link_id: Optional[UUID] = None
    # Primary link flag
    primary: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> FileLinkRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FileLinkRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return FileLinkRequest()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .....api.core.api_date_time import ApiDateTime

        from .....api.core.api_date_time import ApiDateTime

        fields: Dict[str, Callable[[Any], None]] = {
            "access": lambda n : setattr(self, 'access', n.get_int_value()),
            "expirationDate": lambda n : setattr(self, 'expiration_date', n.get_object_value(ApiDateTime)),
            "internal": lambda n : setattr(self, 'internal', n.get_bool_value()),
            "linkId": lambda n : setattr(self, 'link_id', n.get_uuid_value()),
            "primary": lambda n : setattr(self, 'primary', n.get_bool_value()),
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
        writer.write_object_value("expirationDate", self.expiration_date)
        writer.write_bool_value("internal", self.internal)
        writer.write_uuid_value("linkId", self.link_id)
        writer.write_bool_value("primary", self.primary)
    

