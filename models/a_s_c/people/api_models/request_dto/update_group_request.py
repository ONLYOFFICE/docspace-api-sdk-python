from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

@dataclass
class UpdateGroupRequest(Parsable):
    """
    Group request parameters
    """
    # Group manager ID
    group_manager: Optional[UUID] = None
    # Group name
    group_name: Optional[str] = None
    # List of user IDs to add to the group
    members_to_add: Optional[List[UUID]] = None
    # List of user IDs to remove from the group
    members_to_remove: Optional[List[UUID]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UpdateGroupRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UpdateGroupRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UpdateGroupRequest()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "groupManager": lambda n : setattr(self, 'group_manager', n.get_uuid_value()),
            "groupName": lambda n : setattr(self, 'group_name', n.get_str_value()),
            "membersToAdd": lambda n : setattr(self, 'members_to_add', n.get_collection_of_primitive_values(UUID)),
            "membersToRemove": lambda n : setattr(self, 'members_to_remove', n.get_collection_of_primitive_values(UUID)),
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
        writer.write_uuid_value("groupManager", self.group_manager)
        writer.write_str_value("groupName", self.group_name)
        writer.write_collection_of_primitive_values("membersToAdd", self.members_to_add)
        writer.write_collection_of_primitive_values("membersToRemove", self.members_to_remove)
    

