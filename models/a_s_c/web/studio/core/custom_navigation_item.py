from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

@dataclass
class CustomNavigationItem(Parsable):
    """
    Custom navigation parameters
    """
    # Big image
    big_img: Optional[str] = None
    # Id
    id: Optional[UUID] = None
    # Label
    label: Optional[str] = None
    # Show in menu or not
    show_in_menu: Optional[bool] = None
    # Show on home page or not
    show_on_home_page: Optional[bool] = None
    # Small image
    small_img: Optional[str] = None
    # URL
    url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CustomNavigationItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CustomNavigationItem
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CustomNavigationItem()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "bigImg": lambda n : setattr(self, 'big_img', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_uuid_value()),
            "label": lambda n : setattr(self, 'label', n.get_str_value()),
            "showInMenu": lambda n : setattr(self, 'show_in_menu', n.get_bool_value()),
            "showOnHomePage": lambda n : setattr(self, 'show_on_home_page', n.get_bool_value()),
            "smallImg": lambda n : setattr(self, 'small_img', n.get_str_value()),
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
        writer.write_str_value("bigImg", self.big_img)
        writer.write_uuid_value("id", self.id)
        writer.write_str_value("label", self.label)
        writer.write_bool_value("showInMenu", self.show_in_menu)
        writer.write_bool_value("showOnHomePage", self.show_on_home_page)
        writer.write_str_value("smallImg", self.small_img)
        writer.write_str_value("url", self.url)
    

