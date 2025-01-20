from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....api.core.api_date_time import ApiDateTime
    from .....web.api.models.employee_dto import EmployeeDto

@dataclass
class FileEntryDto(Parsable):
    # [0 - None, 1 - Read and write, 2 - Read, 3 - Restrict, 4 - Varies, 5 - Review, 6 - Comment, 7 - Fill forms, 8 - Custom filter, 9 - Room manager, 10 - Editing, 11 - Content creator]
    access: Optional[int] = None
    # The autoDelete property
    auto_delete: Optional[ApiDateTime] = None
    # The created property
    created: Optional[ApiDateTime] = None
    # The createdBy property
    created_by: Optional[EmployeeDto] = None
    # The fileEntryType property
    file_entry_type: Optional[int] = None
    # Order
    order: Optional[str] = None
    # [0 - Default, 1 - Coomon, 2 - Bunch, 3 - Trash, 5 - User, 6 - Share, 8 - Projects, 10 - Favourites, 11 - Recent, 12 - Templates, 13 - Privacy, 14 - Virtual rooms, 15 - Filling forms room, 16 - Editing room, 19 - Custom room, 20 - Archive, 21 - Thirdparty backup, 22 - Public room, 25 - Ready form folder, 26 - In process form folder, 27 - Form filling folder done, 28 - Form filling folder in progress, 29 - Virtual Data Room]
    parent_room_type: Optional[int] = None
    # Provider ID
    provider_id: Optional[int] = None
    # Provider is specified or not
    provider_item: Optional[bool] = None
    # Provider key
    provider_key: Optional[str] = None
    # [0 - Default, 1 - Coomon, 2 - Bunch, 3 - Trash, 5 - User, 6 - Share, 8 - Projects, 10 - Favourites, 11 - Recent, 12 - Templates, 13 - Privacy, 14 - Virtual rooms, 15 - Filling forms room, 16 - Editing room, 19 - Custom room, 20 - Archive, 21 - Thirdparty backup, 22 - Public room, 25 - Ready form folder, 26 - In process form folder, 27 - Form filling folder done, 28 - Form filling folder in progress, 29 - Virtual Data Room]
    root_folder_type: Optional[int] = None
    # Specifies if the file is shared or not
    shared: Optional[bool] = None
    # Title
    title: Optional[str] = None
    # The updated property
    updated: Optional[ApiDateTime] = None
    # The updatedBy property
    updated_by: Optional[EmployeeDto] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> FileEntryDto:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FileEntryDto
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return FileEntryDto()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .....api.core.api_date_time import ApiDateTime
        from .....web.api.models.employee_dto import EmployeeDto

        from .....api.core.api_date_time import ApiDateTime
        from .....web.api.models.employee_dto import EmployeeDto

        fields: Dict[str, Callable[[Any], None]] = {
            "access": lambda n : setattr(self, 'access', n.get_int_value()),
            "autoDelete": lambda n : setattr(self, 'auto_delete', n.get_object_value(ApiDateTime)),
            "created": lambda n : setattr(self, 'created', n.get_object_value(ApiDateTime)),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(EmployeeDto)),
            "fileEntryType": lambda n : setattr(self, 'file_entry_type', n.get_int_value()),
            "order": lambda n : setattr(self, 'order', n.get_str_value()),
            "parentRoomType": lambda n : setattr(self, 'parent_room_type', n.get_int_value()),
            "providerId": lambda n : setattr(self, 'provider_id', n.get_int_value()),
            "providerItem": lambda n : setattr(self, 'provider_item', n.get_bool_value()),
            "providerKey": lambda n : setattr(self, 'provider_key', n.get_str_value()),
            "rootFolderType": lambda n : setattr(self, 'root_folder_type', n.get_int_value()),
            "shared": lambda n : setattr(self, 'shared', n.get_bool_value()),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
            "updated": lambda n : setattr(self, 'updated', n.get_object_value(ApiDateTime)),
            "updatedBy": lambda n : setattr(self, 'updated_by', n.get_object_value(EmployeeDto)),
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
        from .....web.api.models.employee_dto import EmployeeDto

        writer.write_int_value("access", self.access)
        writer.write_object_value("autoDelete", self.auto_delete)
        writer.write_object_value("created", self.created)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_int_value("fileEntryType", self.file_entry_type)
        writer.write_str_value("order", self.order)
        writer.write_int_value("parentRoomType", self.parent_room_type)
        writer.write_int_value("providerId", self.provider_id)
        writer.write_bool_value("providerItem", self.provider_item)
        writer.write_str_value("providerKey", self.provider_key)
        writer.write_int_value("rootFolderType", self.root_folder_type)
        writer.write_bool_value("shared", self.shared)
        writer.write_str_value("title", self.title)
        writer.write_object_value("updated", self.updated)
        writer.write_object_value("updatedBy", self.updated_by)
    

