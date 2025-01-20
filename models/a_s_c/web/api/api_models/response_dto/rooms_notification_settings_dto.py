from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .rooms_notification_settings_dto_disabled_rooms import RoomsNotificationSettingsDto_disabledRooms

@dataclass
class RoomsNotificationSettingsDto(Parsable):
    # List of rooms with the disabled notifications
    disabled_rooms: Optional[List[RoomsNotificationSettingsDto_disabledRooms]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RoomsNotificationSettingsDto:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RoomsNotificationSettingsDto
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RoomsNotificationSettingsDto()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .rooms_notification_settings_dto_disabled_rooms import RoomsNotificationSettingsDto_disabledRooms

        from .rooms_notification_settings_dto_disabled_rooms import RoomsNotificationSettingsDto_disabledRooms

        fields: Dict[str, Callable[[Any], None]] = {
            "disabledRooms": lambda n : setattr(self, 'disabled_rooms', n.get_collection_of_object_values(RoomsNotificationSettingsDto_disabledRooms)),
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
        from .rooms_notification_settings_dto_disabled_rooms import RoomsNotificationSettingsDto_disabledRooms

        writer.write_collection_of_object_values("disabledRooms", self.disabled_rooms)
    

