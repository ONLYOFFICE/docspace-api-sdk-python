from __future__ import annotations
import datetime
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .backup_ajax_handler_cron_params import BackupAjaxHandler_CronParams
    from .backup_ajax_handler_schedule_storage_params import BackupAjaxHandler_Schedule_storageParams

@dataclass
class BackupAjaxHandler_Schedule(Parsable):
    # The backupsStored property
    backups_stored: Optional[int] = None
    # The cronParams property
    cron_params: Optional[BackupAjaxHandler_CronParams] = None
    # The dump property
    dump: Optional[bool] = None
    # The lastBackupTime property
    last_backup_time: Optional[datetime.datetime] = None
    # The storageParams property
    storage_params: Optional[BackupAjaxHandler_Schedule_storageParams] = None
    # [0 - Documents, 1 - Thridparty documents, 2 - Custom cloud, 3 - Local, 4 - Data store, 5 - Thirdparty consumer]
    storage_type: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BackupAjaxHandler_Schedule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BackupAjaxHandler_Schedule
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return BackupAjaxHandler_Schedule()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .backup_ajax_handler_cron_params import BackupAjaxHandler_CronParams
        from .backup_ajax_handler_schedule_storage_params import BackupAjaxHandler_Schedule_storageParams

        from .backup_ajax_handler_cron_params import BackupAjaxHandler_CronParams
        from .backup_ajax_handler_schedule_storage_params import BackupAjaxHandler_Schedule_storageParams

        fields: Dict[str, Callable[[Any], None]] = {
            "backupsStored": lambda n : setattr(self, 'backups_stored', n.get_int_value()),
            "cronParams": lambda n : setattr(self, 'cron_params', n.get_object_value(BackupAjaxHandler_CronParams)),
            "dump": lambda n : setattr(self, 'dump', n.get_bool_value()),
            "lastBackupTime": lambda n : setattr(self, 'last_backup_time', n.get_datetime_value()),
            "storageParams": lambda n : setattr(self, 'storage_params', n.get_object_value(BackupAjaxHandler_Schedule_storageParams)),
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
        from .backup_ajax_handler_cron_params import BackupAjaxHandler_CronParams
        from .backup_ajax_handler_schedule_storage_params import BackupAjaxHandler_Schedule_storageParams

        writer.write_int_value("backupsStored", self.backups_stored)
        writer.write_object_value("cronParams", self.cron_params)
        writer.write_bool_value("dump", self.dump)
        writer.write_datetime_value("lastBackupTime", self.last_backup_time)
        writer.write_object_value("storageParams", self.storage_params)
        writer.write_int_value("storageType", self.storage_type)
    

