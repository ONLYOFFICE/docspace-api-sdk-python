from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .webhooks_config_dto import WebhooksConfigDto

@dataclass
class WebhooksConfigWithStatusDto(Parsable):
    # The configs property
    configs: Optional[WebhooksConfigDto] = None
    # Status
    status: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WebhooksConfigWithStatusDto:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WebhooksConfigWithStatusDto
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WebhooksConfigWithStatusDto()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .webhooks_config_dto import WebhooksConfigDto

        from .webhooks_config_dto import WebhooksConfigDto

        fields: Dict[str, Callable[[Any], None]] = {
            "configs": lambda n : setattr(self, 'configs', n.get_object_value(WebhooksConfigDto)),
            "status": lambda n : setattr(self, 'status', n.get_int_value()),
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
        from .webhooks_config_dto import WebhooksConfigDto

        writer.write_object_value("configs", self.configs)
        writer.write_int_value("status", self.status)
    

