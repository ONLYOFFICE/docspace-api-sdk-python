from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .file_share_dto import FileShareDto

@dataclass
class RoomSecurityDto(Parsable):
    # List of room members
    members: Optional[List[FileShareDto]] = None
    # Warning
    warning: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RoomSecurityDto:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RoomSecurityDto
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RoomSecurityDto()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .file_share_dto import FileShareDto

        from .file_share_dto import FileShareDto

        fields: Dict[str, Callable[[Any], None]] = {
            "members": lambda n : setattr(self, 'members', n.get_collection_of_object_values(FileShareDto)),
            "warning": lambda n : setattr(self, 'warning', n.get_str_value()),
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
        from .file_share_dto import FileShareDto

        writer.write_collection_of_object_values("members", self.members)
        writer.write_str_value("warning", self.warning)
    

