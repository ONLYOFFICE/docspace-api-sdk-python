from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..type import Type
    from .custom_attribute_data import CustomAttributeData
    from .member_info import MemberInfo

@dataclass
class ParameterInfo(Parsable):
    # The attributes property
    attributes: Optional[int] = None
    # The customAttributes property
    custom_attributes: Optional[List[CustomAttributeData]] = None
    # The hasDefaultValue property
    has_default_value: Optional[bool] = None
    # The isIn property
    is_in: Optional[bool] = None
    # The isLcid property
    is_lcid: Optional[bool] = None
    # The isOptional property
    is_optional: Optional[bool] = None
    # The isOut property
    is_out: Optional[bool] = None
    # The isRetval property
    is_retval: Optional[bool] = None
    # The member property
    member: Optional[MemberInfo] = None
    # The metadataToken property
    metadata_token: Optional[int] = None
    # The name property
    name: Optional[str] = None
    # The parameterType property
    parameter_type: Optional[Type] = None
    # The position property
    position: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ParameterInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ParameterInfo
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ParameterInfo()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ..type import Type
        from .custom_attribute_data import CustomAttributeData
        from .member_info import MemberInfo

        from ..type import Type
        from .custom_attribute_data import CustomAttributeData
        from .member_info import MemberInfo

        fields: Dict[str, Callable[[Any], None]] = {
            "attributes": lambda n : setattr(self, 'attributes', n.get_int_value()),
            "customAttributes": lambda n : setattr(self, 'custom_attributes', n.get_collection_of_object_values(CustomAttributeData)),
            "hasDefaultValue": lambda n : setattr(self, 'has_default_value', n.get_bool_value()),
            "isIn": lambda n : setattr(self, 'is_in', n.get_bool_value()),
            "isLcid": lambda n : setattr(self, 'is_lcid', n.get_bool_value()),
            "isOptional": lambda n : setattr(self, 'is_optional', n.get_bool_value()),
            "isOut": lambda n : setattr(self, 'is_out', n.get_bool_value()),
            "isRetval": lambda n : setattr(self, 'is_retval', n.get_bool_value()),
            "member": lambda n : setattr(self, 'member', n.get_object_value(MemberInfo)),
            "metadataToken": lambda n : setattr(self, 'metadata_token', n.get_int_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "parameterType": lambda n : setattr(self, 'parameter_type', n.get_object_value(Type)),
            "position": lambda n : setattr(self, 'position', n.get_int_value()),
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
        from ..type import Type
        from .custom_attribute_data import CustomAttributeData
        from .member_info import MemberInfo

        writer.write_int_value("attributes", self.attributes)
        writer.write_object_value("member", self.member)
        writer.write_object_value("parameterType", self.parameter_type)
    

