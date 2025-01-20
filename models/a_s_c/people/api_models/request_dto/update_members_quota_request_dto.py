from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .update_members_quota_request_dto_quota import UpdateMembersQuotaRequestDto_quota

@dataclass
class UpdateMembersQuotaRequestDto(Parsable):
    """
    Request parameters for updating user information
    """
    # Quota
    quota: Optional[UpdateMembersQuotaRequestDto_quota] = None
    # List of user IDs
    user_ids: Optional[List[UUID]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UpdateMembersQuotaRequestDto:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UpdateMembersQuotaRequestDto
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UpdateMembersQuotaRequestDto()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .update_members_quota_request_dto_quota import UpdateMembersQuotaRequestDto_quota

        from .update_members_quota_request_dto_quota import UpdateMembersQuotaRequestDto_quota

        fields: Dict[str, Callable[[Any], None]] = {
            "quota": lambda n : setattr(self, 'quota', n.get_object_value(UpdateMembersQuotaRequestDto_quota)),
            "userIds": lambda n : setattr(self, 'user_ids', n.get_collection_of_primitive_values(UUID)),
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
        from .update_members_quota_request_dto_quota import UpdateMembersQuotaRequestDto_quota

        writer.write_object_value("quota", self.quota)
        writer.write_collection_of_primitive_values("userIds", self.user_ids)
    

