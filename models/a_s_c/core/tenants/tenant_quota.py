from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class TenantQuota(Parsable):
    # Specifies if the audit trail is available or not
    audit: Optional[bool] = None
    # Specifies if the automatic Backup&Restore feature is available or not
    auto_backup_restore: Optional[bool] = None
    # Specifies if the branding settings are available or not
    branding: Optional[bool] = None
    # Specifies if the content search is available or not
    content_search: Optional[bool] = None
    # Number of rooms
    count_room: Optional[int] = None
    # Number of portal room administrators
    count_room_admin: Optional[int] = None
    # Number of portal users
    count_user: Optional[int] = None
    # Specifies if the custom domain URL is available or not
    custom: Optional[bool] = None
    # Specifies if the customization settings are available or not
    customization: Optional[bool] = None
    # Specifies if this tenant quota is Docs edition or not
    docs_edition: Optional[bool] = None
    # Tenant quota features
    features: Optional[str] = None
    # Specifies if the tenant quota is free or not
    free: Optional[bool] = None
    # Specifies if the LDAP settings are available or not
    ldap: Optional[bool] = None
    # Specifies if the license is lifetime or not
    lifetime: Optional[bool] = None
    # Maximum file size
    max_file_size: Optional[int] = None
    # Maximum total size
    max_total_size: Optional[int] = None
    # Name
    name: Optional[str] = None
    # Specifies if the tenant quota is nonprofit or not
    non_profit: Optional[bool] = None
    # Specifies if Oauth is available or not
    oauth: Optional[bool] = None
    # Price
    price: Optional[float] = None
    # Price currency symbol
    price_currency_symbol: Optional[str] = None
    # Product ID
    product_id: Optional[str] = None
    # Specifies if the SSO settings are available or not
    sso: Optional[bool] = None
    # Specifies if the statistic settings are available or not
    statistic: Optional[bool] = None
    # Tenant ID
    tenant_id: Optional[int] = None
    # Specifies if the third-party accounts linking is available or not
    third_party: Optional[bool] = None
    # Specifies if the tenant quota is trial or not
    trial: Optional[bool] = None
    # Specifies if the tenant quota is updated or not
    update: Optional[bool] = None
    # Number of room users
    users_in_room: Optional[int] = None
    # Specifies if the tenant quota is visible or not
    visible: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TenantQuota:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TenantQuota
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TenantQuota()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "audit": lambda n : setattr(self, 'audit', n.get_bool_value()),
            "autoBackupRestore": lambda n : setattr(self, 'auto_backup_restore', n.get_bool_value()),
            "branding": lambda n : setattr(self, 'branding', n.get_bool_value()),
            "contentSearch": lambda n : setattr(self, 'content_search', n.get_bool_value()),
            "countRoom": lambda n : setattr(self, 'count_room', n.get_int_value()),
            "countRoomAdmin": lambda n : setattr(self, 'count_room_admin', n.get_int_value()),
            "countUser": lambda n : setattr(self, 'count_user', n.get_int_value()),
            "custom": lambda n : setattr(self, 'custom', n.get_bool_value()),
            "customization": lambda n : setattr(self, 'customization', n.get_bool_value()),
            "docsEdition": lambda n : setattr(self, 'docs_edition', n.get_bool_value()),
            "features": lambda n : setattr(self, 'features', n.get_str_value()),
            "free": lambda n : setattr(self, 'free', n.get_bool_value()),
            "ldap": lambda n : setattr(self, 'ldap', n.get_bool_value()),
            "lifetime": lambda n : setattr(self, 'lifetime', n.get_bool_value()),
            "maxFileSize": lambda n : setattr(self, 'max_file_size', n.get_int_value()),
            "maxTotalSize": lambda n : setattr(self, 'max_total_size', n.get_int_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "nonProfit": lambda n : setattr(self, 'non_profit', n.get_bool_value()),
            "oauth": lambda n : setattr(self, 'oauth', n.get_bool_value()),
            "price": lambda n : setattr(self, 'price', n.get_float_value()),
            "priceCurrencySymbol": lambda n : setattr(self, 'price_currency_symbol', n.get_str_value()),
            "productId": lambda n : setattr(self, 'product_id', n.get_str_value()),
            "sso": lambda n : setattr(self, 'sso', n.get_bool_value()),
            "statistic": lambda n : setattr(self, 'statistic', n.get_bool_value()),
            "tenantId": lambda n : setattr(self, 'tenant_id', n.get_int_value()),
            "thirdParty": lambda n : setattr(self, 'third_party', n.get_bool_value()),
            "trial": lambda n : setattr(self, 'trial', n.get_bool_value()),
            "update": lambda n : setattr(self, 'update', n.get_bool_value()),
            "usersInRoom": lambda n : setattr(self, 'users_in_room', n.get_int_value()),
            "visible": lambda n : setattr(self, 'visible', n.get_bool_value()),
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
        writer.write_bool_value("audit", self.audit)
        writer.write_bool_value("autoBackupRestore", self.auto_backup_restore)
        writer.write_bool_value("branding", self.branding)
        writer.write_bool_value("contentSearch", self.content_search)
        writer.write_int_value("countRoom", self.count_room)
        writer.write_int_value("countRoomAdmin", self.count_room_admin)
        writer.write_int_value("countUser", self.count_user)
        writer.write_bool_value("custom", self.custom)
        writer.write_bool_value("customization", self.customization)
        writer.write_bool_value("docsEdition", self.docs_edition)
        writer.write_str_value("features", self.features)
        writer.write_bool_value("free", self.free)
        writer.write_bool_value("ldap", self.ldap)
        writer.write_bool_value("lifetime", self.lifetime)
        writer.write_int_value("maxFileSize", self.max_file_size)
        writer.write_int_value("maxTotalSize", self.max_total_size)
        writer.write_str_value("name", self.name)
        writer.write_bool_value("nonProfit", self.non_profit)
        writer.write_bool_value("oauth", self.oauth)
        writer.write_float_value("price", self.price)
        writer.write_str_value("priceCurrencySymbol", self.price_currency_symbol)
        writer.write_str_value("productId", self.product_id)
        writer.write_bool_value("sso", self.sso)
        writer.write_bool_value("statistic", self.statistic)
        writer.write_int_value("tenantId", self.tenant_id)
        writer.write_bool_value("thirdParty", self.third_party)
        writer.write_bool_value("trial", self.trial)
        writer.write_bool_value("update", self.update)
        writer.write_int_value("usersInRoom", self.users_in_room)
        writer.write_bool_value("visible", self.visible)
    

