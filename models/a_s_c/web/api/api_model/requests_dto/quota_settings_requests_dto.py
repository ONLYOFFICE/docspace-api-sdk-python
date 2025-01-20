from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .quota_settings_requests_dto_default_quota import QuotaSettingsRequestsDto_defaultQuota

@dataclass
class QuotaSettingsRequestsDto(Parsable):
    """
    Request parameters for the user quota settings
    """
    # Default quota value
    default_quota: Optional[QuotaSettingsRequestsDto_defaultQuota] = None
    # Specifies if the quota settings are enabled or not
    enable_quota: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> QuotaSettingsRequestsDto:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: QuotaSettingsRequestsDto
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return QuotaSettingsRequestsDto()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .quota_settings_requests_dto_default_quota import QuotaSettingsRequestsDto_defaultQuota

        from .quota_settings_requests_dto_default_quota import QuotaSettingsRequestsDto_defaultQuota

        fields: Dict[str, Callable[[Any], None]] = {
            "defaultQuota": lambda n : setattr(self, 'default_quota', n.get_object_value(QuotaSettingsRequestsDto_defaultQuota)),
            "enableQuota": lambda n : setattr(self, 'enable_quota', n.get_bool_value()),
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
        from .quota_settings_requests_dto_default_quota import QuotaSettingsRequestsDto_defaultQuota

        writer.write_object_value("defaultQuota", self.default_quota)
        writer.write_bool_value("enableQuota", self.enable_quota)
    

