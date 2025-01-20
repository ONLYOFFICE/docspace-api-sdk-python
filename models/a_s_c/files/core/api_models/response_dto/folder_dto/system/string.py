from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .......api.core.api_date_time import ApiDateTime
    from .......web.api.models.employee_dto import EmployeeDto
    from .....virtual_rooms.logo import Logo
    from ....room_data_lifetime_dto import RoomDataLifetimeDto
    from ...watermark_dto import WatermarkDto
    from .string_security import String_security

@dataclass
class String(Parsable):
    # [0 - None, 1 - Read and write, 2 - Read, 3 - Restrict, 4 - Varies, 5 - Review, 6 - Comment, 7 - Fill forms, 8 - Custom filter, 9 - Room manager, 10 - Editing, 11 - Content creator]
    access: Optional[int] = None
    # The autoDelete property
    auto_delete: Optional[ApiDateTime] = None
    # Can share
    can_share: Optional[bool] = None
    # The created property
    created: Optional[ApiDateTime] = None
    # The createdBy property
    created_by: Optional[EmployeeDto] = None
    # Deny download
    deny_download: Optional[bool] = None
    # Expired
    expired: Optional[bool] = None
    # Specifies if the link external
    external: Optional[bool] = None
    # The fileEntryType property
    file_entry_type: Optional[int] = None
    # Number of files
    files_count: Optional[int] = None
    # Number of folders
    folders_count: Optional[int] = None
    # Id
    id: Optional[String] = None
    # InRoom
    in_room: Optional[bool] = None
    # Indexing
    indexing: Optional[bool] = None
    # Specifies if the room has a custom quota or not
    is_custom_quota: Optional[bool] = None
    # Specifies if a folder is favorite or not
    is_favorite: Optional[bool] = None
    # Specifies if a folder is shareable or not
    is_shareable: Optional[bool] = None
    # The lifetime property
    lifetime: Optional[RoomDataLifetimeDto] = None
    # The logo property
    logo: Optional[Logo] = None
    # Specifies if a folder is muted or not
    mute: Optional[bool] = None
    # Number for a new folder
    new: Optional[int] = None
    # Order
    order: Optional[String] = None
    # Origin id
    origin_id: Optional[String] = None
    # Origin room id
    origin_room_id: Optional[String] = None
    # Origin room title
    origin_room_title: Optional[String] = None
    # Origin title
    origin_title: Optional[String] = None
    # Parent folder ID
    parent_id: Optional[String] = None
    # [0 - Default, 1 - Coomon, 2 - Bunch, 3 - Trash, 5 - User, 6 - Share, 8 - Projects, 10 - Favourites, 11 - Recent, 12 - Templates, 13 - Privacy, 14 - Virtual rooms, 15 - Filling forms room, 16 - Editing room, 19 - Custom room, 20 - Archive, 21 - Thirdparty backup, 22 - Public room, 25 - Ready form folder, 26 - In process form folder, 27 - Form filling folder done, 28 - Form filling folder in progress, 29 - Virtual Data Room]
    parent_room_type: Optional[int] = None
    # Specifies if the password protected
    password_protected: Optional[bool] = None
    # Specifies if a folder is pinned or not
    pinned: Optional[bool] = None
    # Specifies if a folder is private or not
    private: Optional[bool] = None
    # Provider ID
    provider_id: Optional[int] = None
    # Provider is specified or not
    provider_item: Optional[bool] = None
    # Provider key
    provider_key: Optional[String] = None
    # Quota
    quota_limit: Optional[int] = None
    # The requestToken property
    request_token: Optional[String] = None
    # [1 - Form filling room, 2 - Collaboration room, 5 - Custom room, 6 - Public room, 8 - Virtual data room]
    room_type: Optional[int] = None
    # Root folder id
    root_folder_id: Optional[String] = None
    # [0 - Default, 1 - Coomon, 2 - Bunch, 3 - Trash, 5 - User, 6 - Share, 8 - Projects, 10 - Favourites, 11 - Recent, 12 - Templates, 13 - Privacy, 14 - Virtual rooms, 15 - Filling forms room, 16 - Editing room, 19 - Custom room, 20 - Archive, 21 - Thirdparty backup, 22 - Public room, 25 - Ready form folder, 26 - In process form folder, 27 - Form filling folder done, 28 - Form filling folder in progress, 29 - Virtual Data Room]
    root_folder_type: Optional[int] = None
    # Security
    security: Optional[String_security] = None
    # Specifies if the file is shared or not
    shared: Optional[bool] = None
    # List of tags
    tags: Optional[List[String]] = None
    # Title
    title: Optional[String] = None
    # [0 - Default, 1 - Coomon, 2 - Bunch, 3 - Trash, 5 - User, 6 - Share, 8 - Projects, 10 - Favourites, 11 - Recent, 12 - Templates, 13 - Privacy, 14 - Virtual rooms, 15 - Filling forms room, 16 - Editing room, 19 - Custom room, 20 - Archive, 21 - Thirdparty backup, 22 - Public room, 25 - Ready form folder, 26 - In process form folder, 27 - Form filling folder done, 28 - Form filling folder in progress, 29 - Virtual Data Room]
    type: Optional[int] = None
    # The updated property
    updated: Optional[ApiDateTime] = None
    # The updatedBy property
    updated_by: Optional[EmployeeDto] = None
    # Counter
    used_space: Optional[int] = None
    # The watermark property
    watermark: Optional[WatermarkDto] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> String:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: String
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return String()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .......api.core.api_date_time import ApiDateTime
        from .......web.api.models.employee_dto import EmployeeDto
        from .....virtual_rooms.logo import Logo
        from ....room_data_lifetime_dto import RoomDataLifetimeDto
        from ...watermark_dto import WatermarkDto
        from .string_security import String_security

        from .......api.core.api_date_time import ApiDateTime
        from .......web.api.models.employee_dto import EmployeeDto
        from .....virtual_rooms.logo import Logo
        from ....room_data_lifetime_dto import RoomDataLifetimeDto
        from ...watermark_dto import WatermarkDto
        from .string_security import String_security

        fields: Dict[str, Callable[[Any], None]] = {
            "access": lambda n : setattr(self, 'access', n.get_int_value()),
            "autoDelete": lambda n : setattr(self, 'auto_delete', n.get_object_value(ApiDateTime)),
            "canShare": lambda n : setattr(self, 'can_share', n.get_bool_value()),
            "created": lambda n : setattr(self, 'created', n.get_object_value(ApiDateTime)),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(EmployeeDto)),
            "denyDownload": lambda n : setattr(self, 'deny_download', n.get_bool_value()),
            "expired": lambda n : setattr(self, 'expired', n.get_bool_value()),
            "external": lambda n : setattr(self, 'external', n.get_bool_value()),
            "fileEntryType": lambda n : setattr(self, 'file_entry_type', n.get_int_value()),
            "filesCount": lambda n : setattr(self, 'files_count', n.get_int_value()),
            "foldersCount": lambda n : setattr(self, 'folders_count', n.get_int_value()),
            "id": lambda n : setattr(self, 'id', n.get_object_value(String)),
            "inRoom": lambda n : setattr(self, 'in_room', n.get_bool_value()),
            "indexing": lambda n : setattr(self, 'indexing', n.get_bool_value()),
            "isCustomQuota": lambda n : setattr(self, 'is_custom_quota', n.get_bool_value()),
            "isFavorite": lambda n : setattr(self, 'is_favorite', n.get_bool_value()),
            "isShareable": lambda n : setattr(self, 'is_shareable', n.get_bool_value()),
            "lifetime": lambda n : setattr(self, 'lifetime', n.get_object_value(RoomDataLifetimeDto)),
            "logo": lambda n : setattr(self, 'logo', n.get_object_value(Logo)),
            "mute": lambda n : setattr(self, 'mute', n.get_bool_value()),
            "new": lambda n : setattr(self, 'new', n.get_int_value()),
            "order": lambda n : setattr(self, 'order', n.get_object_value(String)),
            "originId": lambda n : setattr(self, 'origin_id', n.get_object_value(String)),
            "originRoomId": lambda n : setattr(self, 'origin_room_id', n.get_object_value(String)),
            "originRoomTitle": lambda n : setattr(self, 'origin_room_title', n.get_object_value(String)),
            "originTitle": lambda n : setattr(self, 'origin_title', n.get_object_value(String)),
            "parentId": lambda n : setattr(self, 'parent_id', n.get_object_value(String)),
            "parentRoomType": lambda n : setattr(self, 'parent_room_type', n.get_int_value()),
            "passwordProtected": lambda n : setattr(self, 'password_protected', n.get_bool_value()),
            "pinned": lambda n : setattr(self, 'pinned', n.get_bool_value()),
            "private": lambda n : setattr(self, 'private', n.get_bool_value()),
            "providerId": lambda n : setattr(self, 'provider_id', n.get_int_value()),
            "providerItem": lambda n : setattr(self, 'provider_item', n.get_bool_value()),
            "providerKey": lambda n : setattr(self, 'provider_key', n.get_object_value(String)),
            "quotaLimit": lambda n : setattr(self, 'quota_limit', n.get_int_value()),
            "requestToken": lambda n : setattr(self, 'request_token', n.get_object_value(String)),
            "roomType": lambda n : setattr(self, 'room_type', n.get_int_value()),
            "rootFolderId": lambda n : setattr(self, 'root_folder_id', n.get_object_value(String)),
            "rootFolderType": lambda n : setattr(self, 'root_folder_type', n.get_int_value()),
            "security": lambda n : setattr(self, 'security', n.get_object_value(String_security)),
            "shared": lambda n : setattr(self, 'shared', n.get_bool_value()),
            "tags": lambda n : setattr(self, 'tags', n.get_collection_of_primitive_values(String)),
            "title": lambda n : setattr(self, 'title', n.get_object_value(String)),
            "type": lambda n : setattr(self, 'type', n.get_int_value()),
            "updated": lambda n : setattr(self, 'updated', n.get_object_value(ApiDateTime)),
            "updatedBy": lambda n : setattr(self, 'updated_by', n.get_object_value(EmployeeDto)),
            "usedSpace": lambda n : setattr(self, 'used_space', n.get_int_value()),
            "watermark": lambda n : setattr(self, 'watermark', n.get_object_value(WatermarkDto)),
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
        from .......api.core.api_date_time import ApiDateTime
        from .......web.api.models.employee_dto import EmployeeDto
        from .....virtual_rooms.logo import Logo
        from ....room_data_lifetime_dto import RoomDataLifetimeDto
        from ...watermark_dto import WatermarkDto
        from .string_security import String_security

        writer.write_int_value("access", self.access)
        writer.write_object_value("autoDelete", self.auto_delete)
        writer.write_bool_value("canShare", self.can_share)
        writer.write_object_value("created", self.created)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_bool_value("denyDownload", self.deny_download)
        writer.write_bool_value("expired", self.expired)
        writer.write_bool_value("external", self.external)
        writer.write_int_value("fileEntryType", self.file_entry_type)
        writer.write_int_value("filesCount", self.files_count)
        writer.write_int_value("foldersCount", self.folders_count)
        writer.write_str_value("id", self.id)
        writer.write_bool_value("inRoom", self.in_room)
        writer.write_bool_value("indexing", self.indexing)
        writer.write_bool_value("isCustomQuota", self.is_custom_quota)
        writer.write_bool_value("isFavorite", self.is_favorite)
        writer.write_bool_value("isShareable", self.is_shareable)
        writer.write_object_value("lifetime", self.lifetime)
        writer.write_object_value("logo", self.logo)
        writer.write_bool_value("mute", self.mute)
        writer.write_int_value("new", self.new)
        writer.write_str_value("order", self.order)
        writer.write_str_value("originId", self.origin_id)
        writer.write_str_value("originRoomId", self.origin_room_id)
        writer.write_str_value("originRoomTitle", self.origin_room_title)
        writer.write_str_value("originTitle", self.origin_title)
        writer.write_str_value("parentId", self.parent_id)
        writer.write_int_value("parentRoomType", self.parent_room_type)
        writer.write_bool_value("passwordProtected", self.password_protected)
        writer.write_bool_value("pinned", self.pinned)
        writer.write_bool_value("private", self.private)
        writer.write_int_value("providerId", self.provider_id)
        writer.write_bool_value("providerItem", self.provider_item)
        writer.write_str_value("providerKey", self.provider_key)
        writer.write_int_value("quotaLimit", self.quota_limit)
        writer.write_str_value("requestToken", self.request_token)
        writer.write_int_value("roomType", self.room_type)
        writer.write_str_value("rootFolderId", self.root_folder_id)
        writer.write_int_value("rootFolderType", self.root_folder_type)
        writer.write_object_value("security", self.security)
        writer.write_bool_value("shared", self.shared)
        writer.write_collection_of_primitive_values("tags", self.tags)
        writer.write_str_value("title", self.title)
        writer.write_int_value("type", self.type)
        writer.write_object_value("updated", self.updated)
        writer.write_object_value("updatedBy", self.updated_by)
        writer.write_int_value("usedSpace", self.used_space)
        writer.write_object_value("watermark", self.watermark)
    

