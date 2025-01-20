from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class FileShareDto(Parsable):
    # [0 - None, 1 - Read and write, 2 - Read, 3 - Restrict, 4 - Varies, 5 - Review, 6 - Comment, 7 - Fill forms, 8 - Custom filter, 9 - Room manager, 10 - Editing, 11 - Content creator]
    access: Optional[int] = None
    # Spceifies if this user can edit the access to the specified file or not
    can_edit_access: Optional[bool] = None
    # Specifies if the file is locked by this user or not
    is_locked: Optional[bool] = None
    # Specifies if this user is an owner of the specified file or not
    is_owner: Optional[bool] = None
    # [0 - User, 1 - External link, 2 - Group, 3 - Invitation link, 4 - Primary external link]
    subject_type: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> FileShareDto:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FileShareDto
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return FileShareDto()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "access": lambda n : setattr(self, 'access', n.get_int_value()),
            "canEditAccess": lambda n : setattr(self, 'can_edit_access', n.get_bool_value()),
            "isLocked": lambda n : setattr(self, 'is_locked', n.get_bool_value()),
            "isOwner": lambda n : setattr(self, 'is_owner', n.get_bool_value()),
            "subjectType": lambda n : setattr(self, 'subject_type', n.get_int_value()),
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
        writer.write_int_value("access", self.access)
        writer.write_bool_value("canEditAccess", self.can_edit_access)
        writer.write_bool_value("isLocked", self.is_locked)
        writer.write_bool_value("isOwner", self.is_owner)
        writer.write_int_value("subjectType", self.subject_type)
    

