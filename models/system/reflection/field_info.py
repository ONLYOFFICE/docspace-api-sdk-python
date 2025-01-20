from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from warnings import warn

if TYPE_CHECKING:
    from ..runtime_field_handle import RuntimeFieldHandle
    from ..type import Type
    from .custom_attribute_data import CustomAttributeData
    from .module import Module

@dataclass
class FieldInfo(Parsable):
    # The attributes property
    attributes: Optional[int] = None
    # The customAttributes property
    custom_attributes: Optional[List[CustomAttributeData]] = None
    # The declaringType property
    declaring_type: Optional[Type] = None
    # The fieldHandle property
    field_handle: Optional[RuntimeFieldHandle] = None
    # The fieldType property
    field_type: Optional[Type] = None
    # The isAssembly property
    is_assembly: Optional[bool] = None
    # The isCollectible property
    is_collectible: Optional[bool] = None
    # The isFamily property
    is_family: Optional[bool] = None
    # The isFamilyAndAssembly property
    is_family_and_assembly: Optional[bool] = None
    # The isFamilyOrAssembly property
    is_family_or_assembly: Optional[bool] = None
    # The isInitOnly property
    is_init_only: Optional[bool] = None
    # The isLiteral property
    is_literal: Optional[bool] = None
    # The isNotSerialized property
    is_not_serialized: Optional[bool] = None
    # The isPinvokeImpl property
    is_pinvoke_impl: Optional[bool] = None
    # The isPrivate property
    is_private: Optional[bool] = None
    # The isPublic property
    is_public: Optional[bool] = None
    # The isSecurityCritical property
    is_security_critical: Optional[bool] = None
    # The isSecuritySafeCritical property
    is_security_safe_critical: Optional[bool] = None
    # The isSecurityTransparent property
    is_security_transparent: Optional[bool] = None
    # The isSpecialName property
    is_special_name: Optional[bool] = None
    # The isStatic property
    is_static: Optional[bool] = None
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
    def create_from_discriminator_value(parse_node: ParseNode) -> FieldInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FieldInfo
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return FieldInfo()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ..runtime_field_handle import RuntimeFieldHandle
        from ..type import Type
        from .custom_attribute_data import CustomAttributeData
        from .module import Module

        from ..runtime_field_handle import RuntimeFieldHandle
        from ..type import Type
        from .custom_attribute_data import CustomAttributeData
        from .module import Module

        fields: Dict[str, Callable[[Any], None]] = {
            "attributes": lambda n : setattr(self, 'attributes', n.get_int_value()),
            "customAttributes": lambda n : setattr(self, 'custom_attributes', n.get_collection_of_object_values(CustomAttributeData)),
            "declaringType": lambda n : setattr(self, 'declaring_type', n.get_object_value(Type)),
            "fieldHandle": lambda n : setattr(self, 'field_handle', n.get_object_value(RuntimeFieldHandle)),
            "fieldType": lambda n : setattr(self, 'field_type', n.get_object_value(Type)),
            "isAssembly": lambda n : setattr(self, 'is_assembly', n.get_bool_value()),
            "isCollectible": lambda n : setattr(self, 'is_collectible', n.get_bool_value()),
            "isFamily": lambda n : setattr(self, 'is_family', n.get_bool_value()),
            "isFamilyAndAssembly": lambda n : setattr(self, 'is_family_and_assembly', n.get_bool_value()),
            "isFamilyOrAssembly": lambda n : setattr(self, 'is_family_or_assembly', n.get_bool_value()),
            "isInitOnly": lambda n : setattr(self, 'is_init_only', n.get_bool_value()),
            "isLiteral": lambda n : setattr(self, 'is_literal', n.get_bool_value()),
            "isNotSerialized": lambda n : setattr(self, 'is_not_serialized', n.get_bool_value()),
            "isPinvokeImpl": lambda n : setattr(self, 'is_pinvoke_impl', n.get_bool_value()),
            "isPrivate": lambda n : setattr(self, 'is_private', n.get_bool_value()),
            "isPublic": lambda n : setattr(self, 'is_public', n.get_bool_value()),
            "isSecurityCritical": lambda n : setattr(self, 'is_security_critical', n.get_bool_value()),
            "isSecuritySafeCritical": lambda n : setattr(self, 'is_security_safe_critical', n.get_bool_value()),
            "isSecurityTransparent": lambda n : setattr(self, 'is_security_transparent', n.get_bool_value()),
            "isSpecialName": lambda n : setattr(self, 'is_special_name', n.get_bool_value()),
            "isStatic": lambda n : setattr(self, 'is_static', n.get_bool_value()),
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
        from ..runtime_field_handle import RuntimeFieldHandle
        from ..type import Type
        from .custom_attribute_data import CustomAttributeData
        from .module import Module

        writer.write_int_value("attributes", self.attributes)
        writer.write_object_value("declaringType", self.declaring_type)
        writer.write_object_value("fieldHandle", self.field_handle)
        writer.write_object_value("fieldType", self.field_type)
        writer.write_int_value("memberType", self.member_type)
        writer.write_object_value("module", self.module)
        writer.write_object_value("reflectedType", self.reflected_type)
    

