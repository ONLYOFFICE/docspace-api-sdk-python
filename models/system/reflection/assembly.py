from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from warnings import warn

if TYPE_CHECKING:
    from ..type import Type
    from .custom_attribute_data import CustomAttributeData
    from .method_info import MethodInfo
    from .module import Module
    from .type_info import TypeInfo

@dataclass
class Assembly(Parsable):
    # The codeBase property
    code_base: Optional[str] = None
    # The customAttributes property
    custom_attributes: Optional[List[CustomAttributeData]] = None
    # The definedTypes property
    defined_types: Optional[List[TypeInfo]] = None
    # The entryPoint property
    entry_point: Optional[MethodInfo] = None
    # The escapedCodeBase property
    escaped_code_base: Optional[str] = None
    # The exportedTypes property
    exported_types: Optional[List[Type]] = None
    # The fullName property
    full_name: Optional[str] = None
    # The globalAssemblyCache property
    global_assembly_cache: Optional[bool] = None
    # The hostContext property
    host_context: Optional[int] = None
    # The imageRuntimeVersion property
    image_runtime_version: Optional[str] = None
    # The isCollectible property
    is_collectible: Optional[bool] = None
    # The isDynamic property
    is_dynamic: Optional[bool] = None
    # The isFullyTrusted property
    is_fully_trusted: Optional[bool] = None
    # The location property
    location: Optional[str] = None
    # The manifestModule property
    manifest_module: Optional[Module] = None
    # The modules property
    modules: Optional[List[Module]] = None
    # The reflectionOnly property
    reflection_only: Optional[bool] = None
    # The securityRuleSet property
    security_rule_set: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Assembly:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Assembly
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Assembly()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ..type import Type
        from .custom_attribute_data import CustomAttributeData
        from .method_info import MethodInfo
        from .module import Module
        from .type_info import TypeInfo

        from ..type import Type
        from .custom_attribute_data import CustomAttributeData
        from .method_info import MethodInfo
        from .module import Module
        from .type_info import TypeInfo

        fields: Dict[str, Callable[[Any], None]] = {
            "codeBase": lambda n : setattr(self, 'code_base', n.get_str_value()),
            "customAttributes": lambda n : setattr(self, 'custom_attributes', n.get_collection_of_object_values(CustomAttributeData)),
            "definedTypes": lambda n : setattr(self, 'defined_types', n.get_collection_of_object_values(TypeInfo)),
            "entryPoint": lambda n : setattr(self, 'entry_point', n.get_object_value(MethodInfo)),
            "escapedCodeBase": lambda n : setattr(self, 'escaped_code_base', n.get_str_value()),
            "exportedTypes": lambda n : setattr(self, 'exported_types', n.get_collection_of_object_values(Type)),
            "fullName": lambda n : setattr(self, 'full_name', n.get_str_value()),
            "globalAssemblyCache": lambda n : setattr(self, 'global_assembly_cache', n.get_bool_value()),
            "hostContext": lambda n : setattr(self, 'host_context', n.get_int_value()),
            "imageRuntimeVersion": lambda n : setattr(self, 'image_runtime_version', n.get_str_value()),
            "isCollectible": lambda n : setattr(self, 'is_collectible', n.get_bool_value()),
            "isDynamic": lambda n : setattr(self, 'is_dynamic', n.get_bool_value()),
            "isFullyTrusted": lambda n : setattr(self, 'is_fully_trusted', n.get_bool_value()),
            "location": lambda n : setattr(self, 'location', n.get_str_value()),
            "manifestModule": lambda n : setattr(self, 'manifest_module', n.get_object_value(Module)),
            "modules": lambda n : setattr(self, 'modules', n.get_collection_of_object_values(Module)),
            "reflectionOnly": lambda n : setattr(self, 'reflection_only', n.get_bool_value()),
            "securityRuleSet": lambda n : setattr(self, 'security_rule_set', n.get_int_value()),
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
        from .type_info import TypeInfo

        writer.write_object_value("entryPoint", self.entry_point)
        writer.write_object_value("manifestModule", self.manifest_module)
        writer.write_int_value("securityRuleSet", self.security_rule_set)
    

