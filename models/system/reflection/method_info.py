from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..runtime_method_handle import RuntimeMethodHandle
    from ..type import Type
    from .custom_attribute_data import CustomAttributeData
    from .i_custom_attribute_provider import ICustomAttributeProvider
    from .module import Module
    from .parameter_info import ParameterInfo

@dataclass
class MethodInfo(Parsable):
    # The attributes property
    attributes: Optional[int] = None
    # The callingConvention property
    calling_convention: Optional[int] = None
    # The containsGenericParameters property
    contains_generic_parameters: Optional[bool] = None
    # The customAttributes property
    custom_attributes: Optional[List[CustomAttributeData]] = None
    # The declaringType property
    declaring_type: Optional[Type] = None
    # The isAbstract property
    is_abstract: Optional[bool] = None
    # The isAssembly property
    is_assembly: Optional[bool] = None
    # The isCollectible property
    is_collectible: Optional[bool] = None
    # The isConstructedGenericMethod property
    is_constructed_generic_method: Optional[bool] = None
    # The isConstructor property
    is_constructor: Optional[bool] = None
    # The isFamily property
    is_family: Optional[bool] = None
    # The isFamilyAndAssembly property
    is_family_and_assembly: Optional[bool] = None
    # The isFamilyOrAssembly property
    is_family_or_assembly: Optional[bool] = None
    # The isFinal property
    is_final: Optional[bool] = None
    # The isGenericMethod property
    is_generic_method: Optional[bool] = None
    # The isGenericMethodDefinition property
    is_generic_method_definition: Optional[bool] = None
    # The isHideBySig property
    is_hide_by_sig: Optional[bool] = None
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
    # The isVirtual property
    is_virtual: Optional[bool] = None
    # The memberType property
    member_type: Optional[int] = None
    # The metadataToken property
    metadata_token: Optional[int] = None
    # The methodHandle property
    method_handle: Optional[RuntimeMethodHandle] = None
    # The methodImplementationFlags property
    method_implementation_flags: Optional[int] = None
    # The module property
    module: Optional[Module] = None
    # The name property
    name: Optional[str] = None
    # The reflectedType property
    reflected_type: Optional[Type] = None
    # The returnParameter property
    return_parameter: Optional[ParameterInfo] = None
    # The returnType property
    return_type: Optional[Type] = None
    # The returnTypeCustomAttributes property
    return_type_custom_attributes: Optional[ICustomAttributeProvider] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MethodInfo:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MethodInfo
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MethodInfo()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ..runtime_method_handle import RuntimeMethodHandle
        from ..type import Type
        from .custom_attribute_data import CustomAttributeData
        from .i_custom_attribute_provider import ICustomAttributeProvider
        from .module import Module
        from .parameter_info import ParameterInfo

        from ..runtime_method_handle import RuntimeMethodHandle
        from ..type import Type
        from .custom_attribute_data import CustomAttributeData
        from .i_custom_attribute_provider import ICustomAttributeProvider
        from .module import Module
        from .parameter_info import ParameterInfo

        fields: Dict[str, Callable[[Any], None]] = {
            "attributes": lambda n : setattr(self, 'attributes', n.get_int_value()),
            "callingConvention": lambda n : setattr(self, 'calling_convention', n.get_int_value()),
            "containsGenericParameters": lambda n : setattr(self, 'contains_generic_parameters', n.get_bool_value()),
            "customAttributes": lambda n : setattr(self, 'custom_attributes', n.get_collection_of_object_values(CustomAttributeData)),
            "declaringType": lambda n : setattr(self, 'declaring_type', n.get_object_value(Type)),
            "isAbstract": lambda n : setattr(self, 'is_abstract', n.get_bool_value()),
            "isAssembly": lambda n : setattr(self, 'is_assembly', n.get_bool_value()),
            "isCollectible": lambda n : setattr(self, 'is_collectible', n.get_bool_value()),
            "isConstructedGenericMethod": lambda n : setattr(self, 'is_constructed_generic_method', n.get_bool_value()),
            "isConstructor": lambda n : setattr(self, 'is_constructor', n.get_bool_value()),
            "isFamily": lambda n : setattr(self, 'is_family', n.get_bool_value()),
            "isFamilyAndAssembly": lambda n : setattr(self, 'is_family_and_assembly', n.get_bool_value()),
            "isFamilyOrAssembly": lambda n : setattr(self, 'is_family_or_assembly', n.get_bool_value()),
            "isFinal": lambda n : setattr(self, 'is_final', n.get_bool_value()),
            "isGenericMethod": lambda n : setattr(self, 'is_generic_method', n.get_bool_value()),
            "isGenericMethodDefinition": lambda n : setattr(self, 'is_generic_method_definition', n.get_bool_value()),
            "isHideBySig": lambda n : setattr(self, 'is_hide_by_sig', n.get_bool_value()),
            "isPrivate": lambda n : setattr(self, 'is_private', n.get_bool_value()),
            "isPublic": lambda n : setattr(self, 'is_public', n.get_bool_value()),
            "isSecurityCritical": lambda n : setattr(self, 'is_security_critical', n.get_bool_value()),
            "isSecuritySafeCritical": lambda n : setattr(self, 'is_security_safe_critical', n.get_bool_value()),
            "isSecurityTransparent": lambda n : setattr(self, 'is_security_transparent', n.get_bool_value()),
            "isSpecialName": lambda n : setattr(self, 'is_special_name', n.get_bool_value()),
            "isStatic": lambda n : setattr(self, 'is_static', n.get_bool_value()),
            "isVirtual": lambda n : setattr(self, 'is_virtual', n.get_bool_value()),
            "memberType": lambda n : setattr(self, 'member_type', n.get_int_value()),
            "metadataToken": lambda n : setattr(self, 'metadata_token', n.get_int_value()),
            "methodHandle": lambda n : setattr(self, 'method_handle', n.get_object_value(RuntimeMethodHandle)),
            "methodImplementationFlags": lambda n : setattr(self, 'method_implementation_flags', n.get_int_value()),
            "module": lambda n : setattr(self, 'module', n.get_object_value(Module)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "reflectedType": lambda n : setattr(self, 'reflected_type', n.get_object_value(Type)),
            "returnParameter": lambda n : setattr(self, 'return_parameter', n.get_object_value(ParameterInfo)),
            "returnType": lambda n : setattr(self, 'return_type', n.get_object_value(Type)),
            "returnTypeCustomAttributes": lambda n : setattr(self, 'return_type_custom_attributes', n.get_object_value(ICustomAttributeProvider)),
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
        from ..runtime_method_handle import RuntimeMethodHandle
        from ..type import Type
        from .custom_attribute_data import CustomAttributeData
        from .i_custom_attribute_provider import ICustomAttributeProvider
        from .module import Module
        from .parameter_info import ParameterInfo

        writer.write_int_value("attributes", self.attributes)
        writer.write_int_value("callingConvention", self.calling_convention)
        writer.write_object_value("declaringType", self.declaring_type)
        writer.write_int_value("memberType", self.member_type)
        writer.write_object_value("methodHandle", self.method_handle)
        writer.write_int_value("methodImplementationFlags", self.method_implementation_flags)
        writer.write_object_value("module", self.module)
        writer.write_object_value("reflectedType", self.reflected_type)
        writer.write_object_value("returnParameter", self.return_parameter)
        writer.write_object_value("returnType", self.return_type)
        writer.write_object_value("returnTypeCustomAttributes", self.return_type_custom_attributes)
    

