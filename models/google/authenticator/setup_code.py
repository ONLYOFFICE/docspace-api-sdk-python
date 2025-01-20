from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class SetupCode(Parsable):
    # The account property
    account: Optional[str] = None
    # The manualEntryKey property
    manual_entry_key: Optional[str] = None
    # The qrCodeSetupImageUrl property
    qr_code_setup_image_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SetupCode:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SetupCode
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SetupCode()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "account": lambda n : setattr(self, 'account', n.get_str_value()),
            "manualEntryKey": lambda n : setattr(self, 'manual_entry_key', n.get_str_value()),
            "qrCodeSetupImageUrl": lambda n : setattr(self, 'qr_code_setup_image_url', n.get_str_value()),
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
    

