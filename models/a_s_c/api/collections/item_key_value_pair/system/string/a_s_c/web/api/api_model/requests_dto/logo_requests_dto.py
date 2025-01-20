from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ...........web.api.api_model.requests_dto.logo_requests_dto import LogoRequestsDto

@dataclass
class LogoRequestsDto(Parsable):
    # The key property
    key: Optional[str] = None
    # The value property
    value: Optional[LogoRequestsDto] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LogoRequestsDto:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LogoRequestsDto
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LogoRequestsDto()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ...........web.api.api_model.requests_dto.logo_requests_dto import LogoRequestsDto

        from ...........web.api.api_model.requests_dto.logo_requests_dto import LogoRequestsDto

        fields: Dict[str, Callable[[Any], None]] = {
            "key": lambda n : setattr(self, 'key', n.get_str_value()),
            "value": lambda n : setattr(self, 'value', n.get_object_value(LogoRequestsDto)),
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
        from ...........web.api.api_model.requests_dto.logo_requests_dto import LogoRequestsDto

        writer.write_str_value("key", self.key)
        writer.write_object_value("value", self.value)
    

