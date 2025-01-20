from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .custom_attribute_typed_argument import CustomAttributeTypedArgument
    from .member_info import MemberInfo

@dataclass
class CustomAttributeNamedArgument(Parsable):
    # The isField property
    is_field: Optional[bool] = None
    # The memberInfo property
    member_info: Optional[MemberInfo] = None
    # The memberName property
    member_name: Optional[str] = None
    # The typedValue property
    typed_value: Optional[CustomAttributeTypedArgument] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CustomAttributeNamedArgument:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CustomAttributeNamedArgument
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CustomAttributeNamedArgument()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .custom_attribute_typed_argument import CustomAttributeTypedArgument
        from .member_info import MemberInfo

        from .custom_attribute_typed_argument import CustomAttributeTypedArgument
        from .member_info import MemberInfo

        fields: Dict[str, Callable[[Any], None]] = {
            "isField": lambda n : setattr(self, 'is_field', n.get_bool_value()),
            "memberInfo": lambda n : setattr(self, 'member_info', n.get_object_value(MemberInfo)),
            "memberName": lambda n : setattr(self, 'member_name', n.get_str_value()),
            "typedValue": lambda n : setattr(self, 'typed_value', n.get_object_value(CustomAttributeTypedArgument)),
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
        from .custom_attribute_typed_argument import CustomAttributeTypedArgument
        from .member_info import MemberInfo

        writer.write_object_value("memberInfo", self.member_info)
        writer.write_object_value("typedValue", self.typed_value)
    

