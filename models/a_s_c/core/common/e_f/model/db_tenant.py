from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .db_tenant_partner import DbTenantPartner

@dataclass
class DbTenant(Parsable):
    # Alias
    alias: Optional[str] = None
    # Calls
    calls: Optional[bool] = None
    # Creation date time
    creation_date_time: Optional[datetime.datetime] = None
    # Id
    id: Optional[int] = None
    # [0 - Other, 1 - Accounting, 2 - Advertising marketing PR, 3 - Banking, 4 - Consulting, 5 - Design, 6 - Education, 7 - Environment, 8 - Financial services, 9 - Health care, 10 - IT, 11 - Legal, 12 - Manufacturing, 13 - Public sector, 14 - Publishing, 15 - Retail sales, 16 - Telecommunications]
    industry: Optional[int] = None
    # Language
    language: Optional[str] = None
    # Last modified
    last_modified: Optional[datetime.datetime] = None
    # Mapped domain
    mapped_domain: Optional[str] = None
    # Name
    name: Optional[str] = None
    # Owner id
    owner_id: Optional[UUID] = None
    # The partner property
    partner: Optional[DbTenantPartner] = None
    # Payment id
    payment_id: Optional[str] = None
    # [0 - Active, 1 - Suspended, 2 - Remove pending, 3 - Transfering, 4 - Restoring, 5 - Migrating, 6 - Encryption]
    status: Optional[int] = None
    # Status changed
    status_changed: Optional[datetime.datetime] = None
    # Status changed hack
    status_changed_hack: Optional[datetime.datetime] = None
    # Time zone
    time_zone: Optional[str] = None
    # [0 - None, 1 - Custom, 2 - All]
    trusted_domains_enabled: Optional[int] = None
    # Trusted domains raw
    trusted_domains_raw: Optional[str] = None
    # Version
    version: Optional[int] = None
    # Version_changed
    version_changed: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DbTenant:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DbTenant
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DbTenant()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .db_tenant_partner import DbTenantPartner

        from .db_tenant_partner import DbTenantPartner

        fields: Dict[str, Callable[[Any], None]] = {
            "alias": lambda n : setattr(self, 'alias', n.get_str_value()),
            "calls": lambda n : setattr(self, 'calls', n.get_bool_value()),
            "creationDateTime": lambda n : setattr(self, 'creation_date_time', n.get_datetime_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "industry": lambda n : setattr(self, 'industry', n.get_int_value()),
            "language": lambda n : setattr(self, 'language', n.get_str_value()),
            "lastModified": lambda n : setattr(self, 'last_modified', n.get_datetime_value()),
            "mappedDomain": lambda n : setattr(self, 'mapped_domain', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "ownerId": lambda n : setattr(self, 'owner_id', n.get_uuid_value()),
            "partner": lambda n : setattr(self, 'partner', n.get_object_value(DbTenantPartner)),
            "paymentId": lambda n : setattr(self, 'payment_id', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_int_value()),
            "statusChanged": lambda n : setattr(self, 'status_changed', n.get_datetime_value()),
            "statusChangedHack": lambda n : setattr(self, 'status_changed_hack', n.get_datetime_value()),
            "timeZone": lambda n : setattr(self, 'time_zone', n.get_str_value()),
            "trustedDomainsEnabled": lambda n : setattr(self, 'trusted_domains_enabled', n.get_int_value()),
            "trustedDomainsRaw": lambda n : setattr(self, 'trusted_domains_raw', n.get_str_value()),
            "version": lambda n : setattr(self, 'version', n.get_int_value()),
            "version_Changed": lambda n : setattr(self, 'version_changed', n.get_datetime_value()),
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
        from .db_tenant_partner import DbTenantPartner

        writer.write_str_value("alias", self.alias)
        writer.write_bool_value("calls", self.calls)
        writer.write_datetime_value("creationDateTime", self.creation_date_time)
        writer.write_int_value("id", self.id)
        writer.write_int_value("industry", self.industry)
        writer.write_str_value("language", self.language)
        writer.write_datetime_value("lastModified", self.last_modified)
        writer.write_str_value("mappedDomain", self.mapped_domain)
        writer.write_str_value("name", self.name)
        writer.write_uuid_value("ownerId", self.owner_id)
        writer.write_object_value("partner", self.partner)
        writer.write_str_value("paymentId", self.payment_id)
        writer.write_int_value("status", self.status)
        writer.write_datetime_value("statusChanged", self.status_changed)
        writer.write_datetime_value("statusChangedHack", self.status_changed_hack)
        writer.write_str_value("timeZone", self.time_zone)
        writer.write_int_value("trustedDomainsEnabled", self.trusted_domains_enabled)
        writer.write_str_value("trustedDomainsRaw", self.trusted_domains_raw)
        writer.write_int_value("version", self.version)
        writer.write_datetime_value("version_Changed", self.version_changed)
    

