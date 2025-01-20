from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..type import Type
    from .custom_attribute_data import CustomAttributeData
    from .module import Module

@dataclass
class MemberInfo(Parsable):
    # The customAttributes property
    custom_attributes: Optional[List[CustomAttributeData]] = None
    # The declaringType property
    declaring_type: Optional[Type] = None
    # The isCollectible property
    is_collectible: Optional[bool] = None
    # The memberType property
    member_type: Optional[int] = None
    # The metadataToken property
    metadata_token: Optional[int] = None
    # The module property
    module: Optional[Module] = None
    # The name property
    name: Optional[str] = None
    # The reflectedType property
    reflected_type: Optional[Type] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MemberInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MemberInfo
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MemberInfo()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ..type import Type
        from .custom_attribute_data import CustomAttributeData
        from .module import Module

        from ..type import Type
        from .custom_attribute_data import CustomAttributeData
        from .module import Module

        fields: Dict[str, Callable[[Any], None]] = {
            "customAttributes": lambda n : setattr(self, 'custom_attributes', n.get_collection_of_object_values(CustomAttributeData)),
            "declaringType": lambda n : setattr(self, 'declaring_type', n.get_object_value(Type)),
            "isCollectible": lambda n : setattr(self, 'is_collectible', n.get_bool_value()),
            "memberType": lambda n : setattr(self, 'member_type', n.get_int_value()),
            "metadataToken": lambda n : setattr(self, 'metadata_token', n.get_int_value()),
            "module": lambda n : setattr(self, 'module', n.get_object_value(Module)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "reflectedType": lambda n : setattr(self, 'reflected_type', n.get_object_value(Type)),
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
        from .module import Module

        writer.write_object_value("declaringType", self.declaring_type)
        writer.write_int_value("memberType", self.member_type)
        writer.write_object_value("module", self.module)
        writer.write_object_value("reflectedType", self.reflected_type)
    

