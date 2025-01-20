from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class MigratingApiGroup(Parsable):
    # The groupName property
    group_name: Optional[str] = None
    # The moduleName property
    module_name: Optional[str] = None
    # The shouldImport property
    should_import: Optional[bool] = None
    # The userUidList property
    user_uid_list: Optional[List[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MigratingApiGroup:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MigratingApiGroup
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MigratingApiGroup()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "groupName": lambda n : setattr(self, 'group_name', n.get_str_value()),
            "moduleName": lambda n : setattr(self, 'module_name', n.get_str_value()),
            "shouldImport": lambda n : setattr(self, 'should_import', n.get_bool_value()),
            "userUidList": lambda n : setattr(self, 'user_uid_list', n.get_collection_of_primitive_values(str)),
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
        writer.write_str_value("groupName", self.group_name)
        writer.write_str_value("moduleName", self.module_name)
        writer.write_bool_value("shouldImport", self.should_import)
        writer.write_collection_of_primitive_values("userUidList", self.user_uid_list)
    

