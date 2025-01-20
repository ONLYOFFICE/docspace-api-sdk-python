from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

@dataclass
class BackupHistoryRecord(Parsable):
    # The createdOn property
    created_on: Optional[datetime.datetime] = None
    # The expiresOn property
    expires_on: Optional[datetime.datetime] = None
    # The fileName property
    file_name: Optional[str] = None
    # The id property
    id: Optional[UUID] = None
    # [0 - Documents, 1 - Thridparty documents, 2 - Custom cloud, 3 - Local, 4 - Data store, 5 - Thirdparty consumer]
    storage_type: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BackupHistoryRecord:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BackupHistoryRecord
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return BackupHistoryRecord()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        fields: Dict[str, Callable[[Any], None]] = {
            "createdOn": lambda n : setattr(self, 'created_on', n.get_datetime_value()),
            "expiresOn": lambda n : setattr(self, 'expires_on', n.get_datetime_value()),
            "fileName": lambda n : setattr(self, 'file_name', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_uuid_value()),
            "storageType": lambda n : setattr(self, 'storage_type', n.get_int_value()),
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
        writer.write_datetime_value("createdOn", self.created_on)
        writer.write_datetime_value("expiresOn", self.expires_on)
        writer.write_str_value("fileName", self.file_name)
        writer.write_uuid_value("id", self.id)
        writer.write_int_value("storageType", self.storage_type)
    

