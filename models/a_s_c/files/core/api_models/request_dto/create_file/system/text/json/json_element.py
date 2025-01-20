from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .json_element_template_id import JsonElement_templateId

@dataclass
class JsonElement(Parsable):
    """
    Parameters for creating a file
    """
    # Specifies whether to allow the creation of external extension files or not
    enable_external_ext: Optional[bool] = None
    # Form ID
    form_id: Optional[int] = None
    # Template file ID
    template_id: Optional[JsonElement_templateId] = None
    # File title
    title: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> JsonElement:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: JsonElement
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return JsonElement()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .json_element_template_id import JsonElement_templateId

        from .json_element_template_id import JsonElement_templateId

        fields: Dict[str, Callable[[Any], None]] = {
            "enableExternalExt": lambda n : setattr(self, 'enable_external_ext', n.get_bool_value()),
            "formId": lambda n : setattr(self, 'form_id', n.get_int_value()),
            "templateId": lambda n : setattr(self, 'template_id', n.get_object_value(JsonElement_templateId)),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
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
        from .json_element_template_id import JsonElement_templateId

        writer.write_bool_value("enableExternalExt", self.enable_external_ext)
        writer.write_int_value("formId", self.form_id)
        writer.write_object_value("templateId", self.template_id)
        writer.write_str_value("title", self.title)
    

