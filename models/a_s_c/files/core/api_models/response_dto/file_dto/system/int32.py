from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .......api.core.api_date_time import ApiDateTime
    from .......web.api.models.employee_dto import EmployeeDto
    from ...draft_location.system.int32 import Int32
    from .int32_available_external_rights import Int32_availableExternalRights
    from .int32_security import Int32_security
    from .int32_view_accessibility import Int32_viewAccessibility

@dataclass
class Int32(Parsable):
    # [0 - None, 1 - Read and write, 2 - Read, 3 - Restrict, 4 - Varies, 5 - Review, 6 - Comment, 7 - Fill forms, 8 - Custom filter, 9 - Room manager, 10 - Editing, 11 - Content creator]
    access: Optional[int] = None
    # The autoDelete property
    auto_delete: Optional[ApiDateTime] = None
    # Available external rights
    available_external_rights: Optional[Int32_availableExternalRights] = None
    # Can share
    can_share: Optional[bool] = None
    # Comment
    comment: Optional[str] = None
    # Content length
    content_length: Optional[str] = None
    # The created property
    created: Optional[ApiDateTime] = None
    # The createdBy property
    created_by: Optional[EmployeeDto] = None
    # The draftLocation property
    draft_location: Optional[Int32] = None
    # Encrypted or not
    encrypted: Optional[bool] = None
    # The expired property
    expired: Optional[ApiDateTime] = None
    # The fileEntryType property
    file_entry_type: Optional[int] = None
    # File extension
    file_exst: Optional[str] = None
    # [0 - None, 1 - Is editing, 2 - Is new, 4 - Is converting, 8 - Is original, 16 - Is editing alone, 32 - Is favorite, 64 - Is template, 128 - Is fill form draft]
    file_status: Optional[int] = None
    # [0 - Unknown, 1 - Archive, 2 - Video, 3 - Audio, 4 - Image, 5 - Spreadsheet, 6 - Presentation, 7 - Document, 10 - Pdf]
    file_type: Optional[int] = None
    # Folder ID
    folder_id: Optional[int] = None
    # Is there a draft or not
    has_draft: Optional[bool] = None
    # Id
    id: Optional[int] = None
    # InProcess folder ID
    in_process_folder_id: Optional[int] = None
    # InProcess folder title
    in_process_folder_title: Optional[str] = None
    # Is there a form or not
    is_form: Optional[bool] = None
    # The lastOpened property
    last_opened: Optional[ApiDateTime] = None
    # Locked or not
    locked: Optional[bool] = None
    # User ID who locked a file
    locked_by: Optional[str] = None
    # Muted or not
    mute: Optional[bool] = None
    # Order
    order: Optional[str] = None
    # Origin id
    origin_id: Optional[int] = None
    # Origin room id
    origin_room_id: Optional[int] = None
    # Origin room title
    origin_room_title: Optional[str] = None
    # Origin title
    origin_title: Optional[str] = None
    # [0 - Default, 1 - Coomon, 2 - Bunch, 3 - Trash, 5 - User, 6 - Share, 8 - Projects, 10 - Favourites, 11 - Recent, 12 - Templates, 13 - Privacy, 14 - Virtual rooms, 15 - Filling forms room, 16 - Editing room, 19 - Custom room, 20 - Archive, 21 - Thirdparty backup, 22 - Public room, 25 - Ready form folder, 26 - In process form folder, 27 - Form filling folder done, 28 - Form filling folder in progress, 29 - Virtual Data Room]
    parent_room_type: Optional[int] = None
    # Provider ID
    provider_id: Optional[int] = None
    # Provider is specified or not
    provider_item: Optional[bool] = None
    # Provider key
    provider_key: Optional[str] = None
    # Pure content length
    pure_content_length: Optional[int] = None
    # The requestToken property
    request_token: Optional[str] = None
    # Root folder id
    root_folder_id: Optional[int] = None
    # [0 - Default, 1 - Coomon, 2 - Bunch, 3 - Trash, 5 - User, 6 - Share, 8 - Projects, 10 - Favourites, 11 - Recent, 12 - Templates, 13 - Privacy, 14 - Virtual rooms, 15 - Filling forms room, 16 - Editing room, 19 - Custom room, 20 - Archive, 21 - Thirdparty backup, 22 - Public room, 25 - Ready form folder, 26 - In process form folder, 27 - Form filling folder done, 28 - Form filling folder in progress, 29 - Virtual Data Room]
    root_folder_type: Optional[int] = None
    # Security
    security: Optional[Int32_security] = None
    # Specifies if the file is shared or not
    shared: Optional[bool] = None
    # Specifies if the filling has started or not
    start_filling: Optional[bool] = None
    # [0 - Waiting, 1 - Created, 2 - Error, 3 - Not required, 4 - Creating]
    thumbnail_status: Optional[int] = None
    # Thumbnail URL
    thumbnail_url: Optional[str] = None
    # Title
    title: Optional[str] = None
    # The updated property
    updated: Optional[ApiDateTime] = None
    # The updatedBy property
    updated_by: Optional[EmployeeDto] = None
    # Version
    version: Optional[int] = None
    # Version group
    version_group: Optional[int] = None
    # File accessibility
    view_accessibility: Optional[Int32_viewAccessibility] = None
    # URL to view a file
    view_url: Optional[str] = None
    # Web URL
    web_url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Int32:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Int32
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Int32()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from .......api.core.api_date_time import ApiDateTime
        from .......web.api.models.employee_dto import EmployeeDto
        from ...draft_location.system.int32 import Int32
        from .int32_available_external_rights import Int32_availableExternalRights
        from .int32_security import Int32_security
        from .int32_view_accessibility import Int32_viewAccessibility

        from .......api.core.api_date_time import ApiDateTime
        from .......web.api.models.employee_dto import EmployeeDto
        from ...draft_location.system.int32 import Int32
        from .int32_available_external_rights import Int32_availableExternalRights
        from .int32_security import Int32_security
        from .int32_view_accessibility import Int32_viewAccessibility

        fields: Dict[str, Callable[[Any], None]] = {
            "access": lambda n : setattr(self, 'access', n.get_int_value()),
            "autoDelete": lambda n : setattr(self, 'auto_delete', n.get_object_value(ApiDateTime)),
            "availableExternalRights": lambda n : setattr(self, 'available_external_rights', n.get_object_value(Int32_availableExternalRights)),
            "canShare": lambda n : setattr(self, 'can_share', n.get_bool_value()),
            "comment": lambda n : setattr(self, 'comment', n.get_str_value()),
            "contentLength": lambda n : setattr(self, 'content_length', n.get_str_value()),
            "created": lambda n : setattr(self, 'created', n.get_object_value(ApiDateTime)),
            "createdBy": lambda n : setattr(self, 'created_by', n.get_object_value(EmployeeDto)),
            "draftLocation": lambda n : setattr(self, 'draft_location', n.get_object_value(Int32)),
            "encrypted": lambda n : setattr(self, 'encrypted', n.get_bool_value()),
            "expired": lambda n : setattr(self, 'expired', n.get_object_value(ApiDateTime)),
            "fileEntryType": lambda n : setattr(self, 'file_entry_type', n.get_int_value()),
            "fileExst": lambda n : setattr(self, 'file_exst', n.get_str_value()),
            "fileStatus": lambda n : setattr(self, 'file_status', n.get_int_value()),
            "fileType": lambda n : setattr(self, 'file_type', n.get_int_value()),
            "folderId": lambda n : setattr(self, 'folder_id', n.get_int_value()),
            "hasDraft": lambda n : setattr(self, 'has_draft', n.get_bool_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "inProcessFolderId": lambda n : setattr(self, 'in_process_folder_id', n.get_int_value()),
            "inProcessFolderTitle": lambda n : setattr(self, 'in_process_folder_title', n.get_str_value()),
            "isForm": lambda n : setattr(self, 'is_form', n.get_bool_value()),
            "lastOpened": lambda n : setattr(self, 'last_opened', n.get_object_value(ApiDateTime)),
            "locked": lambda n : setattr(self, 'locked', n.get_bool_value()),
            "lockedBy": lambda n : setattr(self, 'locked_by', n.get_str_value()),
            "mute": lambda n : setattr(self, 'mute', n.get_bool_value()),
            "order": lambda n : setattr(self, 'order', n.get_str_value()),
            "originId": lambda n : setattr(self, 'origin_id', n.get_int_value()),
            "originRoomId": lambda n : setattr(self, 'origin_room_id', n.get_int_value()),
            "originRoomTitle": lambda n : setattr(self, 'origin_room_title', n.get_str_value()),
            "originTitle": lambda n : setattr(self, 'origin_title', n.get_str_value()),
            "parentRoomType": lambda n : setattr(self, 'parent_room_type', n.get_int_value()),
            "providerId": lambda n : setattr(self, 'provider_id', n.get_int_value()),
            "providerItem": lambda n : setattr(self, 'provider_item', n.get_bool_value()),
            "providerKey": lambda n : setattr(self, 'provider_key', n.get_str_value()),
            "pureContentLength": lambda n : setattr(self, 'pure_content_length', n.get_int_value()),
            "requestToken": lambda n : setattr(self, 'request_token', n.get_str_value()),
            "rootFolderId": lambda n : setattr(self, 'root_folder_id', n.get_int_value()),
            "rootFolderType": lambda n : setattr(self, 'root_folder_type', n.get_int_value()),
            "security": lambda n : setattr(self, 'security', n.get_object_value(Int32_security)),
            "shared": lambda n : setattr(self, 'shared', n.get_bool_value()),
            "startFilling": lambda n : setattr(self, 'start_filling', n.get_bool_value()),
            "thumbnailStatus": lambda n : setattr(self, 'thumbnail_status', n.get_int_value()),
            "thumbnailUrl": lambda n : setattr(self, 'thumbnail_url', n.get_str_value()),
            "title": lambda n : setattr(self, 'title', n.get_str_value()),
            "updated": lambda n : setattr(self, 'updated', n.get_object_value(ApiDateTime)),
            "updatedBy": lambda n : setattr(self, 'updated_by', n.get_object_value(EmployeeDto)),
            "version": lambda n : setattr(self, 'version', n.get_int_value()),
            "versionGroup": lambda n : setattr(self, 'version_group', n.get_int_value()),
            "viewAccessibility": lambda n : setattr(self, 'view_accessibility', n.get_object_value(Int32_viewAccessibility)),
            "viewUrl": lambda n : setattr(self, 'view_url', n.get_str_value()),
            "webUrl": lambda n : setattr(self, 'web_url', n.get_str_value()),
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
        from ...draft_location.system.int32 import Int32
        from .int32_available_external_rights import Int32_availableExternalRights
        from .int32_security import Int32_security
        from .int32_view_accessibility import Int32_viewAccessibility

        writer.write_int_value("access", self.access)
        writer.write_object_value("autoDelete", self.auto_delete)
        writer.write_object_value("availableExternalRights", self.available_external_rights)
        writer.write_bool_value("canShare", self.can_share)
        writer.write_str_value("comment", self.comment)
        writer.write_str_value("contentLength", self.content_length)
        writer.write_object_value("created", self.created)
        writer.write_object_value("createdBy", self.created_by)
        writer.write_int_value("draftLocation", self.draft_location)
        writer.write_bool_value("encrypted", self.encrypted)
        writer.write_object_value("expired", self.expired)
        writer.write_int_value("fileEntryType", self.file_entry_type)
        writer.write_str_value("fileExst", self.file_exst)
        writer.write_int_value("fileStatus", self.file_status)
        writer.write_int_value("fileType", self.file_type)
        writer.write_int_value("folderId", self.folder_id)
        writer.write_bool_value("hasDraft", self.has_draft)
        writer.write_int_value("id", self.id)
        writer.write_int_value("inProcessFolderId", self.in_process_folder_id)
        writer.write_str_value("inProcessFolderTitle", self.in_process_folder_title)
        writer.write_bool_value("isForm", self.is_form)
        writer.write_object_value("lastOpened", self.last_opened)
        writer.write_bool_value("locked", self.locked)
        writer.write_str_value("lockedBy", self.locked_by)
        writer.write_bool_value("mute", self.mute)
        writer.write_str_value("order", self.order)
        writer.write_int_value("originId", self.origin_id)
        writer.write_int_value("originRoomId", self.origin_room_id)
        writer.write_str_value("originRoomTitle", self.origin_room_title)
        writer.write_str_value("originTitle", self.origin_title)
        writer.write_int_value("parentRoomType", self.parent_room_type)
        writer.write_int_value("providerId", self.provider_id)
        writer.write_bool_value("providerItem", self.provider_item)
        writer.write_str_value("providerKey", self.provider_key)
        writer.write_int_value("pureContentLength", self.pure_content_length)
        writer.write_str_value("requestToken", self.request_token)
        writer.write_int_value("rootFolderId", self.root_folder_id)
        writer.write_int_value("rootFolderType", self.root_folder_type)
        writer.write_object_value("security", self.security)
        writer.write_bool_value("shared", self.shared)
        writer.write_bool_value("startFilling", self.start_filling)
        writer.write_int_value("thumbnailStatus", self.thumbnail_status)
        writer.write_str_value("thumbnailUrl", self.thumbnail_url)
        writer.write_str_value("title", self.title)
        writer.write_object_value("updated", self.updated)
        writer.write_object_value("updatedBy", self.updated_by)
        writer.write_int_value("version", self.version)
        writer.write_int_value("versionGroup", self.version_group)
        writer.write_object_value("viewAccessibility", self.view_accessibility)
        writer.write_str_value("viewUrl", self.view_url)
        writer.write_str_value("webUrl", self.web_url)
    

