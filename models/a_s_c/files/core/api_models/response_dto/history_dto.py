from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....api.core.api_date_time import ApiDateTime
    from .....web.api.models.employee_dto import EmployeeDto
    from ...core.entries.history_action import HistoryAction
    from ...core.entries.history_data import HistoryData

@dataclass
class HistoryDto(Parsable):
    # The action property
    action: Optional[HistoryAction] = None
    # The data property
    data: Optional[HistoryData] = None
    # The date property
    date: Optional[ApiDateTime] = None
    # The initiator property
    initiator: Optional[EmployeeDto] = None
    # Related
    related: Optional[List[HistoryDto]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> HistoryDto:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: HistoryDto
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return HistoryDto()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .....api.core.api_date_time import ApiDateTime
        from .....web.api.models.employee_dto import EmployeeDto
        from ...core.entries.history_action import HistoryAction
        from ...core.entries.history_data import HistoryData

        from .....api.core.api_date_time import ApiDateTime
        from .....web.api.models.employee_dto import EmployeeDto
        from ...core.entries.history_action import HistoryAction
        from ...core.entries.history_data import HistoryData

        fields: Dict[str, Callable[[Any], None]] = {
            "action": lambda n : setattr(self, 'action', n.get_object_value(HistoryAction)),
            "data": lambda n : setattr(self, 'data', n.get_object_value(HistoryData)),
            "date": lambda n : setattr(self, 'date', n.get_object_value(ApiDateTime)),
            "initiator": lambda n : setattr(self, 'initiator', n.get_object_value(EmployeeDto)),
            "related": lambda n : setattr(self, 'related', n.get_collection_of_object_values(HistoryDto)),
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
        from .....api.core.api_date_time import ApiDateTime
        from .....web.api.models.employee_dto import EmployeeDto
        from ...core.entries.history_action import HistoryAction
        from ...core.entries.history_data import HistoryData

        writer.write_object_value("action", self.action)
        writer.write_object_value("data", self.data)
        writer.write_object_value("date", self.date)
        writer.write_object_value("initiator", self.initiator)
        writer.write_collection_of_object_values("related", self.related)
    

