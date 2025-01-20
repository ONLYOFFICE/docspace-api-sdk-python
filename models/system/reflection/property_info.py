from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..type import Type
    from .custom_attribute_data import CustomAttributeData
    from .method_info import MethodInfo
    from .module import Module

@dataclass
class PropertyInfo(Parsable):
    # The attributes property
    attributes: Optional[int] = None
    # The canRead property
    can_read: Optional[bool] = None
    # The canWrite property
    can_write: Optional[bool] = None
    # The customAttributes property
    custom_attributes: Optional[List[CustomAttributeData]] = None
    # The declaringType property
    declaring_type: Optional[Type] = None
    # The getMethod property
    get_method: Optional[MethodInfo] = None
    # The isCollectible property
    is_collectible: Optional[bool] = None
    # The isSpecialName property
    is_special_name: Optional[bool] = None
    # The memberType property
    member_type: Optional[int] = None
    # The metadataToken property
    metadata_token: Optional[int] = None
    # The module property
    module: Optional[Module] = None
    # The name property
    name: Optional[str] = None
    # The propertyType property
    property_type: Optional[Type] = None
    # The reflectedType property
    reflected_type: Optional[Type] = None
    # The setMethod property
    set_method: Optional[MethodInfo] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PropertyInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PropertyInfo
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PropertyInfo()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ..type import Type
        from .custom_attribute_data import CustomAttributeData
        from .method_info import MethodInfo
        from .module import Module

        from ..type import Type
        from .custom_attribute_data import CustomAttributeData
        from .method_info import MethodInfo
        from .module import Module

        fields: Dict[str, Callable[[Any], None]] = {
            "attributes": lambda n : setattr(self, 'attributes', n.get_int_value()),
            "canRead": lambda n : setattr(self, 'can_read', n.get_bool_value()),
            "canWrite": lambda n : setattr(self, 'can_write', n.get_bool_value()),
            "customAttributes": lambda n : setattr(self, 'custom_attributes', n.get_collection_of_object_values(CustomAttributeData)),
            "declaringType": lambda n : setattr(self, 'declaring_type', n.get_object_value(Type)),
            "getMethod": lambda n : setattr(self, 'get_method', n.get_object_value(MethodInfo)),
            "isCollectible": lambda n : setattr(self, 'is_collectible', n.get_bool_value()),
            "isSpecialName": lambda n : setattr(self, 'is_special_name', n.get_bool_value()),
            "memberType": lambda n : setattr(self, 'member_type', n.get_int_value()),
            "metadataToken": lambda n : setattr(self, 'metadata_token', n.get_int_value()),
            "module": lambda n : setattr(self, 'module', n.get_object_value(Module)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "propertyType": lambda n : setattr(self, 'property_type', n.get_object_value(Type)),
            "reflectedType": lambda n : setattr(self, 'reflected_type', n.get_object_value(Type)),
            "setMethod": lambda n : setattr(self, 'set_method', n.get_object_value(MethodInfo)),
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
        from .method_info import MethodInfo
        from .module import Module

        writer.write_int_value("attributes", self.attributes)
        writer.write_object_value("declaringType", self.declaring_type)
        writer.write_object_value("getMethod", self.get_method)
        writer.write_int_value("memberType", self.member_type)
        writer.write_object_value("module", self.module)
        writer.write_object_value("propertyType", self.property_type)
        writer.write_object_value("reflectedType", self.reflected_type)
        writer.write_object_value("setMethod", self.set_method)
    

