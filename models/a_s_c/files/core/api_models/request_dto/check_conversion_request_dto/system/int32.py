from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class Int32(Parsable):
    """
    Request parameters for starting file conversion
    """
    # Create new if exists
    create_new_if_exist: Optional[bool] = None
    # File ID
    file_id: Optional[int] = None
    # Output type
    output_type: Optional[str] = None
    # Password
    password: Optional[str] = None
    # Specifies whether to start a conversion process or not
    start_convert: Optional[bool] = None
    # Specifies if the conversion process is synchronous or not
    sync: Optional[bool] = None
    # File version
    version: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Int32:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Int32
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Int32()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "createNewIfExist": lambda n : setattr(self, 'create_new_if_exist', n.get_bool_value()),
            "fileId": lambda n : setattr(self, 'file_id', n.get_int_value()),
            "outputType": lambda n : setattr(self, 'output_type', n.get_str_value()),
            "password": lambda n : setattr(self, 'password', n.get_str_value()),
            "startConvert": lambda n : setattr(self, 'start_convert', n.get_bool_value()),
            "sync": lambda n : setattr(self, 'sync', n.get_bool_value()),
            "version": lambda n : setattr(self, 'version', n.get_int_value()),
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
        writer.write_bool_value("createNewIfExist", self.create_new_if_exist)
        writer.write_int_value("fileId", self.file_id)
        writer.write_str_value("outputType", self.output_type)
        writer.write_str_value("password", self.password)
        writer.write_bool_value("startConvert", self.start_convert)
        writer.write_bool_value("sync", self.sync)
        writer.write_int_value("version", self.version)
    

