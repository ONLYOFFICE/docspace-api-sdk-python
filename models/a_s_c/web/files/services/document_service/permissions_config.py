from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class PermissionsConfig(Parsable):
    # Change history
    change_history: Optional[bool] = None
    # Chat
    chat: Optional[bool] = None
    # Comment
    comment: Optional[bool] = None
    # Copy
    copy: Optional[bool] = None
    # Download
    download: Optional[bool] = None
    # Edit
    edit: Optional[bool] = None
    # FillForms
    fill_forms: Optional[bool] = None
    # ModifyFilter
    modify_filter: Optional[bool] = None
    # Print
    print: Optional[bool] = None
    # Protect
    protect: Optional[bool] = None
    # Rename
    rename: Optional[bool] = None
    # Review
    review: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PermissionsConfig:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PermissionsConfig
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PermissionsConfig()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "changeHistory": lambda n : setattr(self, 'change_history', n.get_bool_value()),
            "chat": lambda n : setattr(self, 'chat', n.get_bool_value()),
            "comment": lambda n : setattr(self, 'comment', n.get_bool_value()),
            "copy": lambda n : setattr(self, 'copy', n.get_bool_value()),
            "download": lambda n : setattr(self, 'download', n.get_bool_value()),
            "edit": lambda n : setattr(self, 'edit', n.get_bool_value()),
            "fillForms": lambda n : setattr(self, 'fill_forms', n.get_bool_value()),
            "modifyFilter": lambda n : setattr(self, 'modify_filter', n.get_bool_value()),
            "print": lambda n : setattr(self, 'print', n.get_bool_value()),
            "protect": lambda n : setattr(self, 'protect', n.get_bool_value()),
            "rename": lambda n : setattr(self, 'rename', n.get_bool_value()),
            "review": lambda n : setattr(self, 'review', n.get_bool_value()),
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
        writer.write_bool_value("changeHistory", self.change_history)
        writer.write_bool_value("chat", self.chat)
        writer.write_bool_value("comment", self.comment)
        writer.write_bool_value("copy", self.copy)
        writer.write_bool_value("download", self.download)
        writer.write_bool_value("edit", self.edit)
        writer.write_bool_value("fillForms", self.fill_forms)
        writer.write_bool_value("modifyFilter", self.modify_filter)
        writer.write_bool_value("print", self.print)
        writer.write_bool_value("protect", self.protect)
        writer.write_bool_value("rename", self.rename)
        writer.write_bool_value("review", self.review)
    

