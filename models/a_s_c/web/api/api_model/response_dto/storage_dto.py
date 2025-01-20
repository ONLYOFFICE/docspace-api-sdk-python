from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ....studio.user_controls.management.auth_key import AuthKey

@dataclass
class StorageDto(Parsable):
    # Specifies if this is the current storage or not
    current: Optional[bool] = None
    # ID
    id: Optional[str] = None
    # Specifies if this storage can be set or not
    is_set: Optional[bool] = None
    # List of authentication keys
    properties: Optional[List[AuthKey]] = None
    # Title
    title: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> StorageDto:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: StorageDto
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return StorageDto()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ....studio.user_controls.management.auth_key import AuthKey

        from ....studio.user_controls.management.auth_key import AuthKey

        fields: Dict[str, Callable[[Any], None]] = {
            "current": lambda n : setattr(self, 'current', n.get_bool_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "isSet": lambda n : setattr(self, 'is_set', n.get_bool_value()),
            "properties": lambda n : setattr(self, 'properties', n.get_collection_of_object_values(AuthKey)),
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
        from ....studio.user_controls.management.auth_key import AuthKey

        writer.write_bool_value("current", self.current)
        writer.write_str_value("id", self.id)
        writer.write_bool_value("isSet", self.is_set)
        writer.write_collection_of_object_values("properties", self.properties)
        writer.write_str_value("title", self.title)
    

