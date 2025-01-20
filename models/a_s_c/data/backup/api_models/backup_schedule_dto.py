from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ....api.collections.item_key_value_pair.system.object.system.object import Object
    from .cron import Cron

@dataclass
class BackupScheduleDto(Parsable):
    """
    Backup schedule parameters
    """
    # Maximum number of the stored backup copies
    backups_stored: Optional[int] = None
    # Cron parameters
    cron_params: Optional[Cron] = None
    # Specifies if a dump will be created or not
    dump: Optional[bool] = None
    # Storage parameters
    storage_params: Optional[List[object]] = None
    # [0 - Documents, 1 - Thridparty documents, 2 - Custom cloud, 3 - Local, 4 - Data store, 5 - Thirdparty consumer]
    storage_type: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BackupScheduleDto:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BackupScheduleDto
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return BackupScheduleDto()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from ....api.collections.item_key_value_pair.system.object.system.object import Object
        from .cron import Cron

        from ....api.collections.item_key_value_pair.system.object.system.object import Object
        from .cron import Cron

        fields: Dict[str, Callable[[Any], None]] = {
            "backupsStored": lambda n : setattr(self, 'backups_stored', n.get_int_value()),
            "cronParams": lambda n : setattr(self, 'cron_params', n.get_object_value(Cron)),
            "dump": lambda n : setattr(self, 'dump', n.get_bool_value()),
            "storageParams": lambda n : setattr(self, 'storage_params', n.get_collection_of_object_values(Object)),
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
        from ....api.collections.item_key_value_pair.system.object.system.object import Object
        from .cron import Cron

        writer.write_int_value("backupsStored", self.backups_stored)
        writer.write_object_value("cronParams", self.cron_params)
        writer.write_bool_value("dump", self.dump)
        writer.write_collection_of_object_values("storageParams", self.storage_params)
        writer.write_int_value("storageType", self.storage_type)
    

