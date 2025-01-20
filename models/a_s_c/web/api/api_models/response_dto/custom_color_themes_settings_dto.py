from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ....core.utility.settings.custom_color_themes_settings_item import CustomColorThemesSettingsItem

@dataclass
class CustomColorThemesSettingsDto(Parsable):
    # Limit
    limit: Optional[int] = None
    # Selected
    selected: Optional[int] = None
    # Themes
    themes: Optional[List[CustomColorThemesSettingsItem]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CustomColorThemesSettingsDto:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CustomColorThemesSettingsDto
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CustomColorThemesSettingsDto()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ....core.utility.settings.custom_color_themes_settings_item import CustomColorThemesSettingsItem

        from ....core.utility.settings.custom_color_themes_settings_item import CustomColorThemesSettingsItem

        fields: Dict[str, Callable[[Any], None]] = {
            "limit": lambda n : setattr(self, 'limit', n.get_int_value()),
            "selected": lambda n : setattr(self, 'selected', n.get_int_value()),
            "themes": lambda n : setattr(self, 'themes', n.get_collection_of_object_values(CustomColorThemesSettingsItem)),
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
        from ....core.utility.settings.custom_color_themes_settings_item import CustomColorThemesSettingsItem

        writer.write_int_value("limit", self.limit)
        writer.write_int_value("selected", self.selected)
        writer.write_collection_of_object_values("themes", self.themes)
    

