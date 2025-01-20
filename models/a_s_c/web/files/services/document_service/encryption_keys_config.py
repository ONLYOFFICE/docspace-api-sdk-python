from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class EncryptionKeysConfig(Parsable):
    # Crypto engine id
    crypto_engine_id: Optional[str] = None
    # Private key enc
    private_key_enc: Optional[str] = None
    # Public key
    public_key: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EncryptionKeysConfig:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EncryptionKeysConfig
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EncryptionKeysConfig()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "cryptoEngineId": lambda n : setattr(self, 'crypto_engine_id', n.get_str_value()),
            "privateKeyEnc": lambda n : setattr(self, 'private_key_enc', n.get_str_value()),
            "publicKey": lambda n : setattr(self, 'public_key', n.get_str_value()),
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
        writer.write_str_value("privateKeyEnc", self.private_key_enc)
        writer.write_str_value("publicKey", self.public_key)
    

