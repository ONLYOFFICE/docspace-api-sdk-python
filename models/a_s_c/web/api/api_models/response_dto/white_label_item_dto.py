from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ......six_labors.image_sharp.size import Size
    from .white_label_item_path_dto import WhiteLabelItemPathDto

@dataclass
class WhiteLabelItemDto(Parsable):
    # File name
    name: Optional[str] = None
    # The path property
    path: Optional[WhiteLabelItemPathDto] = None
    # The size property
    size: Optional[Size] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> WhiteLabelItemDto:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: WhiteLabelItemDto
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return WhiteLabelItemDto()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ......six_labors.image_sharp.size import Size
        from .white_label_item_path_dto import WhiteLabelItemPathDto

        from ......six_labors.image_sharp.size import Size
        from .white_label_item_path_dto import WhiteLabelItemPathDto

        fields: Dict[str, Callable[[Any], None]] = {
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "path": lambda n : setattr(self, 'path', n.get_object_value(WhiteLabelItemPathDto)),
            "size": lambda n : setattr(self, 'size', n.get_object_value(Size)),
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
        from ......six_labors.image_sharp.size import Size
        from .white_label_item_path_dto import WhiteLabelItemPathDto

        writer.write_str_value("name", self.name)
        writer.write_object_value("path", self.path)
        writer.write_object_value("size", self.size)
    

