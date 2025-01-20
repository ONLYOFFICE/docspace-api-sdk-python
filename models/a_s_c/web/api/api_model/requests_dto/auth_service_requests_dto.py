from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ....studio.user_controls.management.auth_key import AuthKey

@dataclass
class AuthServiceRequestsDto(Parsable):
    """
    Request parameters for authorization service
    """
    # Specifies if the authentication service can be set or not
    can_set: Optional[bool] = None
    # Description
    description: Optional[str] = None
    # Instruction
    instruction: Optional[str] = None
    # Name
    name: Optional[str] = None
    # List of authorization keys
    props: Optional[List[AuthKey]] = None
    # Title
    title: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AuthServiceRequestsDto:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AuthServiceRequestsDto
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AuthServiceRequestsDto()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ....studio.user_controls.management.auth_key import AuthKey

        from ....studio.user_controls.management.auth_key import AuthKey

        fields: Dict[str, Callable[[Any], None]] = {
            "canSet": lambda n : setattr(self, 'can_set', n.get_bool_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "instruction": lambda n : setattr(self, 'instruction', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "props": lambda n : setattr(self, 'props', n.get_collection_of_object_values(AuthKey)),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
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
        from ....studio.user_controls.management.auth_key import AuthKey

        writer.write_bool_value("canSet", self.can_set)
        writer.write_str_value("description", self.description)
        writer.write_str_value("instruction", self.instruction)
        writer.write_str_value("name", self.name)
        writer.write_collection_of_object_values("props", self.props)
        writer.write_str_value("title", self.title)
    

