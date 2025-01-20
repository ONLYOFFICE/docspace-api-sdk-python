from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ....core.utility.settings.custom_color_themes_settings_item import CustomColorThemesSettingsItem

@dataclass
class CustomColorThemesSettingsRequestsDto(Parsable):
    """
    Portal theme settings
    """
    # Selected or not
    selected: Optional[int] = None
    # The theme property
    theme: Optional[CustomColorThemesSettingsItem] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CustomColorThemesSettingsRequestsDto:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CustomColorThemesSettingsRequestsDto
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CustomColorThemesSettingsRequestsDto()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ....core.utility.settings.custom_color_themes_settings_item import CustomColorThemesSettingsItem

        from ....core.utility.settings.custom_color_themes_settings_item import CustomColorThemesSettingsItem

        fields: Dict[str, Callable[[Any], None]] = {
            "selected": lambda n : setattr(self, 'selected', n.get_int_value()),
            "theme": lambda n : setattr(self, 'theme', n.get_object_value(CustomColorThemesSettingsItem)),
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

        writer.write_int_value("selected", self.selected)
        writer.write_object_value("theme", self.theme)
    

