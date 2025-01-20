from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class WizardRequestsDto(Parsable):
    """
    Wizard settings request parameters
    """
    # AMI ID
    ami_id: Optional[str] = None
    # Email
    email: Optional[str] = None
    # Language
    lng: Optional[str] = None
    # Password hash
    password_hash: Optional[str] = None
    # Subscribed from the site or not
    subscribe_from_site: Optional[bool] = None
    # Time zone
    time_zone: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WizardRequestsDto:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WizardRequestsDto
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WizardRequestsDto()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "amiId": lambda n : setattr(self, 'ami_id', n.get_str_value()),
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "lng": lambda n : setattr(self, 'lng', n.get_str_value()),
            "passwordHash": lambda n : setattr(self, 'password_hash', n.get_str_value()),
            "subscribeFromSite": lambda n : setattr(self, 'subscribe_from_site', n.get_bool_value()),
            "timeZone": lambda n : setattr(self, 'time_zone', n.get_str_value()),
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
        writer.write_str_value("amiId", self.ami_id)
        writer.write_str_value("email", self.email)
        writer.write_str_value("lng", self.lng)
        writer.write_str_value("passwordHash", self.password_hash)
        writer.write_bool_value("subscribeFromSite", self.subscribe_from_site)
        writer.write_str_value("timeZone", self.time_zone)
    

