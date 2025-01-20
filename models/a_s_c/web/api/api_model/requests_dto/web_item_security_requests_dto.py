from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

@dataclass
class WebItemSecurityRequestsDto(Parsable):
    """
    Module request parameters
    """
    # Specifies if the module security settings are enabled or not
    enabled: Optional[bool] = None
    # Module ID
    id: Optional[str] = None
    # List of user/group IDs with the access to the module
    subjects: Optional[List[UUID]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WebItemSecurityRequestsDto:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WebItemSecurityRequestsDto
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WebItemSecurityRequestsDto()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "enabled": lambda n : setattr(self, 'enabled', n.get_bool_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "subjects": lambda n : setattr(self, 'subjects', n.get_collection_of_primitive_values(UUID)),
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
        writer.write_bool_value("enabled", self.enabled)
        writer.write_str_value("id", self.id)
        writer.write_collection_of_primitive_values("subjects", self.subjects)
    

