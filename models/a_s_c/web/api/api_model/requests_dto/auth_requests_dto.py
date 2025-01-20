from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .confirm_data import ConfirmData

@dataclass
class AuthRequestsDto(Parsable):
    """
    Authentication request parameters
    """
    # Provider access token
    access_token: Optional[str] = None
    # Two-factor authentication code
    code: Optional[str] = None
    # Code for getting a token
    code_o_auth: Optional[str] = None
    # The confirmData property
    confirm_data: Optional[ConfirmData] = None
    # Culture
    culture: Optional[str] = None
    # Password
    password: Optional[str] = None
    # Password hash
    password_hash: Optional[str] = None
    # Provider type
    provider: Optional[str] = None
    # reCAPTCHA response
    recaptcha_response: Optional[str] = None
    # [0 - Default, 1 - AndroidV2, 2 - iOSV2, 3 - hCaptcha]
    recaptcha_type: Optional[int] = None
    # Serialized user profile
    serialized_profile: Optional[str] = None
    # Session based authentication or not
    session: Optional[bool] = None
    # Username / email
    user_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AuthRequestsDto:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AuthRequestsDto
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AuthRequestsDto()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .confirm_data import ConfirmData

        from .confirm_data import ConfirmData

        fields: Dict[str, Callable[[Any], None]] = {
            "accessToken": lambda n : setattr(self, 'access_token', n.get_str_value()),
            "code": lambda n : setattr(self, 'code', n.get_str_value()),
            "codeOAuth": lambda n : setattr(self, 'code_o_auth', n.get_str_value()),
            "confirmData": lambda n : setattr(self, 'confirm_data', n.get_object_value(ConfirmData)),
            "culture": lambda n : setattr(self, 'culture', n.get_str_value()),
            "password": lambda n : setattr(self, 'password', n.get_str_value()),
            "passwordHash": lambda n : setattr(self, 'password_hash', n.get_str_value()),
            "provider": lambda n : setattr(self, 'provider', n.get_str_value()),
            "recaptchaResponse": lambda n : setattr(self, 'recaptcha_response', n.get_str_value()),
            "recaptchaType": lambda n : setattr(self, 'recaptcha_type', n.get_int_value()),
            "serializedProfile": lambda n : setattr(self, 'serialized_profile', n.get_str_value()),
            "session": lambda n : setattr(self, 'session', n.get_bool_value()),
            "userName": lambda n : setattr(self, 'user_name', n.get_str_value()),
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
        from .confirm_data import ConfirmData

        writer.write_str_value("accessToken", self.access_token)
        writer.write_str_value("code", self.code)
        writer.write_str_value("codeOAuth", self.code_o_auth)
        writer.write_object_value("confirmData", self.confirm_data)
        writer.write_str_value("culture", self.culture)
        writer.write_str_value("password", self.password)
        writer.write_str_value("passwordHash", self.password_hash)
        writer.write_str_value("provider", self.provider)
        writer.write_str_value("recaptchaResponse", self.recaptcha_response)
        writer.write_int_value("recaptchaType", self.recaptcha_type)
        writer.write_str_value("serializedProfile", self.serialized_profile)
        writer.write_bool_value("session", self.session)
        writer.write_str_value("userName", self.user_name)
    

