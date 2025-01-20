from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class EmbeddedConfig(Parsable):
    # Embed url
    embed_url: Optional[str] = None
    # Save url
    save_url: Optional[str] = None
    # Share link param
    share_link_param: Optional[str] = None
    # Share url
    share_url: Optional[str] = None
    # Toolbar docked
    toolbar_docked: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EmbeddedConfig:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EmbeddedConfig
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EmbeddedConfig()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "embedUrl": lambda n : setattr(self, 'embed_url', n.get_str_value()),
            "saveUrl": lambda n : setattr(self, 'save_url', n.get_str_value()),
            "shareLinkParam": lambda n : setattr(self, 'share_link_param', n.get_str_value()),
            "shareUrl": lambda n : setattr(self, 'share_url', n.get_str_value()),
            "toolbarDocked": lambda n : setattr(self, 'toolbar_docked', n.get_str_value()),
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
        writer.write_str_value("shareLinkParam", self.share_link_param)
    

