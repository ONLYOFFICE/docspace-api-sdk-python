from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

@dataclass
class Module(Parsable):
    # Product class name
    app_name: Optional[str] = None
    # Description
    description: Optional[str] = None
    # Help URL
    help_url: Optional[str] = None
    # Icon URL
    icon_url: Optional[str] = None
    # ID
    id: Optional[UUID] = None
    # Large image URL
    image_url: Optional[str] = None
    # Specifies if the module is primary or not
    is_primary: Optional[bool] = None
    # Start link
    link: Optional[str] = None
    # Title
    title: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Module:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Module
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Module()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "appName": lambda n : setattr(self, 'app_name', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "helpUrl": lambda n : setattr(self, 'help_url', n.get_str_value()),
            "iconUrl": lambda n : setattr(self, 'icon_url', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_uuid_value()),
            "imageUrl": lambda n : setattr(self, 'image_url', n.get_str_value()),
            "isPrimary": lambda n : setattr(self, 'is_primary', n.get_bool_value()),
            "link": lambda n : setattr(self, 'link', n.get_str_value()),
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
        writer.write_str_value("appName", self.app_name)
        writer.write_str_value("description", self.description)
        writer.write_str_value("helpUrl", self.help_url)
        writer.write_str_value("iconUrl", self.icon_url)
        writer.write_uuid_value("id", self.id)
        writer.write_str_value("imageUrl", self.image_url)
        writer.write_bool_value("isPrimary", self.is_primary)
        writer.write_str_value("link", self.link)
        writer.write_str_value("title", self.title)
    

