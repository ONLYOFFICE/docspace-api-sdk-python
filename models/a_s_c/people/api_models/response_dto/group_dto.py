from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from ....web.api.models.employee_full_dto import EmployeeFullDto

@dataclass
class GroupDto(Parsable):
    # Category
    category: Optional[UUID] = None
    # ID
    id: Optional[UUID] = None
    # Specifies if the LDAP settings are enabled for the group or not
    is_l_d_a_p: Optional[bool] = None
    # The manager property
    manager: Optional[EmployeeFullDto] = None
    # List of members
    members: Optional[List[EmployeeFullDto]] = None
    # Members count
    members_count: Optional[int] = None
    # Name
    name: Optional[str] = None
    # Parent
    parent: Optional[UUID] = None
    # Shared
    shared: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> GroupDto:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: GroupDto
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return GroupDto()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ....web.api.models.employee_full_dto import EmployeeFullDto

        from ....web.api.models.employee_full_dto import EmployeeFullDto

        fields: Dict[str, Callable[[Any], None]] = {
            "category": lambda n : setattr(self, 'category', n.get_uuid_value()),
            "id": lambda n : setattr(self, 'id', n.get_uuid_value()),
            "isLDAP": lambda n : setattr(self, 'is_l_d_a_p', n.get_bool_value()),
            "manager": lambda n : setattr(self, 'manager', n.get_object_value(EmployeeFullDto)),
            "members": lambda n : setattr(self, 'members', n.get_collection_of_object_values(EmployeeFullDto)),
            "membersCount": lambda n : setattr(self, 'members_count', n.get_int_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "parent": lambda n : setattr(self, 'parent', n.get_uuid_value()),
            "shared": lambda n : setattr(self, 'shared', n.get_bool_value()),
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
        from ....web.api.models.employee_full_dto import EmployeeFullDto

        writer.write_uuid_value("category", self.category)
        writer.write_uuid_value("id", self.id)
        writer.write_bool_value("isLDAP", self.is_l_d_a_p)
        writer.write_object_value("manager", self.manager)
        writer.write_collection_of_object_values("members", self.members)
        writer.write_int_value("membersCount", self.members_count)
        writer.write_str_value("name", self.name)
        writer.write_uuid_value("parent", self.parent)
        writer.write_bool_value("shared", self.shared)
    

