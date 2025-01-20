from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .json_element_dest_folder_id import JsonElement_destFolderId

@dataclass
class JsonElement(Parsable):
    """
    Parameters for copying a file
    """
    # Destination folder ID
    dest_folder_id: Optional[JsonElement_destFolderId] = None
    # Destination file title
    dest_title: Optional[str] = None
    # Specifies whether to allow the creation of external extension files or not
    enable_external_ext: Optional[bool] = None
    # Password
    password: Optional[str] = None
    # Convert to form
    to_form: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> JsonElement:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: JsonElement
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return JsonElement()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .json_element_dest_folder_id import JsonElement_destFolderId

        from .json_element_dest_folder_id import JsonElement_destFolderId

        fields: Dict[str, Callable[[Any], None]] = {
            "destFolderId": lambda n : setattr(self, 'dest_folder_id', n.get_object_value(JsonElement_destFolderId)),
            "destTitle": lambda n : setattr(self, 'dest_title', n.get_str_value()),
            "enableExternalExt": lambda n : setattr(self, 'enable_external_ext', n.get_bool_value()),
            "password": lambda n : setattr(self, 'password', n.get_str_value()),
            "toForm": lambda n : setattr(self, 'to_form', n.get_bool_value()),
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
        from .json_element_dest_folder_id import JsonElement_destFolderId

        writer.write_object_value("destFolderId", self.dest_folder_id)
        writer.write_str_value("destTitle", self.dest_title)
        writer.write_bool_value("enableExternalExt", self.enable_external_ext)
        writer.write_str_value("password", self.password)
        writer.write_bool_value("toForm", self.to_form)
    

