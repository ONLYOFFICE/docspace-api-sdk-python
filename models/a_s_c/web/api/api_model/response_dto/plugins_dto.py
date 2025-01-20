from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class PluginsDto(Parsable):
    # Specifies if the plugins can be deleted or not
    delete: Optional[bool] = None
    # Specifies if the plugins are enabled or not
    enabled: Optional[bool] = None
    # Specifies if the plugins can be uploaded or not
    upload: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PluginsDto:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PluginsDto
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PluginsDto()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "delete": lambda n : setattr(self, 'delete', n.get_bool_value()),
            "enabled": lambda n : setattr(self, 'enabled', n.get_bool_value()),
            "upload": lambda n : setattr(self, 'upload', n.get_bool_value()),
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
        writer.write_bool_value("delete", self.delete)
        writer.write_bool_value("enabled", self.enabled)
        writer.write_bool_value("upload", self.upload)
    

