from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .quota import Quota

@dataclass
class Tariff(Parsable):
    # Customer ID
    customer_id: Optional[str] = None
    # Delay due date
    delay_due_date: Optional[datetime.datetime] = None
    # Due date
    due_date: Optional[datetime.datetime] = None
    # ID
    id: Optional[int] = None
    # License date
    license_date: Optional[datetime.datetime] = None
    # List of quotas
    quotas: Optional[List[Quota]] = None
    # [0 - Trial, 1 - Paid, 2 - Delay, 3 - Not paid]
    state: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Tariff:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Tariff
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Tariff()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .quota import Quota

        from .quota import Quota

        fields: Dict[str, Callable[[Any], None]] = {
            "customerId": lambda n : setattr(self, 'customer_id', n.get_str_value()),
            "delayDueDate": lambda n : setattr(self, 'delay_due_date', n.get_datetime_value()),
            "dueDate": lambda n : setattr(self, 'due_date', n.get_datetime_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "licenseDate": lambda n : setattr(self, 'license_date', n.get_datetime_value()),
            "quotas": lambda n : setattr(self, 'quotas', n.get_collection_of_object_values(Quota)),
            "state": lambda n : setattr(self, 'state', n.get_int_value()),
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
        from .quota import Quota

        writer.write_str_value("customerId", self.customer_id)
        writer.write_datetime_value("delayDueDate", self.delay_due_date)
        writer.write_datetime_value("dueDate", self.due_date)
        writer.write_int_value("id", self.id)
        writer.write_datetime_value("licenseDate", self.license_date)
        writer.write_collection_of_object_values("quotas", self.quotas)
        writer.write_int_value("state", self.state)
    

