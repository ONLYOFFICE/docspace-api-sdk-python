from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class DocServiceUrlDto(Parsable):
    # Doc service portal url
    doc_service_portal_url: Optional[str] = None
    # Doc service url
    doc_service_url: Optional[str] = None
    # Doc service url api
    doc_service_url_api: Optional[str] = None
    # Doc service url internal
    doc_service_url_internal: Optional[str] = None
    # Is default
    is_default: Optional[bool] = None
    # Version
    version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DocServiceUrlDto:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DocServiceUrlDto
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DocServiceUrlDto()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "docServicePortalUrl": lambda n : setattr(self, 'doc_service_portal_url', n.get_str_value()),
            "docServiceUrl": lambda n : setattr(self, 'doc_service_url', n.get_str_value()),
            "docServiceUrlApi": lambda n : setattr(self, 'doc_service_url_api', n.get_str_value()),
            "docServiceUrlInternal": lambda n : setattr(self, 'doc_service_url_internal', n.get_str_value()),
            "isDefault": lambda n : setattr(self, 'is_default', n.get_bool_value()),
            "version": lambda n : setattr(self, 'version', n.get_str_value()),
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
        writer.write_str_value("docServicePortalUrl", self.doc_service_portal_url)
        writer.write_str_value("docServiceUrl", self.doc_service_url)
        writer.write_str_value("docServiceUrlApi", self.doc_service_url_api)
        writer.write_str_value("docServiceUrlInternal", self.doc_service_url_internal)
        writer.write_bool_value("isDefault", self.is_default)
        writer.write_str_value("version", self.version)
    

