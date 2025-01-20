from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..type import Type
    from .constructor_info import ConstructorInfo
    from .custom_attribute_named_argument import CustomAttributeNamedArgument
    from .custom_attribute_typed_argument import CustomAttributeTypedArgument

@dataclass
class CustomAttributeData(Parsable):
    # The attributeType property
    attribute_type: Optional[Type] = None
    # The constructorArguments property
    constructor_arguments: Optional[List[CustomAttributeTypedArgument]] = None
    # The constructor property
    constructor-property: Optional[ConstructorInfo] = None
    # The namedArguments property
    named_arguments: Optional[List[CustomAttributeNamedArgument]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CustomAttributeData:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CustomAttributeData
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CustomAttributeData()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ..type import Type
        from .constructor_info import ConstructorInfo
        from .custom_attribute_named_argument import CustomAttributeNamedArgument
        from .custom_attribute_typed_argument import CustomAttributeTypedArgument

        from ..type import Type
        from .constructor_info import ConstructorInfo
        from .custom_attribute_named_argument import CustomAttributeNamedArgument
        from .custom_attribute_typed_argument import CustomAttributeTypedArgument

        fields: Dict[str, Callable[[Any], None]] = {
            "attributeType": lambda n : setattr(self, 'attribute_type', n.get_object_value(Type)),
            "constructorArguments": lambda n : setattr(self, 'constructor_arguments', n.get_collection_of_object_values(CustomAttributeTypedArgument)),
            "constructor": lambda n : setattr(self, 'constructor-property', n.get_object_value(ConstructorInfo)),
            "namedArguments": lambda n : setattr(self, 'named_arguments', n.get_collection_of_object_values(CustomAttributeNamedArgument)),
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
        from .constructor_info import ConstructorInfo
        from .custom_attribute_named_argument import CustomAttributeNamedArgument
        from .custom_attribute_typed_argument import CustomAttributeTypedArgument

        writer.write_object_value("attributeType", self.attribute_type)
        writer.write_object_value("constructor", self.constructor-property)
    

