from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .custom_color_themes_settings_color_item import CustomColorThemesSettingsColorItem

@dataclass
class CustomColorThemesSettingsItem(Parsable):
    # Theme ID
    id: Optional[int] = None
    # The main property
    main: Optional[CustomColorThemesSettingsColorItem] = None
    # Theme name
    name: Optional[str] = None
    # The text property
    text: Optional[CustomColorThemesSettingsColorItem] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CustomColorThemesSettingsItem:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CustomColorThemesSettingsItem
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CustomColorThemesSettingsItem()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .custom_color_themes_settings_color_item import CustomColorThemesSettingsColorItem

        from .custom_color_themes_settings_color_item import CustomColorThemesSettingsColorItem

        fields: Dict[str, Callable[[Any], None]] = {
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "main": lambda n : setattr(self, 'main', n.get_object_value(CustomColorThemesSettingsColorItem)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "text": lambda n : setattr(self, 'text', n.get_object_value(CustomColorThemesSettingsColorItem)),
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
        from .custom_color_themes_settings_color_item import CustomColorThemesSettingsColorItem

        writer.write_int_value("id", self.id)
        writer.write_object_value("main", self.main)
        writer.write_str_value("name", self.name)
        writer.write_object_value("text", self.text)
    

