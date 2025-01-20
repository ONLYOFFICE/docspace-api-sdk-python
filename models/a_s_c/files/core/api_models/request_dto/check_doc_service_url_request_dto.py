from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class CheckDocServiceUrlRequestDto(Parsable):
    """
    Request parameters for checking the document service location
    """
    # The Document Server address
    doc_service_url: Optional[str] = None
    # The Document Server address in the local private network
    doc_service_url_internal: Optional[str] = None
    # The Community Server address
    doc_service_url_portal: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CheckDocServiceUrlRequestDto:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CheckDocServiceUrlRequestDto
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CheckDocServiceUrlRequestDto()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "docServiceUrl": lambda n : setattr(self, 'doc_service_url', n.get_str_value()),
            "docServiceUrlInternal": lambda n : setattr(self, 'doc_service_url_internal', n.get_str_value()),
            "docServiceUrlPortal": lambda n : setattr(self, 'doc_service_url_portal', n.get_str_value()),
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
        writer.write_str_value("docServiceUrl", self.doc_service_url)
        writer.write_str_value("docServiceUrlInternal", self.doc_service_url_internal)
        writer.write_str_value("docServiceUrlPortal", self.doc_service_url_portal)
    

