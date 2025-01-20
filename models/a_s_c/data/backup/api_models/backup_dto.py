from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ....api.collections.item_key_value_pair.system.object.system.object import Object

@dataclass
class BackupDto(Parsable):
    """
    Backup parameters
    """
    # Specifies if a dump will be created or not
    dump: Optional[bool] = None
    # Storage parameters
    storage_params: Optional[List[object]] = None
    # [0 - Documents, 1 - Thridparty documents, 2 - Custom cloud, 3 - Local, 4 - Data store, 5 - Thirdparty consumer]
    storage_type: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BackupDto:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BackupDto
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return BackupDto()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ....api.collections.item_key_value_pair.system.object.system.object import Object

        from ....api.collections.item_key_value_pair.system.object.system.object import Object

        fields: Dict[str, Callable[[Any], None]] = {
            "dump": lambda n : setattr(self, 'dump', n.get_bool_value()),
            "storageParams": lambda n : setattr(self, 'storage_params', n.get_collection_of_object_values(Object)),
            "storageType": lambda n : setattr(self, 'storage_type', n.get_int_value()),
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
        from ....api.collections.item_key_value_pair.system.object.system.object import Object

        writer.write_bool_value("dump", self.dump)
        writer.write_collection_of_object_values("storageParams", self.storage_params)
        writer.write_int_value("storageType", self.storage_type)
    

