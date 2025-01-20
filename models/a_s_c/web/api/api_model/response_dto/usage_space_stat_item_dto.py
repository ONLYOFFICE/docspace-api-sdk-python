from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class UsageSpaceStatItemDto(Parsable):
    # Specifies if the module space is disabled or not
    disabled: Optional[bool] = None
    # Icon
    icon: Optional[str] = None
    # Name
    name: Optional[str] = None
    # Size
    size: Optional[str] = None
    # URL
    url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UsageSpaceStatItemDto:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UsageSpaceStatItemDto
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UsageSpaceStatItemDto()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "disabled": lambda n : setattr(self, 'disabled', n.get_bool_value()),
            "icon": lambda n : setattr(self, 'icon', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "size": lambda n : setattr(self, 'size', n.get_str_value()),
            "url": lambda n : setattr(self, 'url', n.get_str_value()),
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
        writer.write_bool_value("disabled", self.disabled)
        writer.write_str_value("icon", self.icon)
        writer.write_str_value("name", self.name)
        writer.write_str_value("size", self.size)
        writer.write_str_value("url", self.url)
    

