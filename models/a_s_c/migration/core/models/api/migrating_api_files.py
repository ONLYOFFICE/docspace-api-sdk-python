from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class MigratingApiFiles(Parsable):
    # The bytesTotal property
    bytes_total: Optional[int] = None
    # The filesCount property
    files_count: Optional[int] = None
    # The foldersCount property
    folders_count: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MigratingApiFiles:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MigratingApiFiles
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MigratingApiFiles()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "bytesTotal": lambda n : setattr(self, 'bytes_total', n.get_int_value()),
            "filesCount": lambda n : setattr(self, 'files_count', n.get_int_value()),
            "foldersCount": lambda n : setattr(self, 'folders_count', n.get_int_value()),
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
        writer.write_int_value("bytesTotal", self.bytes_total)
        writer.write_int_value("filesCount", self.files_count)
        writer.write_int_value("foldersCount", self.folders_count)
    

