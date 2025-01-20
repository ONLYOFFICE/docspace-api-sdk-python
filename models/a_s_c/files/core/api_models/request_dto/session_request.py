from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....api.core.api_date_time import ApiDateTime

@dataclass
class SessionRequest(Parsable):
    """
    Session parameters
    """
    # Create new if exists
    create_new_if_exist: Optional[bool] = None
    # The createOn property
    create_on: Optional[ApiDateTime] = None
    # Specifies whether to encrypt a file or not
    encrypted: Optional[bool] = None
    # File name
    file_name: Optional[str] = None
    # File length in bytes
    file_size: Optional[int] = None
    # Relative path to the folder
    relative_path: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SessionRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SessionRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SessionRequest()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .....api.core.api_date_time import ApiDateTime

        from .....api.core.api_date_time import ApiDateTime

        fields: Dict[str, Callable[[Any], None]] = {
            "createNewIfExist": lambda n : setattr(self, 'create_new_if_exist', n.get_bool_value()),
            "createOn": lambda n : setattr(self, 'create_on', n.get_object_value(ApiDateTime)),
            "encrypted": lambda n : setattr(self, 'encrypted', n.get_bool_value()),
            "fileName": lambda n : setattr(self, 'file_name', n.get_str_value()),
            "fileSize": lambda n : setattr(self, 'file_size', n.get_int_value()),
            "relativePath": lambda n : setattr(self, 'relative_path', n.get_str_value()),
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
        from .....api.core.api_date_time import ApiDateTime

        writer.write_bool_value("createNewIfExist", self.create_new_if_exist)
        writer.write_object_value("createOn", self.create_on)
        writer.write_bool_value("encrypted", self.encrypted)
        writer.write_str_value("fileName", self.file_name)
        writer.write_int_value("fileSize", self.file_size)
        writer.write_str_value("relativePath", self.relative_path)
    

