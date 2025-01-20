from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....migration.core.models.api.migration_api_info import MigrationApiInfo

@dataclass
class MigrationStatusDto(Parsable):
    # Migration error
    error: Optional[str] = None
    # Specifies whether the migration is completed
    is_completed: Optional[bool] = None
    # The parseResult property
    parse_result: Optional[MigrationApiInfo] = None
    # Migration progress
    progress: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MigrationStatusDto:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MigrationStatusDto
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MigrationStatusDto()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .....migration.core.models.api.migration_api_info import MigrationApiInfo

        from .....migration.core.models.api.migration_api_info import MigrationApiInfo

        fields: Dict[str, Callable[[Any], None]] = {
            "error": lambda n : setattr(self, 'error', n.get_str_value()),
            "isCompleted": lambda n : setattr(self, 'is_completed', n.get_bool_value()),
            "parseResult": lambda n : setattr(self, 'parse_result', n.get_object_value(MigrationApiInfo)),
            "progress": lambda n : setattr(self, 'progress', n.get_float_value()),
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
        from .....migration.core.models.api.migration_api_info import MigrationApiInfo

        writer.write_str_value("error", self.error)
        writer.write_bool_value("isCompleted", self.is_completed)
        writer.write_object_value("parseResult", self.parse_result)
        writer.write_float_value("progress", self.progress)
    

