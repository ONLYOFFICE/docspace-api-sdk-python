from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class SsoIdpCertificateAdvanced(Parsable):
    # Decryption algorithm
    decrypt_algorithm: Optional[str] = None
    # Specifies if the assertions will be decrypted or not
    decrypt_assertions: Optional[bool] = None
    # Verification algorithm
    verify_algorithm: Optional[str] = None
    # Specifies if the signatures of the SAML authentication responses sent to SP will be verified or not
    verify_auth_responses_sign: Optional[bool] = None
    # Specifies if the signatures of the SAML logout requests sent to SP will be verified or not
    verify_logout_requests_sign: Optional[bool] = None
    # Specifies if the signatures of the SAML logout responses sent to SP will be verified or not
    verify_logout_responses_sign: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SsoIdpCertificateAdvanced:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SsoIdpCertificateAdvanced
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SsoIdpCertificateAdvanced()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "decryptAlgorithm": lambda n : setattr(self, 'decrypt_algorithm', n.get_str_value()),
            "decryptAssertions": lambda n : setattr(self, 'decrypt_assertions', n.get_bool_value()),
            "verifyAlgorithm": lambda n : setattr(self, 'verify_algorithm', n.get_str_value()),
            "verifyAuthResponsesSign": lambda n : setattr(self, 'verify_auth_responses_sign', n.get_bool_value()),
            "verifyLogoutRequestsSign": lambda n : setattr(self, 'verify_logout_requests_sign', n.get_bool_value()),
            "verifyLogoutResponsesSign": lambda n : setattr(self, 'verify_logout_responses_sign', n.get_bool_value()),
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
        writer.write_bool_value("decryptAssertions", self.decrypt_assertions)
        writer.write_str_value("verifyAlgorithm", self.verify_algorithm)
        writer.write_bool_value("verifyAuthResponsesSign", self.verify_auth_responses_sign)
        writer.write_bool_value("verifyLogoutRequestsSign", self.verify_logout_requests_sign)
        writer.write_bool_value("verifyLogoutResponsesSign", self.verify_logout_responses_sign)
    

