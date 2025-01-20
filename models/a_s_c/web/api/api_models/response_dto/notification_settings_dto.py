from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class NotificationSettingsDto(Parsable):
    # Specifies if the notification type is enabled or not
    is_enabled: Optional[bool] = None
    # [0 - Badges, 1 - Rooms activity, 2 - Daily feed, 3 - Usefull tips]
    type: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> NotificationSettingsDto:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: NotificationSettingsDto
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return NotificationSettingsDto()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "isEnabled": lambda n : setattr(self, 'is_enabled', n.get_bool_value()),
            "type": lambda n : setattr(self, 'type', n.get_int_value()),
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
        writer.write_bool_value("isEnabled", self.is_enabled)
        writer.write_int_value("type", self.type)
    

