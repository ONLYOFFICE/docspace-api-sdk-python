from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class AceShortWrapper(Parsable):
    # Is link
    is_link: Optional[bool] = None
    # User access rights to the file
    permissions: Optional[str] = None
    # User
    user: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AceShortWrapper:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AceShortWrapper
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AceShortWrapper()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "isLink": lambda n : setattr(self, 'is_link', n.get_bool_value()),
            "permissions": lambda n : setattr(self, 'permissions', n.get_str_value()),
            "user": lambda n : setattr(self, 'user', n.get_str_value()),
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
        writer.write_bool_value("isLink", self.is_link)
        writer.write_str_value("permissions", self.permissions)
        writer.write_str_value("user", self.user)
    

