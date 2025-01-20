from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class CreateTextOrHtmlFile(Parsable):
    """
    Parameters for creating an HTML file
    """
    # File contents
    content: Optional[str] = None
    # Create new if exist
    create_new_if_exist: Optional[bool] = None
    # File title
    title: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CreateTextOrHtmlFile:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CreateTextOrHtmlFile
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CreateTextOrHtmlFile()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "content": lambda n : setattr(self, 'content', n.get_str_value()),
            "createNewIfExist": lambda n : setattr(self, 'create_new_if_exist', n.get_bool_value()),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
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
        writer.write_str_value("content", self.content)
        writer.write_bool_value("createNewIfExist", self.create_new_if_exist)
        writer.write_str_value("title", self.title)
    

