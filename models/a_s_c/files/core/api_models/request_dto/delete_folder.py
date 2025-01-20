from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class DeleteFolder(Parsable):
    """
    Parameters for deleting a folder
    """
    # Specifies whether to delete a folder after the editing session is finished or not
    delete_after: Optional[bool] = None
    # Specifies whether to move a folder to the /"Trash/" folder or delete it immediately
    immediately: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeleteFolder:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeleteFolder
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeleteFolder()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "deleteAfter": lambda n : setattr(self, 'delete_after', n.get_bool_value()),
            "immediately": lambda n : setattr(self, 'immediately', n.get_bool_value()),
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
        writer.write_bool_value("deleteAfter", self.delete_after)
        writer.write_bool_value("immediately", self.immediately)
    

