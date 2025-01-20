from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class DbTenantPartner(Parsable):
    # Affiliate id
    affiliate_id: Optional[str] = None
    # Campaign
    campaign: Optional[str] = None
    # Partner id
    partner_id: Optional[str] = None
    # Tenant id
    tenant_id: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DbTenantPartner:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DbTenantPartner
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DbTenantPartner()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "affiliateId": lambda n : setattr(self, 'affiliate_id', n.get_str_value()),
            "campaign": lambda n : setattr(self, 'campaign', n.get_str_value()),
            "partnerId": lambda n : setattr(self, 'partner_id', n.get_str_value()),
            "tenantId": lambda n : setattr(self, 'tenant_id', n.get_int_value()),
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
        writer.write_str_value("affiliateId", self.affiliate_id)
        writer.write_str_value("campaign", self.campaign)
        writer.write_str_value("partnerId", self.partner_id)
        writer.write_int_value("tenantId", self.tenant_id)
    

