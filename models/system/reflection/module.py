from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from ..module_handle import ModuleHandle
    from .assembly import Assembly
    from .custom_attribute_data import CustomAttributeData

@dataclass
class Module(Parsable):
    # The assembly property
    assembly: Optional[Assembly] = None
    # The customAttributes property
    custom_attributes: Optional[List[CustomAttributeData]] = None
    # The fullyQualifiedName property
    fully_qualified_name: Optional[str] = None
    # The mdStreamVersion property
    md_stream_version: Optional[int] = None
    # The metadataToken property
    metadata_token: Optional[int] = None
    # The moduleHandle property
    module_handle: Optional[ModuleHandle] = None
    # The moduleVersionId property
    module_version_id: Optional[UUID] = None
    # The name property
    name: Optional[str] = None
    # The scopeName property
    scope_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Module:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Module
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Module()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ..module_handle import ModuleHandle
        from .assembly import Assembly
        from .custom_attribute_data import CustomAttributeData

        from ..module_handle import ModuleHandle
        from .assembly import Assembly
        from .custom_attribute_data import CustomAttributeData

        fields: Dict[str, Callable[[Any], None]] = {
            "assembly": lambda n : setattr(self, 'assembly', n.get_object_value(Assembly)),
            "customAttributes": lambda n : setattr(self, 'custom_attributes', n.get_collection_of_object_values(CustomAttributeData)),
            "fullyQualifiedName": lambda n : setattr(self, 'fully_qualified_name', n.get_str_value()),
            "mdStreamVersion": lambda n : setattr(self, 'md_stream_version', n.get_int_value()),
            "metadataToken": lambda n : setattr(self, 'metadata_token', n.get_int_value()),
            "moduleHandle": lambda n : setattr(self, 'module_handle', n.get_object_value(ModuleHandle)),
            "moduleVersionId": lambda n : setattr(self, 'module_version_id', n.get_uuid_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "scopeName": lambda n : setattr(self, 'scope_name', n.get_str_value()),
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
        from ..module_handle import ModuleHandle
        from .assembly import Assembly
        from .custom_attribute_data import CustomAttributeData

        writer.write_object_value("assembly", self.assembly)
        writer.write_object_value("moduleHandle", self.module_handle)
    

