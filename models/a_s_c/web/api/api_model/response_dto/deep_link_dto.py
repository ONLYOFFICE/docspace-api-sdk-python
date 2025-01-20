from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class DeepLinkDto(Parsable):
    # Android package name
    android_package_name: Optional[str] = None
    # Ios package id
    ios_package_id: Optional[str] = None
    # Url
    url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeepLinkDto:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeepLinkDto
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeepLinkDto()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "androidPackageName": lambda n : setattr(self, 'android_package_name', n.get_str_value()),
            "iosPackageId": lambda n : setattr(self, 'ios_package_id', n.get_str_value()),
            "url": lambda n : setattr(self, 'url', n.get_str_value()),
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
        writer.write_str_value("androidPackageName", self.android_package_name)
        writer.write_str_value("iosPackageId", self.ios_package_id)
        writer.write_str_value("url", self.url)
    

