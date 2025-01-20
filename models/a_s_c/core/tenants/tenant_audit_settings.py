from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class TenantAuditSettings(Parsable):
    # Audit trail lifetime
    audit_trail_life_time: Optional[int] = None
    # Login history lifetime
    login_history_life_time: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TenantAuditSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TenantAuditSettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TenantAuditSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "auditTrailLifeTime": lambda n : setattr(self, 'audit_trail_life_time', n.get_int_value()),
            "loginHistoryLifeTime": lambda n : setattr(self, 'login_history_life_time', n.get_int_value()),
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
        writer.write_int_value("auditTrailLifeTime", self.audit_trail_life_time)
        writer.write_int_value("loginHistoryLifeTime", self.login_history_life_time)
    

