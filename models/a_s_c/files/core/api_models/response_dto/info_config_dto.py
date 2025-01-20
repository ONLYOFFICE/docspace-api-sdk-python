from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....web.files.services.w_c_f_service.ace_short_wrapper import AceShortWrapper

@dataclass
class InfoConfigDto(Parsable):
    # Favorite
    favorite: Optional[bool] = None
    # Folder
    folder: Optional[str] = None
    # Owner
    owner: Optional[str] = None
    # Sharing settings
    sharing_settings: Optional[List[AceShortWrapper]] = None
    # [0 - Desktop, 1 - Mobile, 2 - Embedded]
    type: Optional[int] = None
    # Uploaded
    uploaded: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> InfoConfigDto:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: InfoConfigDto
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return InfoConfigDto()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .....web.files.services.w_c_f_service.ace_short_wrapper import AceShortWrapper

        from .....web.files.services.w_c_f_service.ace_short_wrapper import AceShortWrapper

        fields: Dict[str, Callable[[Any], None]] = {
            "favorite": lambda n : setattr(self, 'favorite', n.get_bool_value()),
            "folder": lambda n : setattr(self, 'folder', n.get_str_value()),
            "owner": lambda n : setattr(self, 'owner', n.get_str_value()),
            "sharingSettings": lambda n : setattr(self, 'sharing_settings', n.get_collection_of_object_values(AceShortWrapper)),
            "type": lambda n : setattr(self, 'type', n.get_int_value()),
            "uploaded": lambda n : setattr(self, 'uploaded', n.get_str_value()),
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
        from .....web.files.services.w_c_f_service.ace_short_wrapper import AceShortWrapper

        writer.write_bool_value("favorite", self.favorite)
        writer.write_str_value("folder", self.folder)
        writer.write_str_value("owner", self.owner)
        writer.write_collection_of_object_values("sharingSettings", self.sharing_settings)
        writer.write_int_value("type", self.type)
        writer.write_str_value("uploaded", self.uploaded)
    

