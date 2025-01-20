from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .......web.api.models.employee_full_dto import EmployeeFullDto
    from ...file_dto.system.int32 import Int32

@dataclass
class Int32(Parsable):
    # The completedForm property
    completed_form: Optional[Int32] = None
    # Form number
    form_number: Optional[int] = None
    # Is room member
    is_room_member: Optional[bool] = None
    # The manager property
    manager: Optional[EmployeeFullDto] = None
    # The originalForm property
    original_form: Optional[Int32] = None
    # Room Id
    room_id: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Int32:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Int32
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Int32()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .......web.api.models.employee_full_dto import EmployeeFullDto
        from ...file_dto.system.int32 import Int32

        from .......web.api.models.employee_full_dto import EmployeeFullDto
        from ...file_dto.system.int32 import Int32

        fields: Dict[str, Callable[[Any], None]] = {
            "completedForm": lambda n : setattr(self, 'completed_form', n.get_object_value(Int32)),
            "formNumber": lambda n : setattr(self, 'form_number', n.get_int_value()),
            "isRoomMember": lambda n : setattr(self, 'is_room_member', n.get_bool_value()),
            "manager": lambda n : setattr(self, 'manager', n.get_object_value(EmployeeFullDto)),
            "originalForm": lambda n : setattr(self, 'original_form', n.get_object_value(Int32)),
            "roomId": lambda n : setattr(self, 'room_id', n.get_int_value()),
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
        from .......web.api.models.employee_full_dto import EmployeeFullDto
        from ...file_dto.system.int32 import Int32

        writer.write_int_value("completedForm", self.completed_form)
        writer.write_int_value("formNumber", self.form_number)
        writer.write_bool_value("isRoomMember", self.is_room_member)
        writer.write_object_value("manager", self.manager)
        writer.write_int_value("originalForm", self.original_form)
        writer.write_int_value("roomId", self.room_id)
    

