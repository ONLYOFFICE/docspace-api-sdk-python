from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class Int32_viewAccessibility(Parsable):
    """
    File accessibility
    """
    # The CanConvert property
    can_convert: Optional[bool] = None
    # The CoAuhtoring property
    co_auhtoring: Optional[bool] = None
    # The ImageView property
    image_view: Optional[bool] = None
    # The MediaView property
    media_view: Optional[bool] = None
    # The MustConvert property
    must_convert: Optional[bool] = None
    # The WebComment property
    web_comment: Optional[bool] = None
    # The WebCustomFilterEditing property
    web_custom_filter_editing: Optional[bool] = None
    # The WebEdit property
    web_edit: Optional[bool] = None
    # The WebRestrictedEditing property
    web_restricted_editing: Optional[bool] = None
    # The WebReview property
    web_review: Optional[bool] = None
    # The WebView property
    web_view: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Int32_viewAccessibility:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Int32_viewAccessibility
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Int32_viewAccessibility()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "CanConvert": lambda n : setattr(self, 'can_convert', n.get_bool_value()),
            "CoAuhtoring": lambda n : setattr(self, 'co_auhtoring', n.get_bool_value()),
            "ImageView": lambda n : setattr(self, 'image_view', n.get_bool_value()),
            "MediaView": lambda n : setattr(self, 'media_view', n.get_bool_value()),
            "MustConvert": lambda n : setattr(self, 'must_convert', n.get_bool_value()),
            "WebComment": lambda n : setattr(self, 'web_comment', n.get_bool_value()),
            "WebCustomFilterEditing": lambda n : setattr(self, 'web_custom_filter_editing', n.get_bool_value()),
            "WebEdit": lambda n : setattr(self, 'web_edit', n.get_bool_value()),
            "WebRestrictedEditing": lambda n : setattr(self, 'web_restricted_editing', n.get_bool_value()),
            "WebReview": lambda n : setattr(self, 'web_review', n.get_bool_value()),
            "WebView": lambda n : setattr(self, 'web_view', n.get_bool_value()),
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
        writer.write_bool_value("CanConvert", self.can_convert)
        writer.write_bool_value("CoAuhtoring", self.co_auhtoring)
        writer.write_bool_value("ImageView", self.image_view)
        writer.write_bool_value("MediaView", self.media_view)
        writer.write_bool_value("MustConvert", self.must_convert)
        writer.write_bool_value("WebComment", self.web_comment)
        writer.write_bool_value("WebCustomFilterEditing", self.web_custom_filter_editing)
        writer.write_bool_value("WebEdit", self.web_edit)
        writer.write_bool_value("WebRestrictedEditing", self.web_restricted_editing)
        writer.write_bool_value("WebReview", self.web_review)
        writer.write_bool_value("WebView", self.web_view)
    

