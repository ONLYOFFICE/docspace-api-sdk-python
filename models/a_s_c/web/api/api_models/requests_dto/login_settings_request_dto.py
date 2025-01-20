from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class LoginSettingsRequestDto(Parsable):
    """
    Login settings request parameters
    """
    # Maximum number of the user attempts to log in
    attempt_count: Optional[int] = None
    # The duration of the account suspension for unsuccessful login attempts
    block_time: Optional[int] = None
    # Expected server response time
    check_period: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LoginSettingsRequestDto:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LoginSettingsRequestDto
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LoginSettingsRequestDto()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "attemptCount": lambda n : setattr(self, 'attempt_count', n.get_int_value()),
            "blockTime": lambda n : setattr(self, 'block_time', n.get_int_value()),
            "checkPeriod": lambda n : setattr(self, 'check_period', n.get_int_value()),
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
        writer.write_int_value("attemptCount", self.attempt_count)
        writer.write_int_value("blockTime", self.block_time)
        writer.write_int_value("checkPeriod", self.check_period)
    

