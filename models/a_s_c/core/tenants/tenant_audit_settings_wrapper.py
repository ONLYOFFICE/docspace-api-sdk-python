from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tenant_audit_settings import TenantAuditSettings

@dataclass
class TenantAuditSettingsWrapper(Parsable):
    """
    Audit trail settings
    """
    # The settings property
    settings: Optional[TenantAuditSettings] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TenantAuditSettingsWrapper:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TenantAuditSettingsWrapper
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TenantAuditSettingsWrapper()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .tenant_audit_settings import TenantAuditSettings

        from .tenant_audit_settings import TenantAuditSettings

        fields: Dict[str, Callable[[Any], None]] = {
            "settings": lambda n : setattr(self, 'settings', n.get_object_value(TenantAuditSettings)),
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
        from .tenant_audit_settings import TenantAuditSettings

        writer.write_object_value("settings", self.settings)
    

