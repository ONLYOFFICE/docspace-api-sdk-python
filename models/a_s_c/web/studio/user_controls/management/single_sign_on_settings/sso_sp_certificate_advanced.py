from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class SsoSpCertificateAdvanced(Parsable):
    # Decryption algorithm
    decrypt_algorithm: Optional[str] = None
    # Encryption algorithm
    encrypt_algorithm: Optional[str] = None
    # Specifies if the assertions will be encrypted or not
    encrypt_assertions: Optional[bool] = None
    # Specifies if SP will sign the SAML authentication requests sent to IdP or not
    sign_auth_requests: Optional[bool] = None
    # Specifies if SP will sign the SAML logout requests sent to IdP or not
    sign_logout_requests: Optional[bool] = None
    # Specifies if sign the SAML logout responses sent to IdP or not
    sign_logout_responses: Optional[bool] = None
    # Signing algorithm
    signing_algorithm: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SsoSpCertificateAdvanced:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SsoSpCertificateAdvanced
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SsoSpCertificateAdvanced()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "decryptAlgorithm": lambda n : setattr(self, 'decrypt_algorithm', n.get_str_value()),
            "encryptAlgorithm": lambda n : setattr(self, 'encrypt_algorithm', n.get_str_value()),
            "encryptAssertions": lambda n : setattr(self, 'encrypt_assertions', n.get_bool_value()),
            "signAuthRequests": lambda n : setattr(self, 'sign_auth_requests', n.get_bool_value()),
            "signLogoutRequests": lambda n : setattr(self, 'sign_logout_requests', n.get_bool_value()),
            "signLogoutResponses": lambda n : setattr(self, 'sign_logout_responses', n.get_bool_value()),
            "signingAlgorithm": lambda n : setattr(self, 'signing_algorithm', n.get_str_value()),
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
        writer.write_str_value("decryptAlgorithm", self.decrypt_algorithm)
        writer.write_str_value("encryptAlgorithm", self.encrypt_algorithm)
        writer.write_bool_value("encryptAssertions", self.encrypt_assertions)
        writer.write_bool_value("signAuthRequests", self.sign_auth_requests)
        writer.write_bool_value("signLogoutRequests", self.sign_logout_requests)
        writer.write_bool_value("signLogoutResponses", self.sign_logout_responses)
        writer.write_str_value("signingAlgorithm", self.signing_algorithm)
    

