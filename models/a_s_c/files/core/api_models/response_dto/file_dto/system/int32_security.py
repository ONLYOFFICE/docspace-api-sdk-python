from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class Int32_security(Parsable):
    """
    Security
    """
    # The ChangeOwner property
    change_owner: Optional[bool] = None
    # The Comment property
    comment: Optional[bool] = None
    # The Convert property
    convert: Optional[bool] = None
    # The Copy property
    copy: Optional[bool] = None
    # The CopyLink property
    copy_link: Optional[bool] = None
    # The CopySharedLink property
    copy_shared_link: Optional[bool] = None
    # The CopyTo property
    copy_to: Optional[bool] = None
    # The Create property
    create: Optional[bool] = None
    # The CreateRoomFrom property
    create_room_from: Optional[bool] = None
    # The CustomFilter property
    custom_filter: Optional[bool] = None
    # The Delete property
    delete: Optional[bool] = None
    # The Download property
    download: Optional[bool] = None
    # The Duplicate property
    duplicate: Optional[bool] = None
    # The Edit property
    edit: Optional[bool] = None
    # The EditAccess property
    edit_access: Optional[bool] = None
    # The EditHistory property
    edit_history: Optional[bool] = None
    # The EditRoom property
    edit_room: Optional[bool] = None
    # The Embed property
    embed: Optional[bool] = None
    # The FillForms property
    fill_forms: Optional[bool] = None
    # The IndexExport property
    index_export: Optional[bool] = None
    # The Lock property
    lock: Optional[bool] = None
    # The Move property
    move: Optional[bool] = None
    # The MoveTo property
    move_to: Optional[bool] = None
    # The Mute property
    mute: Optional[bool] = None
    # The Pin property
    pin: Optional[bool] = None
    # The Read property
    read: Optional[bool] = None
    # The ReadHistory property
    read_history: Optional[bool] = None
    # The ReadLinks property
    read_links: Optional[bool] = None
    # The Reconnect property
    reconnect: Optional[bool] = None
    # The Rename property
    rename: Optional[bool] = None
    # The Review property
    review: Optional[bool] = None
    # The SubmitToFormGallery property
    submit_to_form_gallery: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Int32_security:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Int32_security
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Int32_security()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "ChangeOwner": lambda n : setattr(self, 'change_owner', n.get_bool_value()),
            "Comment": lambda n : setattr(self, 'comment', n.get_bool_value()),
            "Convert": lambda n : setattr(self, 'convert', n.get_bool_value()),
            "Copy": lambda n : setattr(self, 'copy', n.get_bool_value()),
            "CopyLink": lambda n : setattr(self, 'copy_link', n.get_bool_value()),
            "CopySharedLink": lambda n : setattr(self, 'copy_shared_link', n.get_bool_value()),
            "CopyTo": lambda n : setattr(self, 'copy_to', n.get_bool_value()),
            "Create": lambda n : setattr(self, 'create', n.get_bool_value()),
            "CreateRoomFrom": lambda n : setattr(self, 'create_room_from', n.get_bool_value()),
            "CustomFilter": lambda n : setattr(self, 'custom_filter', n.get_bool_value()),
            "Delete": lambda n : setattr(self, 'delete', n.get_bool_value()),
            "Download": lambda n : setattr(self, 'download', n.get_bool_value()),
            "Duplicate": lambda n : setattr(self, 'duplicate', n.get_bool_value()),
            "Edit": lambda n : setattr(self, 'edit', n.get_bool_value()),
            "EditAccess": lambda n : setattr(self, 'edit_access', n.get_bool_value()),
            "EditHistory": lambda n : setattr(self, 'edit_history', n.get_bool_value()),
            "EditRoom": lambda n : setattr(self, 'edit_room', n.get_bool_value()),
            "Embed": lambda n : setattr(self, 'embed', n.get_bool_value()),
            "FillForms": lambda n : setattr(self, 'fill_forms', n.get_bool_value()),
            "IndexExport": lambda n : setattr(self, 'index_export', n.get_bool_value()),
            "Lock": lambda n : setattr(self, 'lock', n.get_bool_value()),
            "Move": lambda n : setattr(self, 'move', n.get_bool_value()),
            "MoveTo": lambda n : setattr(self, 'move_to', n.get_bool_value()),
            "Mute": lambda n : setattr(self, 'mute', n.get_bool_value()),
            "Pin": lambda n : setattr(self, 'pin', n.get_bool_value()),
            "Read": lambda n : setattr(self, 'read', n.get_bool_value()),
            "ReadHistory": lambda n : setattr(self, 'read_history', n.get_bool_value()),
            "ReadLinks": lambda n : setattr(self, 'read_links', n.get_bool_value()),
            "Reconnect": lambda n : setattr(self, 'reconnect', n.get_bool_value()),
            "Rename": lambda n : setattr(self, 'rename', n.get_bool_value()),
            "Review": lambda n : setattr(self, 'review', n.get_bool_value()),
            "SubmitToFormGallery": lambda n : setattr(self, 'submit_to_form_gallery', n.get_bool_value()),
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
        writer.write_bool_value("ChangeOwner", self.change_owner)
        writer.write_bool_value("Comment", self.comment)
        writer.write_bool_value("Convert", self.convert)
        writer.write_bool_value("Copy", self.copy)
        writer.write_bool_value("CopyLink", self.copy_link)
        writer.write_bool_value("CopySharedLink", self.copy_shared_link)
        writer.write_bool_value("CopyTo", self.copy_to)
        writer.write_bool_value("Create", self.create)
        writer.write_bool_value("CreateRoomFrom", self.create_room_from)
        writer.write_bool_value("CustomFilter", self.custom_filter)
        writer.write_bool_value("Delete", self.delete)
        writer.write_bool_value("Download", self.download)
        writer.write_bool_value("Duplicate", self.duplicate)
        writer.write_bool_value("Edit", self.edit)
        writer.write_bool_value("EditAccess", self.edit_access)
        writer.write_bool_value("EditHistory", self.edit_history)
        writer.write_bool_value("EditRoom", self.edit_room)
        writer.write_bool_value("Embed", self.embed)
        writer.write_bool_value("FillForms", self.fill_forms)
        writer.write_bool_value("IndexExport", self.index_export)
        writer.write_bool_value("Lock", self.lock)
        writer.write_bool_value("Move", self.move)
        writer.write_bool_value("MoveTo", self.move_to)
        writer.write_bool_value("Mute", self.mute)
        writer.write_bool_value("Pin", self.pin)
        writer.write_bool_value("Read", self.read)
        writer.write_bool_value("ReadHistory", self.read_history)
        writer.write_bool_value("ReadLinks", self.read_links)
        writer.write_bool_value("Reconnect", self.reconnect)
        writer.write_bool_value("Rename", self.rename)
        writer.write_bool_value("Review", self.review)
        writer.write_bool_value("SubmitToFormGallery", self.submit_to_form_gallery)
    

