from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....api.core.api_date_time import ApiDateTime
    from ...edit_history_author import EditHistoryAuthor
    from .edit_history_changes_wrapper import EditHistoryChangesWrapper

@dataclass
class EditHistoryDto(Parsable):
    # List of history changes
    changes: Optional[List[EditHistoryChangesWrapper]] = None
    # History changes in the string format
    changes_history: Optional[str] = None
    # The created property
    created: Optional[ApiDateTime] = None
    # File ID
    id: Optional[int] = None
    # Key
    key: Optional[str] = None
    # Server version
    server_version: Optional[str] = None
    # The user property
    user: Optional[EditHistoryAuthor] = None
    # File version
    version: Optional[int] = None
    # Version group
    version_group: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EditHistoryDto:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EditHistoryDto
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EditHistoryDto()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .....api.core.api_date_time import ApiDateTime
        from ...edit_history_author import EditHistoryAuthor
        from .edit_history_changes_wrapper import EditHistoryChangesWrapper

        from .....api.core.api_date_time import ApiDateTime
        from ...edit_history_author import EditHistoryAuthor
        from .edit_history_changes_wrapper import EditHistoryChangesWrapper

        fields: Dict[str, Callable[[Any], None]] = {
            "changes": lambda n : setattr(self, 'changes', n.get_collection_of_object_values(EditHistoryChangesWrapper)),
            "changesHistory": lambda n : setattr(self, 'changes_history', n.get_str_value()),
            "created": lambda n : setattr(self, 'created', n.get_object_value(ApiDateTime)),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "key": lambda n : setattr(self, 'key', n.get_str_value()),
            "serverVersion": lambda n : setattr(self, 'server_version', n.get_str_value()),
            "user": lambda n : setattr(self, 'user', n.get_object_value(EditHistoryAuthor)),
            "version": lambda n : setattr(self, 'version', n.get_int_value()),
            "versionGroup": lambda n : setattr(self, 'version_group', n.get_int_value()),
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
        from .....api.core.api_date_time import ApiDateTime
        from ...edit_history_author import EditHistoryAuthor
        from .edit_history_changes_wrapper import EditHistoryChangesWrapper

        writer.write_collection_of_object_values("changes", self.changes)
        writer.write_str_value("changesHistory", self.changes_history)
        writer.write_object_value("created", self.created)
        writer.write_int_value("id", self.id)
        writer.write_str_value("key", self.key)
        writer.write_str_value("serverVersion", self.server_version)
        writer.write_object_value("user", self.user)
        writer.write_int_value("version", self.version)
        writer.write_int_value("versionGroup", self.version_group)
    

