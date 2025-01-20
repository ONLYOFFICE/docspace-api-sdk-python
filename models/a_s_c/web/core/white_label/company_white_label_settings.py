from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class CompanyWhiteLabelSettings(Parsable):
    # Address
    address: Optional[str] = None
    # Company name
    company_name: Optional[str] = None
    # Email address
    email: Optional[str] = None
    # Specifies if a company is a licensor or not
    is_licensor: Optional[bool] = None
    # Phone
    phone: Optional[str] = None
    # Site
    site: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CompanyWhiteLabelSettings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CompanyWhiteLabelSettings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CompanyWhiteLabelSettings()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "address": lambda n : setattr(self, 'address', n.get_str_value()),
            "companyName": lambda n : setattr(self, 'company_name', n.get_str_value()),
            "email": lambda n : setattr(self, 'email', n.get_str_value()),
            "IsLicensor": lambda n : setattr(self, 'is_licensor', n.get_bool_value()),
            "phone": lambda n : setattr(self, 'phone', n.get_str_value()),
            "site": lambda n : setattr(self, 'site', n.get_str_value()),
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
        writer.write_str_value("address", self.address)
        writer.write_str_value("companyName", self.company_name)
        writer.write_str_value("email", self.email)
        writer.write_bool_value("IsLicensor", self.is_licensor)
        writer.write_str_value("phone", self.phone)
        writer.write_str_value("site", self.site)
    

