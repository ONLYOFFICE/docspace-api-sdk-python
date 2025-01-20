from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .model.db_tenant import DbTenant

@dataclass
class FireBaseUser(Parsable):
    # Application
    application: Optional[str] = None
    # Firebase device token
    firebase_device_token: Optional[str] = None
    # ID
    id: Optional[int] = None
    # Specifies if the user is subscribed to the push notifications or not
    is_subscribed: Optional[bool] = None
    # The tenant property
    tenant: Optional[DbTenant] = None
    # Tenant ID
    tenant_id: Optional[int] = None
    # User ID
    user_id: Optional[UUID] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> FireBaseUser:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FireBaseUser
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return FireBaseUser()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .model.db_tenant import DbTenant

        from .model.db_tenant import DbTenant

        fields: Dict[str, Callable[[Any], None]] = {
            "application": lambda n : setattr(self, 'application', n.get_str_value()),
            "firebaseDeviceToken": lambda n : setattr(self, 'firebase_device_token', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "isSubscribed": lambda n : setattr(self, 'is_subscribed', n.get_bool_value()),
            "tenant": lambda n : setattr(self, 'tenant', n.get_object_value(DbTenant)),
            "tenantId": lambda n : setattr(self, 'tenant_id', n.get_int_value()),
            "userId": lambda n : setattr(self, 'user_id', n.get_uuid_value()),
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
        from .model.db_tenant import DbTenant

        writer.write_str_value("application", self.application)
        writer.write_str_value("firebaseDeviceToken", self.firebase_device_token)
        writer.write_int_value("id", self.id)
        writer.write_bool_value("isSubscribed", self.is_subscribed)
        writer.write_object_value("tenant", self.tenant)
        writer.write_int_value("tenantId", self.tenant_id)
        writer.write_uuid_value("userId", self.user_id)
    

