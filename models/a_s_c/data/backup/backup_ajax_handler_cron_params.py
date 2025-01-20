from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class BackupAjaxHandler_CronParams(Parsable):
    # The day property
    day: Optional[int] = None
    # The hour property
    hour: Optional[int] = None
    # [0 - Every day, 1 - Every week, 2 - Every month]
    period: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BackupAjaxHandler_CronParams:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BackupAjaxHandler_CronParams
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return BackupAjaxHandler_CronParams()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "day": lambda n : setattr(self, 'day', n.get_int_value()),
            "hour": lambda n : setattr(self, 'hour', n.get_int_value()),
            "period": lambda n : setattr(self, 'period', n.get_int_value()),
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
        writer.write_int_value("day", self.day)
        writer.write_int_value("hour", self.hour)
        writer.write_int_value("period", self.period)
    

