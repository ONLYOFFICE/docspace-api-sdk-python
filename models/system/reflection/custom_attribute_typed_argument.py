from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..type import Type

@dataclass
class CustomAttributeTypedArgument(Parsable):
    # The argumentType property
    argument_type: Optional[Type] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CustomAttributeTypedArgument:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CustomAttributeTypedArgument
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CustomAttributeTypedArgument()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ..type import Type

        from ..type import Type

        fields: Dict[str, Callable[[Any], None]] = {
            "argumentType": lambda n : setattr(self, 'argument_type', n.get_object_value(Type)),
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

        writer.write_object_value("argumentType", self.argument_type)
    

