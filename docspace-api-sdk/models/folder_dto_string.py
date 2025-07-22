#
# (c) Copyright Ascensio System SIA 2025
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#



from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from docspace-api-sdk.models.api_date_time import ApiDateTime
from docspace-api-sdk.models.employee_dto import EmployeeDto
from docspace-api-sdk.models.file_dto_integer_security import FileDtoIntegerSecurity
from docspace-api-sdk.models.file_entry_type import FileEntryType
from docspace-api-sdk.models.file_share import FileShare
from docspace-api-sdk.models.folder_type import FolderType
from docspace-api-sdk.models.logo import Logo
from docspace-api-sdk.models.room_data_lifetime_dto import RoomDataLifetimeDto
from docspace-api-sdk.models.room_type import RoomType
from docspace-api-sdk.models.watermark_dto import WatermarkDto
from typing import Optional, Set
from typing_extensions import Self

class FolderDtoString(BaseModel):
    """
    The folder parameters.
    """ # noqa: E501
    title: Optional[StrictStr] = Field(default=None, description="The file entry title.")
    access: Optional[FileShare] = None
    shared: Optional[StrictBool] = Field(default=None, description="Specifies if the file entry is shared or not.")
    created: Optional[ApiDateTime] = None
    created_by: Optional[EmployeeDto] = Field(default=None, alias="createdBy")
    updated: Optional[ApiDateTime] = None
    auto_delete: Optional[ApiDateTime] = Field(default=None, alias="autoDelete")
    root_folder_type: Optional[FolderType] = Field(default=None, alias="rootFolderType")
    parent_room_type: Optional[FolderType] = Field(default=None, alias="parentRoomType")
    updated_by: Optional[EmployeeDto] = Field(default=None, alias="updatedBy")
    provider_item: Optional[StrictBool] = Field(default=None, description="Specifies if the file entry provider is specified or not.", alias="providerItem")
    provider_key: Optional[StrictStr] = Field(default=None, description="The provider key of the file entry.", alias="providerKey")
    provider_id: Optional[StrictInt] = Field(default=None, description="The provider ID of the file entry.", alias="providerId")
    order: Optional[StrictStr] = Field(default=None, description="The order of the file entry.")
    id: Optional[StrictStr] = Field(default=None, description="The file entry ID.")
    root_folder_id: Optional[StrictStr] = Field(default=None, description="The root folder ID of the file entry.", alias="rootFolderId")
    origin_id: Optional[StrictStr] = Field(default=None, description="The origin ID of the file entry.", alias="originId")
    origin_room_id: Optional[StrictStr] = Field(default=None, description="The origin room ID of the file entry.", alias="originRoomId")
    origin_title: Optional[StrictStr] = Field(default=None, description="The origin title of the file entry.", alias="originTitle")
    origin_room_title: Optional[StrictStr] = Field(default=None, description="The origin room title of the file entry.", alias="originRoomTitle")
    can_share: Optional[StrictBool] = Field(default=None, description="Specifies if the file entry can be shared or not.", alias="canShare")
    security: Optional[FileDtoIntegerSecurity] = None
    request_token: Optional[StrictStr] = Field(default=None, description="The request token of the file entry.", alias="requestToken")
    parent_id: Optional[StrictStr] = Field(default=None, description="The parent folder ID of the folder.", alias="parentId")
    files_count: Optional[StrictInt] = Field(default=None, description="The number of files that the folder contains.", alias="filesCount")
    folders_count: Optional[StrictInt] = Field(default=None, description="The number of folders that the folder contains.", alias="foldersCount")
    is_shareable: Optional[StrictBool] = Field(default=None, description="Specifies if the folder can be shared or not.", alias="isShareable")
    is_favorite: Optional[StrictBool] = Field(default=None, description="Specifies if the folder is favorite or not.", alias="isFavorite")
    new: Optional[StrictInt] = Field(default=None, description="The new element index in the folder.")
    mute: Optional[StrictBool] = Field(default=None, description="Specifies if the folder notifications are enabled or not.")
    tags: Optional[List[StrictStr]] = Field(default=None, description="The list of tags of the folder.")
    logo: Optional[Logo] = None
    pinned: Optional[StrictBool] = Field(default=None, description="Specifies if the folder is pinned or not.")
    room_type: Optional[RoomType] = Field(default=None, alias="roomType")
    private: Optional[StrictBool] = Field(default=None, description="Specifies if the folder is private or not.")
    indexing: Optional[StrictBool] = Field(default=None, description="Specifies if the folder is indexed or not.")
    deny_download: Optional[StrictBool] = Field(default=None, description="Specifies if the folder can be downloaded or not.", alias="denyDownload")
    lifetime: Optional[RoomDataLifetimeDto] = None
    watermark: Optional[WatermarkDto] = None
    type: Optional[FolderType] = None
    in_room: Optional[StrictBool] = Field(default=None, description="Specifies if the folder is placed in the room or not.", alias="inRoom")
    quota_limit: Optional[StrictInt] = Field(default=None, description="The folder quota limit.", alias="quotaLimit")
    is_custom_quota: Optional[StrictBool] = Field(default=None, description="Specifies if the folder room has a custom quota or not.", alias="isCustomQuota")
    used_space: Optional[StrictInt] = Field(default=None, description="How much folder space is used (counter).", alias="usedSpace")
    external: Optional[StrictBool] = Field(default=None, description="Specifies if the folder can be accessed via an external link or not.")
    password_protected: Optional[StrictBool] = Field(default=None, description="Specifies if the folder is password protected or not.", alias="passwordProtected")
    expired: Optional[StrictBool] = Field(default=None, description="Specifies if an external link to the folder is expired or not.")
    file_entry_type: Optional[FileEntryType] = Field(default=None, alias="fileEntryType")
    __properties: ClassVar[List[str]] = ["title", "access", "shared", "created", "createdBy", "updated", "autoDelete", "rootFolderType", "parentRoomType", "updatedBy", "providerItem", "providerKey", "providerId", "order", "id", "rootFolderId", "originId", "originRoomId", "originTitle", "originRoomTitle", "canShare", "security", "requestToken", "parentId", "filesCount", "foldersCount", "isShareable", "isFavorite", "new", "mute", "tags", "logo", "pinned", "roomType", "private", "indexing", "denyDownload", "lifetime", "watermark", "type", "inRoom", "quotaLimit", "isCustomQuota", "usedSpace", "external", "passwordProtected", "expired", "fileEntryType"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of FolderDtoString from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of created
        if self.created:
            _dict['created'] = self.created.to_dict()
        # override the default output from pydantic by calling `to_dict()` of created_by
        if self.created_by:
            _dict['createdBy'] = self.created_by.to_dict()
        # override the default output from pydantic by calling `to_dict()` of updated
        if self.updated:
            _dict['updated'] = self.updated.to_dict()
        # override the default output from pydantic by calling `to_dict()` of auto_delete
        if self.auto_delete:
            _dict['autoDelete'] = self.auto_delete.to_dict()
        # override the default output from pydantic by calling `to_dict()` of updated_by
        if self.updated_by:
            _dict['updatedBy'] = self.updated_by.to_dict()
        # override the default output from pydantic by calling `to_dict()` of security
        if self.security:
            _dict['security'] = self.security.to_dict()
        # override the default output from pydantic by calling `to_dict()` of logo
        if self.logo:
            _dict['logo'] = self.logo.to_dict()
        # override the default output from pydantic by calling `to_dict()` of lifetime
        if self.lifetime:
            _dict['lifetime'] = self.lifetime.to_dict()
        # override the default output from pydantic by calling `to_dict()` of watermark
        if self.watermark:
            _dict['watermark'] = self.watermark.to_dict()
        # set to None if title (nullable) is None
        # and model_fields_set contains the field
        if self.title is None and "title" in self.model_fields_set:
            _dict['title'] = None

        # set to None if provider_item (nullable) is None
        # and model_fields_set contains the field
        if self.provider_item is None and "provider_item" in self.model_fields_set:
            _dict['providerItem'] = None

        # set to None if provider_key (nullable) is None
        # and model_fields_set contains the field
        if self.provider_key is None and "provider_key" in self.model_fields_set:
            _dict['providerKey'] = None

        # set to None if provider_id (nullable) is None
        # and model_fields_set contains the field
        if self.provider_id is None and "provider_id" in self.model_fields_set:
            _dict['providerId'] = None

        # set to None if order (nullable) is None
        # and model_fields_set contains the field
        if self.order is None and "order" in self.model_fields_set:
            _dict['order'] = None

        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if root_folder_id (nullable) is None
        # and model_fields_set contains the field
        if self.root_folder_id is None and "root_folder_id" in self.model_fields_set:
            _dict['rootFolderId'] = None

        # set to None if origin_id (nullable) is None
        # and model_fields_set contains the field
        if self.origin_id is None and "origin_id" in self.model_fields_set:
            _dict['originId'] = None

        # set to None if origin_room_id (nullable) is None
        # and model_fields_set contains the field
        if self.origin_room_id is None and "origin_room_id" in self.model_fields_set:
            _dict['originRoomId'] = None

        # set to None if origin_title (nullable) is None
        # and model_fields_set contains the field
        if self.origin_title is None and "origin_title" in self.model_fields_set:
            _dict['originTitle'] = None

        # set to None if origin_room_title (nullable) is None
        # and model_fields_set contains the field
        if self.origin_room_title is None and "origin_room_title" in self.model_fields_set:
            _dict['originRoomTitle'] = None

        # set to None if security (nullable) is None
        # and model_fields_set contains the field
        if self.security is None and "security" in self.model_fields_set:
            _dict['security'] = None

        # set to None if request_token (nullable) is None
        # and model_fields_set contains the field
        if self.request_token is None and "request_token" in self.model_fields_set:
            _dict['requestToken'] = None

        # set to None if parent_id (nullable) is None
        # and model_fields_set contains the field
        if self.parent_id is None and "parent_id" in self.model_fields_set:
            _dict['parentId'] = None

        # set to None if is_shareable (nullable) is None
        # and model_fields_set contains the field
        if self.is_shareable is None and "is_shareable" in self.model_fields_set:
            _dict['isShareable'] = None

        # set to None if is_favorite (nullable) is None
        # and model_fields_set contains the field
        if self.is_favorite is None and "is_favorite" in self.model_fields_set:
            _dict['isFavorite'] = None

        # set to None if tags (nullable) is None
        # and model_fields_set contains the field
        if self.tags is None and "tags" in self.model_fields_set:
            _dict['tags'] = None

        # set to None if in_room (nullable) is None
        # and model_fields_set contains the field
        if self.in_room is None and "in_room" in self.model_fields_set:
            _dict['inRoom'] = None

        # set to None if quota_limit (nullable) is None
        # and model_fields_set contains the field
        if self.quota_limit is None and "quota_limit" in self.model_fields_set:
            _dict['quotaLimit'] = None

        # set to None if is_custom_quota (nullable) is None
        # and model_fields_set contains the field
        if self.is_custom_quota is None and "is_custom_quota" in self.model_fields_set:
            _dict['isCustomQuota'] = None

        # set to None if used_space (nullable) is None
        # and model_fields_set contains the field
        if self.used_space is None and "used_space" in self.model_fields_set:
            _dict['usedSpace'] = None

        # set to None if external (nullable) is None
        # and model_fields_set contains the field
        if self.external is None and "external" in self.model_fields_set:
            _dict['external'] = None

        # set to None if password_protected (nullable) is None
        # and model_fields_set contains the field
        if self.password_protected is None and "password_protected" in self.model_fields_set:
            _dict['passwordProtected'] = None

        # set to None if expired (nullable) is None
        # and model_fields_set contains the field
        if self.expired is None and "expired" in self.model_fields_set:
            _dict['expired'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FolderDtoString from a dict"""
        if obj is None:
            return None


        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "title": obj.get("title"),
            "access": obj.get("access"),
            "shared": obj.get("shared"),
            "created": ApiDateTime.from_dict(obj["created"]) if obj.get("created") is not None else None,
            "createdBy": EmployeeDto.from_dict(obj["createdBy"]) if obj.get("createdBy") is not None else None,
            "updated": ApiDateTime.from_dict(obj["updated"]) if obj.get("updated") is not None else None,
            "autoDelete": ApiDateTime.from_dict(obj["autoDelete"]) if obj.get("autoDelete") is not None else None,
            "rootFolderType": obj.get("rootFolderType"),
            "parentRoomType": obj.get("parentRoomType"),
            "updatedBy": EmployeeDto.from_dict(obj["updatedBy"]) if obj.get("updatedBy") is not None else None,
            "providerItem": obj.get("providerItem"),
            "providerKey": obj.get("providerKey"),
            "providerId": obj.get("providerId"),
            "order": obj.get("order"),
            "id": obj.get("id"),
            "rootFolderId": obj.get("rootFolderId"),
            "originId": obj.get("originId"),
            "originRoomId": obj.get("originRoomId"),
            "originTitle": obj.get("originTitle"),
            "originRoomTitle": obj.get("originRoomTitle"),
            "canShare": obj.get("canShare"),
            "security": FileDtoIntegerSecurity.from_dict(obj["security"]) if obj.get("security") is not None else None,
            "requestToken": obj.get("requestToken"),
            "parentId": obj.get("parentId"),
            "filesCount": obj.get("filesCount"),
            "foldersCount": obj.get("foldersCount"),
            "isShareable": obj.get("isShareable"),
            "isFavorite": obj.get("isFavorite"),
            "new": obj.get("new"),
            "mute": obj.get("mute"),
            "tags": obj.get("tags"),
            "logo": Logo.from_dict(obj["logo"]) if obj.get("logo") is not None else None,
            "pinned": obj.get("pinned"),
            "roomType": obj.get("roomType"),
            "private": obj.get("private"),
            "indexing": obj.get("indexing"),
            "denyDownload": obj.get("denyDownload"),
            "lifetime": RoomDataLifetimeDto.from_dict(obj["lifetime"]) if obj.get("lifetime") is not None else None,
            "watermark": WatermarkDto.from_dict(obj["watermark"]) if obj.get("watermark") is not None else None,
            "type": obj.get("type"),
            "inRoom": obj.get("inRoom"),
            "quotaLimit": obj.get("quotaLimit"),
            "isCustomQuota": obj.get("isCustomQuota"),
            "usedSpace": obj.get("usedSpace"),
            "external": obj.get("external"),
            "passwordProtected": obj.get("passwordProtected"),
            "expired": obj.get("expired"),
            "fileEntryType": obj.get("fileEntryType")
        })
        return _obj


