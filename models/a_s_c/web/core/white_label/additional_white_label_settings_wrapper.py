from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .additional_white_label_settings import AdditionalWhiteLabelSettings

@dataclass
class AdditionalWhiteLabelSettingsWrapper(Parsable):
    """
    Additional white label settings
    """
    # The settings property
    settings: Optional[AdditionalWhiteLabelSettings] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AdditionalWhiteLabelSettingsWrapper:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AdditionalWhiteLabelSettingsWrapper
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AdditionalWhiteLabelSettingsWrapper()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .additional_white_label_settings import AdditionalWhiteLabelSettings

        from .additional_white_label_settings import AdditionalWhiteLabelSettings

        fields: Dict[str, Callable[[Any], None]] = {
            "settings": lambda n : setattr(self, 'settings', n.get_object_value(AdditionalWhiteLabelSettings)),
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
        from .additional_white_label_settings import AdditionalWhiteLabelSettings

        writer.write_object_value("settings", self.settings)
    

