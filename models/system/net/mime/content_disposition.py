from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class ContentDisposition(Parsable):
    # The creationDate property
    creation_date: Optional[datetime.datetime] = None
    # The dispositionType property
    disposition_type: Optional[str] = None
    # The fileName property
    file_name: Optional[str] = None
    # The inline property
    inline: Optional[bool] = None
    # The modificationDate property
    modification_date: Optional[datetime.datetime] = None
    # The readDate property
    read_date: Optional[datetime.datetime] = None
    # The size property
    size: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ContentDisposition:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ContentDisposition
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ContentDisposition()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "creationDate": lambda n : setattr(self, 'creation_date', n.get_datetime_value()),
            "dispositionType": lambda n : setattr(self, 'disposition_type', n.get_str_value()),
            "fileName": lambda n : setattr(self, 'file_name', n.get_str_value()),
            "inline": lambda n : setattr(self, 'inline', n.get_bool_value()),
            "modificationDate": lambda n : setattr(self, 'modification_date', n.get_datetime_value()),
            "readDate": lambda n : setattr(self, 'read_date', n.get_datetime_value()),
            "size": lambda n : setattr(self, 'size', n.get_int_value()),
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
        writer.write_datetime_value("creationDate", self.creation_date)
        writer.write_str_value("dispositionType", self.disposition_type)
        writer.write_str_value("fileName", self.file_name)
        writer.write_bool_value("inline", self.inline)
        writer.write_datetime_value("modificationDate", self.modification_date)
        writer.write_datetime_value("readDate", self.read_date)
        writer.write_int_value("size", self.size)
    

