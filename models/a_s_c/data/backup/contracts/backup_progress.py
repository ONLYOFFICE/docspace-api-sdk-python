from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

@dataclass
class BackupProgress(Parsable):
    # [0 - Backup, 1 - Restore, 2 - Transfer]
    backup_progress_enum: Optional[int] = None
    # The error property
    error: Optional[str] = None
    # The isCompleted property
    is_completed: Optional[bool] = None
    # The link property
    link: Optional[str] = None
    # The progress property
    progress: Optional[int] = None
    # The taskId property
    task_id: Optional[str] = None
    # The tenantId property
    tenant_id: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BackupProgress:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BackupProgress
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return BackupProgress()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "backupProgressEnum": lambda n : setattr(self, 'backup_progress_enum', n.get_int_value()),
            "error": lambda n : setattr(self, 'error', n.get_str_value()),
            "isCompleted": lambda n : setattr(self, 'is_completed', n.get_bool_value()),
            "link": lambda n : setattr(self, 'link', n.get_str_value()),
            "progress": lambda n : setattr(self, 'progress', n.get_int_value()),
            "taskId": lambda n : setattr(self, 'task_id', n.get_str_value()),
            "tenantId": lambda n : setattr(self, 'tenant_id', n.get_int_value()),
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
        writer.write_int_value("backupProgressEnum", self.backup_progress_enum)
        writer.write_str_value("error", self.error)
        writer.write_bool_value("isCompleted", self.is_completed)
        writer.write_str_value("link", self.link)
        writer.write_int_value("progress", self.progress)
        writer.write_str_value("taskId", self.task_id)
        writer.write_int_value("tenantId", self.tenant_id)
    

