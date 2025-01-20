from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

@dataclass
class TenantDto(Parsable):
    # Affiliate ID
    affiliate_id: Optional[str] = None
    # Specifies if the calls are available for this tenant or not
    calls: Optional[bool] = None
    # Campaign
    campaign: Optional[str] = None
    # Creation date and time
    creation_date_time: Optional[datetime.datetime] = None
    # Hosted region
    hosted_region: Optional[str] = None
    # [0 - Other, 1 - Accounting, 2 - Advertising marketing PR, 3 - Banking, 4 - Consulting, 5 - Design, 6 - Education, 7 - Environment, 8 - Financial services, 9 - Health care, 10 - IT, 11 - Legal, 12 - Manufacturing, 13 - Public sector, 14 - Publishing, 15 - Retail sales, 16 - Telecommunications]
    industry: Optional[int] = None
    # Language
    language: Optional[str] = None
    # Last modified date
    last_modified: Optional[datetime.datetime] = None
    # Mapped domain
    mapped_domain: Optional[str] = None
    # Name
    name: Optional[str] = None
    # Owner ID
    owner_id: Optional[UUID] = None
    # Payment ID
    payment_id: Optional[str] = None
    # Specifies if the ONLYOFFICE newsletter is allowed or not
    spam: Optional[bool] = None
    # [0 - Active, 1 - Suspended, 2 - Remove pending, 3 - Transfering, 4 - Restoring, 5 - Migrating, 6 - Encryption]
    status: Optional[int] = None
    # The date and time when the tenant status was changed
    status_change_date: Optional[datetime.datetime] = None
    # Tenant alias
    tenant_alias: Optional[str] = None
    # Tenant ID
    tenant_id: Optional[int] = None
    # Time zone
    time_zone: Optional[str] = None
    # List of trusted domains
    trusted_domains: Optional[List[str]] = None
    # Trusted domains in the string format
    trusted_domains_raw: Optional[str] = None
    # [0 - None, 1 - Custom, 2 - All]
    trusted_domains_type: Optional[int] = None
    # Version
    version: Optional[int] = None
    # The date and time when the tenant version was changed
    version_changed: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TenantDto:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TenantDto
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TenantDto()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "affiliateId": lambda n : setattr(self, 'affiliate_id', n.get_str_value()),
            "calls": lambda n : setattr(self, 'calls', n.get_bool_value()),
            "campaign": lambda n : setattr(self, 'campaign', n.get_str_value()),
            "creationDateTime": lambda n : setattr(self, 'creation_date_time', n.get_datetime_value()),
            "hostedRegion": lambda n : setattr(self, 'hosted_region', n.get_str_value()),
            "industry": lambda n : setattr(self, 'industry', n.get_int_value()),
            "language": lambda n : setattr(self, 'language', n.get_str_value()),
            "lastModified": lambda n : setattr(self, 'last_modified', n.get_datetime_value()),
            "mappedDomain": lambda n : setattr(self, 'mapped_domain', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "ownerId": lambda n : setattr(self, 'owner_id', n.get_uuid_value()),
            "paymentId": lambda n : setattr(self, 'payment_id', n.get_str_value()),
            "spam": lambda n : setattr(self, 'spam', n.get_bool_value()),
            "status": lambda n : setattr(self, 'status', n.get_int_value()),
            "statusChangeDate": lambda n : setattr(self, 'status_change_date', n.get_datetime_value()),
            "tenantAlias": lambda n : setattr(self, 'tenant_alias', n.get_str_value()),
            "tenantId": lambda n : setattr(self, 'tenant_id', n.get_int_value()),
            "timeZone": lambda n : setattr(self, 'time_zone', n.get_str_value()),
            "trustedDomains": lambda n : setattr(self, 'trusted_domains', n.get_collection_of_primitive_values(str)),
            "trustedDomainsRaw": lambda n : setattr(self, 'trusted_domains_raw', n.get_str_value()),
            "trustedDomainsType": lambda n : setattr(self, 'trusted_domains_type', n.get_int_value()),
            "version": lambda n : setattr(self, 'version', n.get_int_value()),
            "versionChanged": lambda n : setattr(self, 'version_changed', n.get_datetime_value()),
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
        writer.write_bool_value("calls", self.calls)
        writer.write_str_value("campaign", self.campaign)
        writer.write_str_value("hostedRegion", self.hosted_region)
        writer.write_int_value("industry", self.industry)
        writer.write_str_value("language", self.language)
        writer.write_datetime_value("lastModified", self.last_modified)
        writer.write_str_value("mappedDomain", self.mapped_domain)
        writer.write_str_value("name", self.name)
        writer.write_uuid_value("ownerId", self.owner_id)
        writer.write_str_value("paymentId", self.payment_id)
        writer.write_bool_value("spam", self.spam)
        writer.write_int_value("status", self.status)
        writer.write_str_value("tenantAlias", self.tenant_alias)
        writer.write_str_value("timeZone", self.time_zone)
        writer.write_collection_of_primitive_values("trustedDomains", self.trusted_domains)
        writer.write_str_value("trustedDomainsRaw", self.trusted_domains_raw)
        writer.write_int_value("trustedDomainsType", self.trusted_domains_type)
        writer.write_int_value("version", self.version)
        writer.write_datetime_value("versionChanged", self.version_changed)
    

