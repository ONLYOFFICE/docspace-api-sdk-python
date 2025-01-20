from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID
from warnings import warn

if TYPE_CHECKING:
    from .reflection.assembly import Assembly
    from .reflection.constructor_info import ConstructorInfo
    from .reflection.custom_attribute_data import CustomAttributeData
    from .reflection.method_base import MethodBase
    from .reflection.module import Module
    from .runtime.interop_services.struct_layout_attribute import StructLayoutAttribute
    from .runtime_type_handle import RuntimeTypeHandle

@dataclass
class Type(Parsable):
    # The assembly property
    assembly: Optional[Assembly] = None
    # The assemblyQualifiedName property
    assembly_qualified_name: Optional[str] = None
    # The attributes property
    attributes: Optional[int] = None
    # The baseType property
    base_type: Optional[Type] = None
    # The containsGenericParameters property
    contains_generic_parameters: Optional[bool] = None
    # The customAttributes property
    custom_attributes: Optional[List[CustomAttributeData]] = None
    # The declaringMethod property
    declaring_method: Optional[MethodBase] = None
    # The declaringType property
    declaring_type: Optional[Type] = None
    # The fullName property
    full_name: Optional[str] = None
    # The genericParameterAttributes property
    generic_parameter_attributes: Optional[int] = None
    # The genericParameterPosition property
    generic_parameter_position: Optional[int] = None
    # The genericTypeArguments property
    generic_type_arguments: Optional[List[Type]] = None
    # The guid property
    guid: Optional[UUID] = None
    # The hasElementType property
    has_element_type: Optional[bool] = None
    # The isAbstract property
    is_abstract: Optional[bool] = None
    # The isAnsiClass property
    is_ansi_class: Optional[bool] = None
    # The isArray property
    is_array: Optional[bool] = None
    # The isAutoClass property
    is_auto_class: Optional[bool] = None
    # The isAutoLayout property
    is_auto_layout: Optional[bool] = None
    # The isByRef property
    is_by_ref: Optional[bool] = None
    # The isByRefLike property
    is_by_ref_like: Optional[bool] = None
    # The isCOMObject property
    is_c_o_m_object: Optional[bool] = None
    # The isClass property
    is_class: Optional[bool] = None
    # The isCollectible property
    is_collectible: Optional[bool] = None
    # The isConstructedGenericType property
    is_constructed_generic_type: Optional[bool] = None
    # The isContextful property
    is_contextful: Optional[bool] = None
    # The isEnum property
    is_enum: Optional[bool] = None
    # The isExplicitLayout property
    is_explicit_layout: Optional[bool] = None
    # The isFunctionPointer property
    is_function_pointer: Optional[bool] = None
    # The isGenericMethodParameter property
    is_generic_method_parameter: Optional[bool] = None
    # The isGenericParameter property
    is_generic_parameter: Optional[bool] = None
    # The isGenericType property
    is_generic_type: Optional[bool] = None
    # The isGenericTypeDefinition property
    is_generic_type_definition: Optional[bool] = None
    # The isGenericTypeParameter property
    is_generic_type_parameter: Optional[bool] = None
    # The isImport property
    is_import: Optional[bool] = None
    # The isInterface property
    is_interface: Optional[bool] = None
    # The isLayoutSequential property
    is_layout_sequential: Optional[bool] = None
    # The isMarshalByRef property
    is_marshal_by_ref: Optional[bool] = None
    # The isNested property
    is_nested: Optional[bool] = None
    # The isNestedAssembly property
    is_nested_assembly: Optional[bool] = None
    # The isNestedFamANDAssem property
    is_nested_fam_a_n_d_assem: Optional[bool] = None
    # The isNestedFamORAssem property
    is_nested_fam_o_r_assem: Optional[bool] = None
    # The isNestedFamily property
    is_nested_family: Optional[bool] = None
    # The isNestedPrivate property
    is_nested_private: Optional[bool] = None
    # The isNestedPublic property
    is_nested_public: Optional[bool] = None
    # The isNotPublic property
    is_not_public: Optional[bool] = None
    # The isPointer property
    is_pointer: Optional[bool] = None
    # The isPrimitive property
    is_primitive: Optional[bool] = None
    # The isPublic property
    is_public: Optional[bool] = None
    # The isSZArray property
    is_s_z_array: Optional[bool] = None
    # The isSealed property
    is_sealed: Optional[bool] = None
    # The isSecurityCritical property
    is_security_critical: Optional[bool] = None
    # The isSecuritySafeCritical property
    is_security_safe_critical: Optional[bool] = None
    # The isSecurityTransparent property
    is_security_transparent: Optional[bool] = None
    # The isSerializable property
    is_serializable: Optional[bool] = None
    # The isSignatureType property
    is_signature_type: Optional[bool] = None
    # The isSpecialName property
    is_special_name: Optional[bool] = None
    # The isTypeDefinition property
    is_type_definition: Optional[bool] = None
    # The isUnicodeClass property
    is_unicode_class: Optional[bool] = None
    # The isUnmanagedFunctionPointer property
    is_unmanaged_function_pointer: Optional[bool] = None
    # The isValueType property
    is_value_type: Optional[bool] = None
    # The isVariableBoundArray property
    is_variable_bound_array: Optional[bool] = None
    # The isVisible property
    is_visible: Optional[bool] = None
    # The memberType property
    member_type: Optional[int] = None
    # The metadataToken property
    metadata_token: Optional[int] = None
    # The module property
    module: Optional[Module] = None
    # The name property
    name: Optional[str] = None
    # The namespace property
    namespace: Optional[str] = None
    # The reflectedType property
    reflected_type: Optional[Type] = None
    # The structLayoutAttribute property
    struct_layout_attribute: Optional[StructLayoutAttribute] = None
    # The typeHandle property
    type_handle: Optional[RuntimeTypeHandle] = None
    # The typeInitializer property
    type_initializer: Optional[ConstructorInfo] = None
    # The underlyingSystemType property
    underlying_system_type: Optional[Type] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Type:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Type
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Type()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .reflection.assembly import Assembly
        from .reflection.constructor_info import ConstructorInfo
        from .reflection.custom_attribute_data import CustomAttributeData
        from .reflection.method_base import MethodBase
        from .reflection.module import Module
        from .runtime.interop_services.struct_layout_attribute import StructLayoutAttribute
        from .runtime_type_handle import RuntimeTypeHandle

        from .reflection.assembly import Assembly
        from .reflection.constructor_info import ConstructorInfo
        from .reflection.custom_attribute_data import CustomAttributeData
        from .reflection.method_base import MethodBase
        from .reflection.module import Module
        from .runtime.interop_services.struct_layout_attribute import StructLayoutAttribute
        from .runtime_type_handle import RuntimeTypeHandle

        fields: Dict[str, Callable[[Any], None]] = {
            "assembly": lambda n : setattr(self, 'assembly', n.get_object_value(Assembly)),
            "assemblyQualifiedName": lambda n : setattr(self, 'assembly_qualified_name', n.get_str_value()),
            "attributes": lambda n : setattr(self, 'attributes', n.get_int_value()),
            "baseType": lambda n : setattr(self, 'base_type', n.get_object_value(Type)),
            "containsGenericParameters": lambda n : setattr(self, 'contains_generic_parameters', n.get_bool_value()),
            "customAttributes": lambda n : setattr(self, 'custom_attributes', n.get_collection_of_object_values(CustomAttributeData)),
            "declaringMethod": lambda n : setattr(self, 'declaring_method', n.get_object_value(MethodBase)),
            "declaringType": lambda n : setattr(self, 'declaring_type', n.get_object_value(Type)),
            "fullName": lambda n : setattr(self, 'full_name', n.get_str_value()),
            "genericParameterAttributes": lambda n : setattr(self, 'generic_parameter_attributes', n.get_int_value()),
            "genericParameterPosition": lambda n : setattr(self, 'generic_parameter_position', n.get_int_value()),
            "genericTypeArguments": lambda n : setattr(self, 'generic_type_arguments', n.get_collection_of_object_values(Type)),
            "guid": lambda n : setattr(self, 'guid', n.get_uuid_value()),
            "hasElementType": lambda n : setattr(self, 'has_element_type', n.get_bool_value()),
            "isAbstract": lambda n : setattr(self, 'is_abstract', n.get_bool_value()),
            "isAnsiClass": lambda n : setattr(self, 'is_ansi_class', n.get_bool_value()),
            "isArray": lambda n : setattr(self, 'is_array', n.get_bool_value()),
            "isAutoClass": lambda n : setattr(self, 'is_auto_class', n.get_bool_value()),
            "isAutoLayout": lambda n : setattr(self, 'is_auto_layout', n.get_bool_value()),
            "isByRef": lambda n : setattr(self, 'is_by_ref', n.get_bool_value()),
            "isByRefLike": lambda n : setattr(self, 'is_by_ref_like', n.get_bool_value()),
            "isCOMObject": lambda n : setattr(self, 'is_c_o_m_object', n.get_bool_value()),
            "isClass": lambda n : setattr(self, 'is_class', n.get_bool_value()),
            "isCollectible": lambda n : setattr(self, 'is_collectible', n.get_bool_value()),
            "isConstructedGenericType": lambda n : setattr(self, 'is_constructed_generic_type', n.get_bool_value()),
            "isContextful": lambda n : setattr(self, 'is_contextful', n.get_bool_value()),
            "isEnum": lambda n : setattr(self, 'is_enum', n.get_bool_value()),
            "isExplicitLayout": lambda n : setattr(self, 'is_explicit_layout', n.get_bool_value()),
            "isFunctionPointer": lambda n : setattr(self, 'is_function_pointer', n.get_bool_value()),
            "isGenericMethodParameter": lambda n : setattr(self, 'is_generic_method_parameter', n.get_bool_value()),
            "isGenericParameter": lambda n : setattr(self, 'is_generic_parameter', n.get_bool_value()),
            "isGenericType": lambda n : setattr(self, 'is_generic_type', n.get_bool_value()),
            "isGenericTypeDefinition": lambda n : setattr(self, 'is_generic_type_definition', n.get_bool_value()),
            "isGenericTypeParameter": lambda n : setattr(self, 'is_generic_type_parameter', n.get_bool_value()),
            "isImport": lambda n : setattr(self, 'is_import', n.get_bool_value()),
            "isInterface": lambda n : setattr(self, 'is_interface', n.get_bool_value()),
            "isLayoutSequential": lambda n : setattr(self, 'is_layout_sequential', n.get_bool_value()),
            "isMarshalByRef": lambda n : setattr(self, 'is_marshal_by_ref', n.get_bool_value()),
            "isNested": lambda n : setattr(self, 'is_nested', n.get_bool_value()),
            "isNestedAssembly": lambda n : setattr(self, 'is_nested_assembly', n.get_bool_value()),
            "isNestedFamANDAssem": lambda n : setattr(self, 'is_nested_fam_a_n_d_assem', n.get_bool_value()),
            "isNestedFamORAssem": lambda n : setattr(self, 'is_nested_fam_o_r_assem', n.get_bool_value()),
            "isNestedFamily": lambda n : setattr(self, 'is_nested_family', n.get_bool_value()),
            "isNestedPrivate": lambda n : setattr(self, 'is_nested_private', n.get_bool_value()),
            "isNestedPublic": lambda n : setattr(self, 'is_nested_public', n.get_bool_value()),
            "isNotPublic": lambda n : setattr(self, 'is_not_public', n.get_bool_value()),
            "isPointer": lambda n : setattr(self, 'is_pointer', n.get_bool_value()),
            "isPrimitive": lambda n : setattr(self, 'is_primitive', n.get_bool_value()),
            "isPublic": lambda n : setattr(self, 'is_public', n.get_bool_value()),
            "isSZArray": lambda n : setattr(self, 'is_s_z_array', n.get_bool_value()),
            "isSealed": lambda n : setattr(self, 'is_sealed', n.get_bool_value()),
            "isSecurityCritical": lambda n : setattr(self, 'is_security_critical', n.get_bool_value()),
            "isSecuritySafeCritical": lambda n : setattr(self, 'is_security_safe_critical', n.get_bool_value()),
            "isSecurityTransparent": lambda n : setattr(self, 'is_security_transparent', n.get_bool_value()),
            "isSerializable": lambda n : setattr(self, 'is_serializable', n.get_bool_value()),
            "isSignatureType": lambda n : setattr(self, 'is_signature_type', n.get_bool_value()),
            "isSpecialName": lambda n : setattr(self, 'is_special_name', n.get_bool_value()),
            "isTypeDefinition": lambda n : setattr(self, 'is_type_definition', n.get_bool_value()),
            "isUnicodeClass": lambda n : setattr(self, 'is_unicode_class', n.get_bool_value()),
            "isUnmanagedFunctionPointer": lambda n : setattr(self, 'is_unmanaged_function_pointer', n.get_bool_value()),
            "isValueType": lambda n : setattr(self, 'is_value_type', n.get_bool_value()),
            "isVariableBoundArray": lambda n : setattr(self, 'is_variable_bound_array', n.get_bool_value()),
            "isVisible": lambda n : setattr(self, 'is_visible', n.get_bool_value()),
            "memberType": lambda n : setattr(self, 'member_type', n.get_int_value()),
            "metadataToken": lambda n : setattr(self, 'metadata_token', n.get_int_value()),
            "module": lambda n : setattr(self, 'module', n.get_object_value(Module)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "namespace": lambda n : setattr(self, 'namespace', n.get_str_value()),
            "reflectedType": lambda n : setattr(self, 'reflected_type', n.get_object_value(Type)),
            "structLayoutAttribute": lambda n : setattr(self, 'struct_layout_attribute', n.get_object_value(StructLayoutAttribute)),
            "typeHandle": lambda n : setattr(self, 'type_handle', n.get_object_value(RuntimeTypeHandle)),
            "typeInitializer": lambda n : setattr(self, 'type_initializer', n.get_object_value(ConstructorInfo)),
            "underlyingSystemType": lambda n : setattr(self, 'underlying_system_type', n.get_object_value(Type)),
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
        from .reflection.assembly import Assembly
        from .reflection.constructor_info import ConstructorInfo
        from .reflection.custom_attribute_data import CustomAttributeData
        from .reflection.method_base import MethodBase
        from .reflection.module import Module
        from .runtime.interop_services.struct_layout_attribute import StructLayoutAttribute
        from .runtime_type_handle import RuntimeTypeHandle

        writer.write_object_value("assembly", self.assembly)
        writer.write_int_value("attributes", self.attributes)
        writer.write_object_value("baseType", self.base_type)
        writer.write_object_value("declaringMethod", self.declaring_method)
        writer.write_object_value("declaringType", self.declaring_type)
        writer.write_int_value("genericParameterAttributes", self.generic_parameter_attributes)
        writer.write_int_value("memberType", self.member_type)
        writer.write_object_value("module", self.module)
        writer.write_object_value("reflectedType", self.reflected_type)
        writer.write_object_value("structLayoutAttribute", self.struct_layout_attribute)
        writer.write_object_value("typeHandle", self.type_handle)
        writer.write_object_value("typeInitializer", self.type_initializer)
        writer.write_object_value("underlyingSystemType", self.underlying_system_type)
    

