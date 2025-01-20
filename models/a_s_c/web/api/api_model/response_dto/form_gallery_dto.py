from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class FormGalleryDto(Parsable):
    # Domain
    domain: Optional[str] = None
    # Ext
    ext: Optional[str] = None
    # Path
    path: Optional[str] = None
    # Upload dashboard
    upload_dashboard: Optional[str] = None
    # Upload domain
    upload_domain: Optional[str] = None
    # Upload ext
    upload_ext: Optional[str] = None
    # Upload path
    upload_path: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> FormGalleryDto:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FormGalleryDto
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return FormGalleryDto()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "domain": lambda n : setattr(self, 'domain', n.get_str_value()),
            "ext": lambda n : setattr(self, 'ext', n.get_str_value()),
            "path": lambda n : setattr(self, 'path', n.get_str_value()),
            "uploadDashboard": lambda n : setattr(self, 'upload_dashboard', n.get_str_value()),
            "uploadDomain": lambda n : setattr(self, 'upload_domain', n.get_str_value()),
            "uploadExt": lambda n : setattr(self, 'upload_ext', n.get_str_value()),
            "uploadPath": lambda n : setattr(self, 'upload_path', n.get_str_value()),
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
        writer.write_str_value("domain", self.domain)
        writer.write_str_value("ext", self.ext)
        writer.write_str_value("path", self.path)
        writer.write_str_value("uploadDashboard", self.upload_dashboard)
        writer.write_str_value("uploadDomain", self.upload_domain)
        writer.write_str_value("uploadExt", self.upload_ext)
        writer.write_str_value("uploadPath", self.upload_path)
    

