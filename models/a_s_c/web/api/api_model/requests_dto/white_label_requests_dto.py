from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....api.collections.item_key_value_pair.system.string.a_s_c.web.api.api_model.requests_dto.logo_requests_dto import LogoRequestsDto

@dataclass
class WhiteLabelRequestsDto(Parsable):
    """
    Request parameters for white label settings
    """
    # Tenant IDs with their logos (light or dark)
    logo: Optional[List[LogoRequestsDto]] = None
    # Logo text
    logo_text: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WhiteLabelRequestsDto:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WhiteLabelRequestsDto
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WhiteLabelRequestsDto()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .....api.collections.item_key_value_pair.system.string.a_s_c.web.api.api_model.requests_dto.logo_requests_dto import LogoRequestsDto

        from .....api.collections.item_key_value_pair.system.string.a_s_c.web.api.api_model.requests_dto.logo_requests_dto import LogoRequestsDto

        fields: Dict[str, Callable[[Any], None]] = {
            "logo": lambda n : setattr(self, 'logo', n.get_collection_of_object_values(LogoRequestsDto)),
            "logoText": lambda n : setattr(self, 'logo_text', n.get_str_value()),
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
        from .....api.collections.item_key_value_pair.system.string.a_s_c.web.api.api_model.requests_dto.logo_requests_dto import LogoRequestsDto

        writer.write_collection_of_object_values("logo", self.logo)
        writer.write_str_value("logoText", self.logo_text)
    

