from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....api.collections.item_key_value_pair.system.string.system.string import String

@dataclass
class StorageRequestsDto(Parsable):
    """
    Storage settings request parameters
    """
    # Storage name
    module: Optional[str] = None
    # Storage properties
    props: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> StorageRequestsDto:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: StorageRequestsDto
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return StorageRequestsDto()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .....api.collections.item_key_value_pair.system.string.system.string import String

        from .....api.collections.item_key_value_pair.system.string.system.string import String

        fields: Dict[str, Callable[[Any], None]] = {
            "module": lambda n : setattr(self, 'module', n.get_str_value()),
            "props": lambda n : setattr(self, 'props', n.get_collection_of_object_values(Str)),
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
        from .....api.collections.item_key_value_pair.system.string.system.string import String

        writer.write_str_value("module", self.module)
        writer.write_collection_of_object_values("props", self.props)
    

