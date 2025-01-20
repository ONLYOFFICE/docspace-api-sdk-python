from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class FirebaseDto(Parsable):
    # API key
    api_key: Optional[str] = None
    # Application ID
    app_id: Optional[str] = None
    # Authentication domain
    auth_domain: Optional[str] = None
    # Database URL
    database_u_r_l: Optional[str] = None
    # Measurement ID
    measurement_id: Optional[str] = None
    # Message sender ID
    messaging_sender_id: Optional[str] = None
    # Project ID
    project_id: Optional[str] = None
    # Storage bucket
    storage_bucket: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> FirebaseDto:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FirebaseDto
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return FirebaseDto()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "apiKey": lambda n : setattr(self, 'api_key', n.get_str_value()),
            "appId": lambda n : setattr(self, 'app_id', n.get_str_value()),
            "authDomain": lambda n : setattr(self, 'auth_domain', n.get_str_value()),
            "databaseURL": lambda n : setattr(self, 'database_u_r_l', n.get_str_value()),
            "measurementId": lambda n : setattr(self, 'measurement_id', n.get_str_value()),
            "messagingSenderId": lambda n : setattr(self, 'messaging_sender_id', n.get_str_value()),
            "projectId": lambda n : setattr(self, 'project_id', n.get_str_value()),
            "storageBucket": lambda n : setattr(self, 'storage_bucket', n.get_str_value()),
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
        writer.write_str_value("apiKey", self.api_key)
        writer.write_str_value("appId", self.app_id)
        writer.write_str_value("authDomain", self.auth_domain)
        writer.write_str_value("databaseURL", self.database_u_r_l)
        writer.write_str_value("measurementId", self.measurement_id)
        writer.write_str_value("messagingSenderId", self.messaging_sender_id)
        writer.write_str_value("projectId", self.project_id)
        writer.write_str_value("storageBucket", self.storage_bucket)
    

