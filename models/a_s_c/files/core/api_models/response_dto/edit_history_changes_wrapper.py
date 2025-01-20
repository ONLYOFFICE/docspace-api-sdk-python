from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....api.core.api_date_time import ApiDateTime
    from ...edit_history_author import EditHistoryAuthor

@dataclass
class EditHistoryChangesWrapper(Parsable):
    # The created property
    created: Optional[ApiDateTime] = None
    # The documentSha256 property
    document_sha256: Optional[str] = None
    # The user property
    user: Optional[EditHistoryAuthor] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> EditHistoryChangesWrapper:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: EditHistoryChangesWrapper
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return EditHistoryChangesWrapper()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .....api.core.api_date_time import ApiDateTime
        from ...edit_history_author import EditHistoryAuthor

        from .....api.core.api_date_time import ApiDateTime
        from ...edit_history_author import EditHistoryAuthor

        fields: Dict[str, Callable[[Any], None]] = {
            "created": lambda n : setattr(self, 'created', n.get_object_value(ApiDateTime)),
            "documentSha256": lambda n : setattr(self, 'document_sha256', n.get_str_value()),
            "user": lambda n : setattr(self, 'user', n.get_object_value(EditHistoryAuthor)),
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

        writer.write_object_value("created", self.created)
        writer.write_str_value("documentSha256", self.document_sha256)
        writer.write_object_value("user", self.user)
    

