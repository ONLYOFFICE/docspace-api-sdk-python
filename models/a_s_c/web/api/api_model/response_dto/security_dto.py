from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ...models.employee_dto import EmployeeDto
    from ...models.group_summary_dto import GroupSummaryDto

@dataclass
class SecurityDto(Parsable):
    # Specifies if the security settings are enabled or not
    enabled: Optional[bool] = None
    # List of groups with the access to the module
    groups: Optional[List[GroupSummaryDto]] = None
    # Specifies if this module is a subitem or not
    is_sub_item: Optional[bool] = None
    # List of users with the access to the module
    users: Optional[List[EmployeeDto]] = None
    # Module ID
    web_item_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SecurityDto:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SecurityDto
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SecurityDto()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ...models.employee_dto import EmployeeDto
        from ...models.group_summary_dto import GroupSummaryDto

        from ...models.employee_dto import EmployeeDto
        from ...models.group_summary_dto import GroupSummaryDto

        fields: Dict[str, Callable[[Any], None]] = {
            "enabled": lambda n : setattr(self, 'enabled', n.get_bool_value()),
            "groups": lambda n : setattr(self, 'groups', n.get_collection_of_object_values(GroupSummaryDto)),
            "isSubItem": lambda n : setattr(self, 'is_sub_item', n.get_bool_value()),
            "users": lambda n : setattr(self, 'users', n.get_collection_of_object_values(EmployeeDto)),
            "webItemId": lambda n : setattr(self, 'web_item_id', n.get_str_value()),
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
        from ...models.employee_dto import EmployeeDto
        from ...models.group_summary_dto import GroupSummaryDto

        writer.write_bool_value("enabled", self.enabled)
        writer.write_collection_of_object_values("groups", self.groups)
        writer.write_bool_value("isSubItem", self.is_sub_item)
        writer.write_collection_of_object_values("users", self.users)
        writer.write_str_value("webItemId", self.web_item_id)
    

